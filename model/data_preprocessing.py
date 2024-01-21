import pandas as pd

def read_data(file_path):
    # Read the .txt file into a list and convert it to a DataFrame
    with open(file_path, 'r') as f:
        log_entries = f.readlines()
    df = pd.DataFrame(log_entries, columns=['log'])

    # Regular expression pattern to extract features from the log
    pattern = r'(?P<IP_Address>\S+) \S+ \S+ \[(?P<Time_Stamp>.*?)\] "(?P<HTTP_Method>\w+) (?P<Requested_File_Path>.*?) (?P<HTTP_Version>HTTP\/\d\.\d)" (?P<Status_Code>\d{3}) (?P<Bytes_Received>\S*) "(?P<Referer_File_Path>.*?)" "(?P<User_Agent>.*?)"'

    df[['IP Address', 'Time Stamp', 'HTTP Method', 'Requested File Path', 'HTTP Version', 'Status Code', 'Bytes Received', 'Referer File Path', 'User Agent']] = df['log'].str.extract(pattern)

    return df

def handle_missing_data(df):
    # Drop the rows with empty values
    df.dropna(axis=0, how='any', inplace=True)
    return df
    