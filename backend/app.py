from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib
from features import extract_sequence

app = Flask(__name__)
CORS(app)

model = load_model("model.h5")
scaler = joblib.load("scaler.pkl")

labels = ["Distracted 😵", "Fatigued 😴", "Focused 🧠"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    if not data or len(data) < 20:
        return jsonify({"label": "Not enough data"})

    df = pd.DataFrame(data)

    sequence = extract_sequence(df)

    if len(sequence) < 5:
        return jsonify({"label": "Not enough sequence"})

    sequence = sequence[:5]
    print("Features BEFORE scaling:", sequence)
    print("Avg delay:", np.mean(sequence[:, 0]))

    sequence = scaler.transform(sequence.reshape(-1, 3)).reshape(1, 5, 3)

    prediction = model.predict(sequence, verbose=0)

    print("Prediction:", prediction)
    print("Features:", sequence)
    return jsonify({
        "label": labels[np.argmax(prediction)],
        "confidence": float(np.max(prediction))
    })
    

if __name__ == "__main__":
    app.run(debug=True)