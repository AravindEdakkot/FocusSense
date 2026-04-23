# 🧠 FocusSense – LSTM-Based Typing Behavior Analyzer

FocusSense is an AI-powered web application that analyzes **typing behavior in real-time** to determine a user’s mental state:  
**Focused 🧠, Distracted 😵, or Fatigued 😴**.

It uses **keystroke dynamics + LSTM (Long Short-Term Memory)** to learn patterns in typing speed, pauses, and consistency.

---

## 🚀 Features

- ⌨️ Real-time keystroke tracking from browser  
- 🧠 AI-based mental state prediction  
- 🔁 LSTM model for sequence learning  
- 📊 Feature extraction (delay, pause, variance)  
- 🌐 Flask REST API backend  
- 🎨 Clean modern UI  
- ⚡ Fast predictions  

---

## 🧠 How It Works

### 1. Keystroke Capture
The frontend records:
- Key pressed  
- Timestamp (`performance.now()`)

---

### 2. Feature Extraction

From raw keystrokes:

- **Average Delay** → typing speed  
- **Pause** → hesitation frequency  
- **Variance** → typing consistency  

---

### 3. Sequence Modeling (LSTM)

[delay, pause, variance] → sequence → LSTM → prediction


---

### 4. Output

| State | Behavior |
|------|--------|
| 🧠 Focused | Fast, smooth typing |
| 😵 Distracted | Irregular typing with pauses |
| 😴 Fatigued | Slow typing with long pauses |

---

## 🏗️ Project Structure
```
focussense/
│
├── backend/
│ ├── app.py
│ ├── train.py
│ ├── model.py
│ ├── features.py
│ ├── generate_dataset.py
│ ├── model.h5
│ └── scaler.pkl
│
├── frontend/
│ ├── index.html
│ └── styles.css
│
├── real_data.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone Repository

---

### 2. Create Virtual Environment
```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install Dependencies
```
pip install -r requirements.txt
```

---

### 4. Generate Dataset
```
python backend/generate_dataset.py
```

---

### 5. Train Model
```
python backend/train.py
```


### 6. Run Backend
```
python backend/app.py
```

### 7. Open Frontend

Open:
```
frontend/index.html
```

---

## 🧪 Usage

1. Start typing in the textbox  
2. Click **Analyze**  
3. View prediction:

---

## 📊 Technologies Used

- Python  
- Flask  
- TensorFlow / Keras  
- NumPy, Pandas  
- Scikit-learn  
- HTML, CSS, JavaScript  

---

## ⚠️ Limitations

- Requires sufficient typing data  
- Accuracy depends on dataset quality  
- Not personalized per user (yet)

---

## 🚀 Future Improvements

- 📈 Real-time prediction (no button)  
- 📊 Typing analytics dashboard  
- 🧠 Personalized learning  
- 📱 Mobile support  
- 🔥 Advanced models (GRU / Attention)

---

## 💡 Key Insight

This project demonstrates how human behavioral patterns (typing) can be used to infer cognitive states using AI.

---

## 📸 Demo

_Add screenshots or GIF here_

---

## 👨‍💻 Author

Aravind E 
https://github.com/AravindEdakkot
---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 🏁 Final Note
Data → Feature Engineering → LSTM → API → UI → Prediction
