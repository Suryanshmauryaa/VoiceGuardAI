# save_dummy_emotion_model.py
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

model = Sequential([
    Input(shape=(100,)),  # adjust input shape to your data
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')  # suppose 5 emotion classes
])

model.save("models/emotion_model.h5")