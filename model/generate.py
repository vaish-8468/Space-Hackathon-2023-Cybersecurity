from gen_pdf import read_logs_from_csv, generate_pdf
from gen_email import generate_email, analyze_logs, send_email, should_generate_email

csv_path = '/content/result.csv'  # Replace with the actual path to your CSV file
logs = read_logs_from_csv(csv_path)

# Generate PDF with logs using HTML template
generate_pdf(logs, output_path='/content/drive/MyDrive/Space Hackathon 2023/anomaly_detection_report.pdf', template_path='/content/drive/MyDrive/ProximaCentauriG5T1/model/index (1).html')

anomalies = analyze_logs(csv_path)
if should_generate_email(): 
        if anomalies:
          generate_email(anomalies)
        csv_path = '/content/drive/MyDrive/Space Hackathon 2023/result.csv'  # Replace with the actual path to your CSV file
        logs = read_logs_from_csv(csv_path)

        # Generate PDF with logs using HTML template
        generate_pdf(logs, output_path='/content/drive/MyDrive/Space Hackathon 2023/anomaly_detection_report.pdf', template_path='/content/index.html')
