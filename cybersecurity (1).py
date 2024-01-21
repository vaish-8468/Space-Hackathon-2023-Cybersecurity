# -*- coding: utf-8 -*-
"""Cybersecurity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_kp6aW9oD98xjgYIdNueZ_cuHCLgMgdG

# This is a practise notebook for this project

Firewall logs to csv conversion using **fortilogcsv**
"""

! git clone https://github.com/N4SOC/fortilogcsv.git

!pip install fortilogcsv

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/fortilogcsv

!python3 convert.py 31Oct2023-messages.txt ##replace 31Oct2023-messages.txt with the log file
## the transformed data would be of the same name ending with .csv

"""#Self-Supervised Log Parsing"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %ls
# %cd drive/MyDrive/space hackathon

!git clone https://github.com/nulog/nulog.git

!pip install deap
!pip install recommonmark
!pip install -U scikit-learn

# Commented out IPython magic to ensure Python compatibility.
# %cd nulog/benchmark

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""## Text to Log File Conversion Code

"""

import os

def convert_txt_to_log(input_txt_path, output_log_path):
    # Check if the input file exists
    if not os.path.exists(input_txt_path):
        print(f"Error: Input file '{input_txt_path}' not found.")
        return

    # Read the content of the text file
    with open(input_txt_path, 'r') as txt_file:
        logs_content = txt_file.read()

    # Create the output log file with the new extension
    with open(output_log_path, 'w') as log_file:
        # Write the content to the log file
        log_file.write(logs_content)

    print(f"Conversion successful. Logs saved to '{output_log_path}'.")

# Example usage
input_txt_file = '/content/drive/MyDrive/space hackathon/nulog/logs/Bhuvan/ssl_access_log-20231107'  # Replace with the path to your text file
output_log_file = '/content/drive/MyDrive/space hackathon/nulog/logs/Bhuvan/convertedDocToLog.log'

convert_txt_to_log(input_txt_file, output_log_file)

# Commented out IPython magic to ensure Python compatibility.
# httpstatusrequest is made rhe content
#the model is extracting templates from https status request url
# %cd /content/drive/MyDrive/Space Hackathon 2023/nulog/benchmark
!python NuLog_benchmark.py

"""([^ ]+) - - \[([^\]]+)\] (.+) (\d+) (\d+) \"([^\"]*)\" \"([^\"]*)\"



Log Parsing Regex
"""

!pip install python-docx

"""## Code Debugging"""

import re
regex='(?P<IPAddress>.*?)\\s+(?P<UserLogin>.*?)\\s+(?P<UserAuth>.*?)\\s+(?P<DateTime>.*?)\\s+(?P<HTTPRequest>.*?)\\s+(?P<HTTPStatusCode>.*?)\\s+(?P<BytesSent>.*?)\\s+(?P<Component>.*?)\\s+(?P<Content>.*?)'
text='172.26.3.214 - - [06/Nov/2023:00:00:02 +0530] "GET /scan_m/cas_userstats/getUserStats.php?sdate=2023-11-06&edate=2023-11-06 HTTP/1.1" 200 93 "-" "python-requests/2.5.1 CPython/3.8.5 Linux/3.10.0-327.el7.x86_64"'

regex = re.compile('^' + regex + '$')

match=regex.search(text)

# headers=['Label','Timestamp',  'Date',  'Node',  'Time',  'NodeRepeat',  'Type',  'Component',  'Level',  'Content']
headers= ['IPAddress', 'UserLogin','UserAuth','DateTime','HTTPRequest','HTTPStatusCode','BytesSent','Component','Content']

message=[match.group(header) for header in headers]

print(message)

import re
regex='(?P<IPAddress>.*?)\\s+(?P<UserLogin>.*?)\\s+(?P<UserAuth>.*?)\\s+(?P<DateTime>.*?)\\s+(?P<HTTPRequest>.*?)\\s+(?P<HTTPStatusCode>.*?)\\s+(?P<BytesSent>.*?)\\s+(?P<Component>.*?)\\s+(?P<Content>.*?)'
text='172.26.3.214 - - [06/Nov/2023:00:00:02 +0530] "GET /scan_m/cas_userstats/getUserStats.php?sdate=2023-11-06&edate=2023-11-06 HTTP/1.1" 200 93 "-" "python-requests/2.5.1 CPython/3.8.5 Linux/3.10.0-327.el7.x86_64"'

