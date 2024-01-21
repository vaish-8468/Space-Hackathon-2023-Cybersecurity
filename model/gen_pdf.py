import csv
import pdfkit

def read_logs_from_csv(csv_path):
  logs = []
  with open(csv_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      logs.append(row)
  return logs

def generate_pdf(logs, output_path='log_report.pdf', template_path='template.html'):
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
