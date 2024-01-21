import re

# Function to detect unusual HTTP Methods
def detect_unusual_method(data):
  if data['Possible Anomaly'] == True and data['HTTP Method'] not in ['GET', 'POST']:
      return 'Unusual HTTP Method'
  else:
      return ''

# Function to detect and mark attack types
def detect_sql_injection(row):
  # Define detection patterns
  patterns = {
      'Union-based SQL Injection; ': r'(\bUNION\b|\bSELECT\b|\bFROM\b|\bWHERE\b)\s*.*\bSELECT\b',
      'Error-based SQL Injection; ': r'\b(ORA-|MySQL error|SQL Server error|PostgreSQL ERROR)\b',
      'Time-based Blind SQL Injection; ': r'\b(SLEEP\s*\(\s*\d+\s*\)|WAITFOR\s+DELAY\s+\'\d+:\d+:\d+\')\b',
      'Boolean-based Blind SQL Injection; ': r'\b(TRUE\b|\bFALSE\b|\bAND\b|\bOR\b|\bNOT\b)',
      'Tautology-based SQL Injection; ': r'\b\d+\s*=\s*\d+\b',
  }
  for attack_type, pattern in patterns.items():
      if re.search(pattern, row['Requested File Path']) or re.search(pattern, row['User Agent']):
          return 'SQL Injection'
  return ''

# Function to detect and mark security misconfigurations
def detect_security_misconfigurations(row):
  # Define security misconfiguration detection patterns
  patterns = {
      'Access to Sensitive Files or Directories': r'/etc/passwd|\b/admin/config.php\b',
      'Directory Listing Attempts': r'/directory/',
      'Unauthorized Access Attempts': r'/login',
      'Open Redirect': r'\?redirect=http://malicious-site.com',
  }
  for misconfig_type, pattern in patterns.items():
      if re.search(pattern, row['Requested File Path']) or re.search(pattern, row['User Agent']):
          return 'Random Attack'
  return ''

def labelling(df):
  df['Possible Anomaly'] = df['Status Code'].astype(int).apply(lambda x: False if x < 300 else True)

  # Apply the function to each row of the DataFrame to create the 'Anomaly Type' column and detect Unusual Method
  df['Anomaly Type'] = df.apply(detect_unusual_method, axis=1)

  # Sort the DataFrame by 'Time Stamp'
  df = df.sort_values('Time Stamp')
  # Create the 'Frequency Count' column
  df['Request Count'] = df.groupby(['IP Address', 'Time Stamp']).cumcount() + 1
  # Detect Unusual Traffic
  df.loc[(df['Request Count'] > 15) & (df['Anomaly Type'] == ''), 'Anomaly Type'] = 'Unusual Traffic'

  # Detet SQL Injection
  df['Anomaly Type'] = df.apply(lambda row: detect_sql_injection(row) if row['Anomaly Type']=='' else row['Anomaly Type'], axis=1)

  # Detect Random Attacks
  df['Anomaly Type'] = df.apply(lambda row: detect_security_misconfigurations(row) if row['Anomaly Type']=='' else row['Anomaly Type'], axis=1)

  # Fill empty values in the 'Anomaly Type' column with 'Valid'
  df['Anomaly Type'].replace('', 'Valid Request', inplace=True)

  return df