regex = re.compile('^' + regex + '$')

match=regex.search(text)

# headers=['Label','Timestamp',  'Date',  'Node',  'Time',  'NodeRepeat',  'Type',  'Component',  'Level',  'Content']
headers= ['IPAddress', 'UserLogin','UserAuth','DateTime','HTTPRequest','HTTPStatusCode','BytesSent','Component','Content']

message=[match.group(header) for header in headers]

print(message)

import re

input_string = '<CLS> "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"'
# input_string = input_string.replace('\'', '')
# Define the regex pattern for splitting on space outside double quotes
regex_pattern = r'\s+'
# regex_pattern = r'(?<=<CLS> ").*?(?=")'

# Define the regex pattern for splitting on space outside double quotes

word2index = {'<PAD>': 0, '<CLS>': 1, '<MASK>': 2}
index2word = {0: '<PAD>', 1: '<CLS>', 2: '<MASK>'}
n_words = 3
# Count SOS and EOS





# Use re.split to split the string based on the regex pattern
result = re.split(regex_pattern, input_string)
n=1
for i in range(len(result)-1):
  result.insert(n," ")
  n=n+2





print("result",result)

new_filtered = []
for f in result:
  if f != None and f != '':
    new_filtered.append(f)
for w in range(len(new_filtered)):
    word=new_filtered[w]
    if word not in word2index:
      word2index[word] = n_words
      index2word[n_words] = word
      n_words += 1
    new_filtered[w] = word2index[new_filtered[w]]


# Output the result
print(new_filtered)

import re

# input_string = '<CLS> ciod: failed to read message prefix on control stream (CioStream socket to 172.16.96.116:33569'
input_string= 'IOThunderboltSwitch<0>(0x0)::listenerCallback - Thunderbolt HPD packet for route = 0x0 port = 11 unplug = 0'
input_string = input_string.replace('\'', '')

# Define the regex pattern for splitting on space outside double quotes
# regex_pattern = r'([ |:|\(|\)|=|,])|(core.)|(\.{2,})'
regex_pattern = r'([ ])|([\w-]+\.){2,}[\w-]+'
word2index = {'<PAD>': 0, '<CLS>': 1, '<MASK>': 2}
index2word = {0: '<PAD>', 1: '<CLS>', 2: '<MASK>'}
n_words = 3
# Count SOS and EOS





# Use re.split to split the string based on the regex pattern
result = re.split(regex_pattern, input_string)
print("result",result)
new_filtered = []
for f in result:
  if f != None and f != '':
    new_filtered.append(f)
print("new_filtered",new_filtered)
for w in range(len(new_filtered)):
    word=new_filtered[w]
    if word not in word2index:
      word2index[word] = n_words
      index2word[n_words] = word
      n_words += 1
    new_filtered[w] = word2index[new_filtered[w]]


# Output the result
print(new_filtered)

import re

def generate_logformat_regex(logformat):
    """ Function to generate regular expression to split log messages
    """
    headers = []
    splitters = re.split(r'(<[^<>]+>)', logformat)
    regex = ''
    for k in range(len(splitters)):
        if k % 2 == 0:
            splitter = re.sub(' +', '\\\s+', splitters[k])
            regex += splitter
        else:
            header = splitters[k].strip('<').strip('>')
            if header == 'IPAddress':
                    regex += '(?P<%s>[^ ]+)' %header
            elif header == 'DateTime':
                    regex += '(?P<%s>[^ ]+ [^ ]+)' %header
            # elif header == 'HTTPRequest':
            #         regex += '(?P<%s>\"([^\"]*)\")' %header
            elif header == 'HTTPStatusCode':
                    regex += '(?P<%s>\d+)' %header
            elif header == 'BytesSent':
                    regex += '(?P<%s>\d+)' %header
            elif header == 'Component':
                    regex += '(?P<%s>[^ ]+)' %header
            # elif header == 'Content':
            #         regex += '\"(?P<%s>[^\"]*)\"' %header
            else:
                    regex += '(?P<%s>.*?)' % header
            headers.append(header)
    regex = re.compile('^' + regex + '$')

    print("logformat...")
    print(regex)
    print(headers)

    return headers, regex

