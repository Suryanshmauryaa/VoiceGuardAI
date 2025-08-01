from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import os

# Create dummy emotion classification model
model = Sequential([
    Dense(128, activation='relu', input_shape=(100,)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(5, activation='softmax')  # Assuming 5 emotion classes
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Ensure 'models/' folder exists
os.makedirs("models", exist_ok=True)

# Save the dummy model
model.save("models/emotion_model.h5")

print("✅ Dummy emotion_model.h5 saved successfully in 'models/' folder.")
