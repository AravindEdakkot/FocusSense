from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from features import extract_features
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Load model + scaler
model = load_model("model.h5")
scaler = joblib.load("scaler.pkl")

labels = ["Focused 🧠", "Distracted 😵", "Fatigued 😴"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or len(data) < 5:
        return jsonify({"label": "Not enough data"})

    df = pd.DataFrame(data)

    # Feature extraction
    features = extract_features(df)

    # 🔥 Save to CSV
    import os
    df_features = pd.DataFrame([features], columns=[
        "wpm", "avg_delay", "pause", "error", "variance"
    ])
    df_features["label"] = "Distracted"  # temporary

    file_path = "real_data.csv"

    if not os.path.isfile(file_path):
        df_features.to_csv(file_path, index=False)
    else:
        df_features.to_csv(file_path, mode='a', header=False, index=False)

    # Prediction
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled, verbose=0)

    label_index = np.argmax(prediction)

    return jsonify({
        "label": labels[label_index],
        "confidence": float(np.max(prediction))
    })
if __name__ == "__main__":
    app.run(debug=True)