logformat = '<IPAddress> <UserLogin> <UserAuth> <DateTime> <Content> <HTTPStatusCode> <BytesSent> <Component> <UserAgent>'
headers, regex = generate_logformat_regex(logformat)

# 'filters': '([^ ]+) - - \[([^\]]+)\] (.+) (\d+) (\d+) \"([^\"]*)\" \"([^\"]*)\"',


log_line = '172.26.3.214 - - [06/Nov/2023:00:00:02 +0530] "GET /scan_m/cas_userstats/getUserStats.php?sdate=2023-11-06&edate=2023-11-06 HTTP/1.1" 200 93 "-" "python-requests/2.5.1 CPython/3.8.5 Linux/3.10.0-327.el7.x86_64"'
# log_line= '172.31.4.195 - - [06/Nov/2023:09:38:48 +0530] "GET /bhuvan_new2d_support_apis/login/login.php HTTP/2.0" 302 363 "https://bhuvan-staging1.nrsc.gov.in/wdc2.0_training/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"'

match = regex.match(log_line)
if match:
    log_data = match.groups()
    print(log_data)

"""### Python code to convert csv back into the log file format"""

import csv
import pandas as pd
from datetime import datetime

def csv_to_log(csv_file, log_file):
    with open(csv_file, 'r') as csv_input:
        csv_reader = csv.DictReader(csv_input)

        with open(log_file, 'w') as log_output:
            for row in csv_reader:

                logs = row.get('log', '-')
                print(logs)
                # timestamp_str = row.get('Timestamp', '')

                # # Assuming the timestamp is in pandas datetime format
                # timestamp = pd.to_datetime(timestamp_str, errors='coerce', utc=True)
                # timestamp_str = timestamp.strftime('%d/%b/%Y:%H:%M:%S %z') if not pd.isnull(timestamp) else '-'

                # request = row.get('Request', '-')
                # status_code = row.get('Status Code', '-')
                # bytes_transferred = row.get('Bytes', '-')
                # referer = row.get('Referer', '-')
                # user_agent = row.get('User Agent', '-')

                # log_line = f'{ip_address} - - [{timestamp}] "{request}" {status_code} {bytes_transferred} "{referer}" "{user_agent}"\n'

                log_output.write(logs)

if __name__ == "__main__":
    # Replace 'input.csv' and 'output.log' with your actual file names
    csv_to_log('/content/drive/MyDrive/space hackathon/New_data.csv', '/content/drive/MyDrive/space hackathon/nonAnomalous.log')

"""## Analytics Report

### Created log template csv
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/drive/MyDrive/Space Hackathon 2023/nulog/benchmark/AttentionParserResult/nonAnomalous (1).log_structured.csv')
df['EventTemplate'].unique()

uniqueTemplates= df['EventTemplate'].unique()

patterns_to_match = ['"GET <*> <*>', '"GET /rbi <*>', '"GET /rbi/ <*>', '"GET /anganwadi/ <*>', '"POST <*> <*>',
                     '"GET /scan_alka/mhrd_ncert/sb/sb-hi.php <*>', '"GET /scan_alka/mhrd_ncert/sb/get/legend_hindi.php?q= <*>',
                     '"GET /scan_p/bhuvanNTL/geometryState.php <*>', '"GET /scan_p/bhuvanNTL/geometryState.php?state=DELHI <*>',
                     '"GET /scan_p/bhuvanNTL/indiageometry.php <*>', '"GET /twris/geoportal/twris.php <*>',
                     '"GET /twris/geoportal/img/south-mini.png <*>', '"GET /kyrdemo/index.html <*>', '"GET /kyrdemo/ <*>',
                     '"POST /kyrdemo/index.html <*>', '"POST /kyrdemo/ <*>']

# Filter DataFrame based on the patterns
filtered_df = df[df['EventTemplate'].isin(uniqueTemplates)].drop_duplicates(subset='EventTemplate')

# Re-index eventIds
filtered_df['EventIds'] = np.arange(1, len(filtered_df) + 1)

filtered_df.to_csv('/content/drive/MyDrive/Space Hackathon 2023/nulog/logs/Bhuvan/nonAnomalous (2).log_templates.csv', index=False)

print(filtered_df)

### TESTING

!python3 NuLog_benchmark.py

"""### Integrating GPT-3"""

