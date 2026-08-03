from flask import Flask, render_template, request
from model.predict import predict_disease
from utils.gemini_helper import get_disease_details, is_leaf_image
import os
import random

tips = [
    "💧 Water plants early in the morning to reduce water loss through evaporation.",
    "🌿 Remove infected leaves immediately to prevent diseases from spreading.",
    "🌱 Rotate crops regularly to maintain soil fertility and reduce pests.",
    "☀️ Ensure plants receive adequate sunlight for healthy growth.",
    "🪱 Apply organic compost to improve soil structure and nutrients.",
    "🐞 Encourage beneficial insects like ladybugs for natural pest control.",
    "🌾 Avoid overwatering, as excess moisture promotes fungal diseases.",
    "🍂 Remove weeds regularly to minimize pest habitats and competition.",
    "🌧️ Water the soil instead of the leaves to reduce fungal infections.",
    "🔍 Inspect plants frequently for early signs of pests and diseases.",
    "🌡️ Monitor temperature changes, as extreme heat or cold can stress plants.",
    "✂️ Prune damaged or diseased branches to encourage healthy growth.",
    "🧪 Test soil pH periodically to ensure optimal nutrient availability.",
    "🌬️ Maintain proper spacing between plants for better air circulation.",
    "🚜 Use clean gardening tools to prevent the spread of plant diseases.",
    "🥕 Apply balanced fertilizers according to crop requirements.",
    "🌼 Plant companion crops to naturally deter harmful insects.",
    "💦 Install drip irrigation to save water and improve irrigation efficiency.",
    "🌱 Use certified disease-free seeds and seedlings for planting.",
    "🍃 Mulch around plants to conserve moisture and suppress weeds.",
    "🐛 Monitor leaves for insect eggs and remove them before they hatch.",
    "🌻 Avoid planting the same crop in the same field every season.",
    "🛡️ Apply recommended fungicides or pesticides only when necessary.",
    "🌿 Keep the field clean by removing fallen leaves and crop residues.",
    "🌦️ Avoid watering during rainy periods to prevent excessive soil moisture.",
    "🪴 Grow healthy seedlings in clean nursery conditions before transplanting.",
    "🌍 Improve soil drainage to prevent root rot and waterlogging.",
    "📅 Follow the recommended planting season for each crop.",
    "🚫 Do not overcrowd plants, as dense foliage encourages disease development.",
    "🌱 Healthy plants are naturally more resistant to pests and diseases—provide proper nutrition and regular care."
]

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    daily_tip = random.choice(tips)
    return render_template("index.html", daily_tip=daily_tip)


@app.route("/predict", methods=["POST"])
def predict():

    if "plant_image" not in request.files:
        return "No file uploaded."

    file = request.files["plant_image"]

    if file.filename == "":
        return "Please select an image."

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:
        # Validate image
        if not is_leaf_image(filepath):
            return render_template(
                "result.html",
                image=file.filename,
                disease="Invalid Image",
                confidence="--",
                details="""
                <h2>Invalid Image</h2>

                <p>
                The uploaded image does not appear to contain a clear plant leaf suitable
                for disease detection.
                </p>

                <p>
                Please upload a clear image of a plant leaf and try again.
                </p>
                """
            )

        # Predict disease
        disease, confidence = predict_disease(filepath)

        # Gemini report
        try:
            details = get_disease_details(disease)
        except Exception as e:
            print("Gemini Error:", e)

            details = """
            <h2>AI Report Unavailable</h2>

            <p>
            The disease was successfully detected, but the AI report
            could not be generated at this time.
            Please try again later.
            </p>
            """

        return render_template(
            "result.html",
            image=file.filename,
            disease=disease,
            confidence=f"{confidence:.2f}%",
            details=details
        )

    finally:
        # Always delete uploaded image
        if os.path.exists(filepath):
            os.remove(filepath)


if __name__ == "__main__":
    app.run(debug=True)