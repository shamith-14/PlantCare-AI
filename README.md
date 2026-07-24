<p align="center">
  <img src="assets/banner.png" alt="PlantCare AI Banner" width="100%">
</p>

<p align="center">
  <img src="assets/logo.png" width="140" alt="PlantCare AI Logo">
</p>

<h1 align="center">🌿 PlantCare AI</h1>

<p align="center">
AI-Powered Plant Disease Detection using MobileNetV2 and Google Gemini Vision
</p>

<p align="center">
<a href="https://plantcare-ai-9kay.onrender.com">
<img src="https://img.shields.io/badge/🚀_Live_Demo-Visit-success?style=for-the-badge">
</a>

<a href="https://linkedin.com/in/shamith-rai-m">
<img src="https://img.shields.io/badge/LinkedIn-Shamith_Rai_M-0A66C2?style=for-the-badge&logo=linkedin">
</a>

<a href="https://github.com/shamith-14/PlantCare-AI">
<img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github">
</a>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-MobileNetV2-orange?style=for-the-badge&logo=tensorflow)
![Google Gemini](https://img.shields.io/badge/Google-Gemini_Vision-4285F4?style=for-the-badge&logo=google)
![Render](https://img.shields.io/badge/Hosted_on-Render-46E3B7?style=for-the-badge&logo=render)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 🌐 Live Demo

### 🚀 https://plantcare-ai-9kay.onrender.com

Try uploading a healthy or diseased leaf image to experience AI-powered plant disease detection.

---


# 📖 Overview

PlantCare AI is an intelligent web application that detects plant diseases from leaf images using a **TensorFlow MobileNetV2 deep learning model**.

Before prediction, every uploaded image is validated using **Google Gemini Vision AI** to ensure it contains a plant leaf. Images that are unrelated (such as people, vehicles, buildings, or random objects) are rejected automatically, improving prediction reliability.

Once a valid leaf image is uploaded, the application predicts the disease, displays the confidence score, and generates AI-powered disease descriptions, treatment recommendations, and prevention tips using **Google Gemini AI**.

The model is trained on the **PlantVillage Dataset**, containing thousands of labeled images across multiple plant species and disease classes.

# ✨ Features

- 🌱 Plant disease detection using TensorFlow MobileNetV2
- 🤖 Google Gemini Vision image validation
- 📷 Accepts leaf images (including leaves held in hand)
- 🚫 Rejects non-leaf images before prediction
- 📊 Confidence score for predictions
- 💡 AI-generated disease descriptions
- 💊 Treatment and prevention recommendations
- ⚡ Fast prediction with optimized inference
- 💻 Responsive Flask web application
- ☁️ Deployed on Render

# 🎬 Demo

<p align="center">
<img src="assets/demo.gif" width="900">
</p>

---

# 🖼️ Application Screenshots

## Home Page

<p align="center">
<img src="assets/home.png" width="900">
</p>

---

## Prediction Result

<p align="center">
<img src="assets/result.png" width="900">
</p>

---

# 🏗️ System Architecture

<p align="center">
<img src="assets/architecture.png" width="900">
</p>

---

# 🧠 AI Model

| Component | Details |
|------------|---------|
| Deep Learning Model | MobileNetV2 |
| Framework | TensorFlow / Keras |
| Dataset | PlantVillage Dataset |
| Image Validation | Google Gemini Vision |
| Disease Recommendation | Google Gemini AI |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |

---

# 🛠️ Tech Stack

### Programming Language

- Python

### Deep Learning

- TensorFlow
- Keras
- MobileNetV2

### AI

- Google Gemini AI API

### Backend

- Flask

### Frontend

- HTML
- CSS
- JavaScript

### Dataset

- PlantVillage Dataset

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```text
PlantCare-AI/
│
├── assets/
│   ├── banner.png
│   ├── logo.png
│   ├── home.png
│   ├── result.png
│   ├── architecture.png
│   └── demo.gif
│
├── database/
│
├── dataset/
│   ├── train/
│   └── val/
│
├── static/
├── templates/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/shamith-14/PlantCare-AI.git
```

```bash
cd PlantCare-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root and add your Google Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Note:** Never upload your `.env` file to GitHub. Ensure it is listed in `.gitignore`.

---

## Run the Application

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

# 🚀 Future Enhancements

- 📱 Mobile application
- 🌍 Multi-language support
- ☁️ Cloud deployment
- 📈 Disease history tracking
- 📷 Real-time camera detection
- 🌾 Fertilizer recommendation system
- 🌦️ Weather-based disease prediction

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Shamith Rai M

🎓 B.Tech in Artificial Intelligence & Machine Learning

🏫 Canara Engineering College, Mangalore

🌐 **Live Demo**

https://plantcare-ai-9kay.onrender.com

💼 **LinkedIn**

https://linkedin.com/in/shamith-rai-m

💻 **GitHub**

https://github.com/shamith-14

📧 **Email**

raishamith2005@gmail.com

---

# 🙏 Acknowledgements

- TensorFlow & Keras
- Google Gemini API
- Flask
- PlantVillage Dataset
- Render Cloud Platform
- Open Source Community

---

<p align="center">

### ⭐ If you found this project useful, please consider giving it a star!

Made with ❤️ by **Shamith Rai M**

</p>