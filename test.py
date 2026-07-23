from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

models = [
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-flash-latest"
]

for model in models:
    print(f"\nTesting: {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Say Hello"
        )
        print("✅ Success:", response.text)

    except Exception as e:
        print("❌ Failed:", e)