import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.utils import to_categorical
from model import create_model
import joblib
from features import extract_sequence

data = pd.read_csv("./real_data.csv")

X = []
y = []

for session_id in data["session_id"].unique():
    session = data[data["session_id"] == session_id]

    seq = extract_sequence(session)

    if len(seq) < 5:
        continue

    X.append(seq[:5])
    y.append(session["label"].iloc[0])

X = np.array(X)
y = np.array(y)

print("X shape:", X.shape)

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y)
y = to_categorical(y)
print("Label mapping:", list(le.classes_))
# Scale
scaler = StandardScaler()
X = scaler.fit_transform(X.reshape(-1, 3)).reshape(X.shape)

joblib.dump(scaler, "scaler.pkl")

# Model
model = create_model((X.shape[1], X.shape[2]))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=15, batch_size=4)

model.save("model.h5")

print("✅ Training complete")