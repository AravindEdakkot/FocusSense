import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load dataset
data = pd.read_csv("./real_data.csv")

# Features and labels  
X = data[["wpm", "avg_delay", "pause", "error", "variance"]].values
y = data["label"].values

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y)
y = to_categorical(y)

# 🔥 Normalize features (VERY IMPORTANT)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Save scaler for later use
import joblib
joblib.dump(scaler, "scaler.pkl")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ Dense model (better for your case)
model = Sequential([
    Dense(64, activation='relu', input_shape=(X.shape[1],)),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=40, batch_size=8, validation_data=(X_test, y_test))

model.save("model.h5")

print("✅ Model trained and saved!")