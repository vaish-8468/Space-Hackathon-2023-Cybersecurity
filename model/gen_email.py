import csv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Global variable to store the timestamp of the last email generation
last_email_timestamp = 0

def generate_email(anomalies):
    global last_email_timestamp

    subject = '[IMPORTANT]--Security Anomalies Detected! ☠️'

    # Read HTML content from a file
    with open('/content/drive/MyDrive/ProximaCentauriG5T1/model/index (1).html', 'r') as html_file:
        html_content = html_file.read()

    # Replace placeholders in HTML content with actual data
    html_content = html_content.replace('[SubjectPlaceholder]', subject)
    
    anomalies_html = ''
    for anomaly in anomalies:
        anomalies_html += f"<tr><td>{anomaly.get('Time Stamp')}</td>"
        anomalies_html += f"<td>{anomaly.get('IPAddress')}</td>"
        anomalies_html += f"<td>{anomaly.get('Status Code')}</td>"
        anomalies_html += f"<td>{anomaly.get('Anomaly Type')}</td>"
        anomalies_html += f"<td>{anomaly.get('Requested File Path')}</td></tr>"

    # Replace the placeholder in HTML content with anomalies HTML
    html_content = html_content.replace('[AnomaliesPlaceholder]', anomalies_html)

    # Update the timestamp of the last email generation
    last_email_timestamp = time.time()

    # Send the email
    send_email(html_content, subject)
  
 

def analyze_logs(csv_file):
    anomalies = []

    with open(csv_file, 'r') as csv_input:
        csv_reader = csv.DictReader(csv_input)

        for row in csv_reader:
            AnomalyType = row.get('Anomaly Type', "Valid Request")

            # Example anomaly detection: if Anomaly type is not Valid, then collect the anomalous logs information
            if AnomalyType != "Valid Request":
                anomalies.append(row)

    return anomalies

def send_email(html_content,subject):
    # Your email configuration goes here
    sender_email = 'rimjhimvartika94@gmail.com'
    sender_password = 'lkch squl mpek mrdk'
    receiver_email = '2020uee0139@iitjammu.ac.in'


    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    # message.attach(MIMEText(body, 'plain'))
    message.attach(MIMEText(html_content, 'html'))

    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

def should_generate_email():
    global last_email_timestamp

    current_timestamp = time.time()
    elapsed_time = current_timestamp - last_email_timestamp

      # Only generate an email if 5 minutes have passed
    return elapsed_time >= 10
   