import pickle
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from data_preprocessing import read_data, handle_missing_data
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Add path to your .txt file
file_path = '/content/drive/MyDrive/ProximaCentauriG5T1/server_logs.txt'  

# Read and preprocess the DataFrame
df = read_data(file_path)
df = handle_missing_data(df)

model = load_model('/content/model.h5')  # Add the path where model gets loaded

# Load Tokenizer and LabelEncoder
with open('tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)
with open('label_encoder.pkl', 'rb') as label_encoder_file:
    label_encoder = pickle.load(label_encoder_file)

# Tokenize and pad the new data
X = tokenizer.texts_to_sequences(df['log'])
X = pad_sequences(X, maxlen=model.input_shape[1])

# Make predictions
predictions = model.predict(X)

# Decode the predicted values back to original labels and add them to the DataFrame
decoded_predictions = label_encoder.inverse_transform(predictions.argmax(axis=1))
df['Prediction'] = decoded_predictions

# Save the result to a CSV file
df.to_csv('result.csv', index=False)
