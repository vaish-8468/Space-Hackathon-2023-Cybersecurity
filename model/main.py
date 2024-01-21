from train import train_model
from data_preprocessing import read_data, handle_missing_data

# Add path to the .txt file
file_path = '/content/drive/MyDrive/ProximaCentauriG5T1/server_logs.txt'  

# Read and preprocess the DataFrame
df = read_data(file_path)
df = handle_missing_data(df)

# Train the model and load it
train_model(df)