!pip install openai==0.18.1

import openai as ai
import os

# OPENAI_API_KEY='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'
# ai.api_key=os.environ.get('OPENAI_API_KEY')
ai.api_key='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'

# a short function that makes a call out to OpenAI’s completion API to generate a series of text tokens from a given prompt:


def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='davinci-002',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=200,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

models = ai.Model.list()

for model in models.data:
    print(model.id)

if __name__ == '__main__':
    prompt = 'Give a brief introduction on Insider Threat Detection Attack and generate a report on anomaly detection if the accuracy of the detection model is 0.76.'
    # prompt = 'Given a set of server log details, analyze the data to identify and report on potential malicious activities. The logs contain information about IP addresses, URLs, and other details. Your task is to generate a report summarizing the following:'
    response = generate_gpt3_response(prompt)

    print(response)

"""### Python script for email alert system"""

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
    with open('/content/index.html', 'r') as html_file:
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
    sender_password = ' '
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

if __name__ == "__main__":
    # Replace 'firewall_logs.csv' with the actual filename
    csv_file = '/content/drive/MyDrive/Space Hackathon 2023/result.csv'

    # Analyze firewall logs
    anomalies = analyze_logs(csv_file)

    # If anomalies are found, send an email alert



# Example usage:
    if should_generate_email():
        if anomalies:
          generate_email(anomalies)
        csv_path = '/content/drive/MyDrive/Space Hackathon 2023/result.csv'  # Replace with the actual path to your CSV file
        logs = read_logs_from_csv(csv_path)

        # Generate PDF with logs using HTML template
        generate_pdf(logs, output_path='/content/drive/MyDrive/Space Hackathon 2023/anomaly_detection_report.pdf', template_path='/content/index.html')

# Install wkhtmltopdf
!apt-get update
!apt-get install -y wkhtmltopdf

"""## PDF Generation"""

!pip install pdfkit

!pip install pdfkit
# Install wkhtmltopdf
!apt-get update
!apt-get install -y wkhtmltopdf

import csv
import pdfkit

def read_logs_from_csv(csv_path):
    logs = []
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            logs.append(row)
    return logs




def generate_pdf(logs, output_path='anomaly_detection_report.pdf', template_path='template.html'):
    try:
        # Load the HTML template
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()

        # Replace the [AnomaliesPlaceholder] with the actual data
        anomalies_html = ''
        for log in logs:
            anomalies_html += f"""
            <tr class="highlight">
                <td>{log.get('Time Stamp', '')}</td>
                <td>{log.get('IP Address', '')}</td>
                <td>{log.get('Status Code', '')}</td>
                <td>{log.get('Anomaly Type', '')}</td>
                <td class="requested-file-path">{log.get('Requested File Path', '')}</td>
            </tr>
            """

        # Replace the [AnomaliesPlaceholder] in the template
        template_content = template_content.replace('[AnomaliesPlaceholder]', anomalies_html)

        # Configure options for PDF generation
        options = {
            'page-size': 'A4',
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'encoding': 'UTF-8',
        }

        # Generate PDF from HTML content
        pdfkit.from_string(template_content, output_path, options=options)

        print(f"PDF generated successfully: {output_path}")
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")




# Example usage:
csv_path = '/content/drive/MyDrive/Space Hackathon 2023/result.csv'  # Replace with the actual path to your CSV file
logs = read_logs_from_csv(csv_path)

# Generate PDF with logs using HTML template
generate_pdf(logs, output_path='/content/drive/MyDrive/Space Hackathon 2023/anomaly_detection_report.pdf', template_path='/content/index.html')