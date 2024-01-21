import pickle
from label_data import labelling
from keras.models import Sequential
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
from data_preprocessing import read_data, handle_missing_data

def split_data(df, tokenizer):
  # Split the data into training and testing sets
  X_train_log, X_test_log, y_train, y_test = train_test_split(df['log'], to_categorical(df['Anomaly Type']), test_size=0.2, random_state=42)
  
  X_train = tokenizer.texts_to_sequences(X_train_log)
  X_train = pad_sequences(X_train)

  X_test = tokenizer.texts_to_sequences(X_test_log)
  X_test = pad_sequences(X_test)

  return X_train, X_test, y_train, y_test

def train_model(df):
  df = labelling(df)  
  # Encode the 'Anomaly Type' column
  label_encoder = LabelEncoder()
  df['Anomaly Type'] = label_encoder.fit_transform(df['Anomaly Type'])

  # Tokenize the 'log' column
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(df['log'])

  # Save Tokenizer and LabelEncoder to files
  with open('tokenizer.pkl', 'wb') as tokenizer_file:
      pickle.dump(tokenizer, tokenizer_file)

  with open('label_encoder.pkl', 'wb') as label_encoder_file:
      pickle.dump(label_encoder, label_encoder_file)

  # Load Tokenizer and LabelEncoder
  with open('tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

  with open('label_encoder.pkl', 'rb') as label_encoder_file:
    label_encoder = pickle.load(label_encoder_file)

  X_train, X_test, y_train, y_test = split_data(df, tokenizer)

  # Define the LSTM model
  model = Sequential()
  model.add(Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=100, input_length=X_train.shape[1]))
  model.add(LSTM(100))
  model.add(Dense(len(label_encoder.classes_), activation='softmax'))

  # Compile the model
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

  # Train the model
  model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2)

  # Evaluate the model
  accuracy = model.evaluate(X_test, y_test)[1]
  print(f"Accuracy: {accuracy}")

  # Save the model
  model.save('model.h5')
