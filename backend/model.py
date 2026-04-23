from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_model(input_shape):
    model = Sequential()

    model.add(LSTM(64, input_shape=input_shape))
    model.add(Dropout(0.4))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(3, activation='softmax'))

    return model