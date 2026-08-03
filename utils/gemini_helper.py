from google import genai
from config import GEMINI_API_KEY
from PIL import Image

client = genai.Client(api_key=GEMINI_API_KEY)


def get_disease_details(disease_name):

    prompt = f"""
You are an expert agricultural scientist.

The detected plant disease is:

{disease_name}

Generate a professional plant disease report.

Return ONLY valid HTML.

Structure:

<h2>Description</h2>
<p>4-5 informative sentences.</p>

<h2>Symptoms</h2>
<ul>
<li>Exactly 5 bullet points</li>
</ul>

<h2>Causes</h2>
<ul>
<li>Exactly 5 bullet points</li>
</ul>

<h2>Treatment</h2>
<ul>
<li>Exactly 6 bullet points</li>
</ul>

<h2>Prevention</h2>
<ul>
<li>Exactly 6 bullet points</li>
</ul>

Do not use Markdown.
Do not use code blocks.
Return only HTML.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


def is_leaf_image(image_path):
    """
    Validates whether the uploaded image contains
    a clear plant leaf suitable for disease prediction.
    """

    prompt = """
You are validating an image for a plant disease detection system.

Determine whether the PRIMARY subject of the image is a plant leaf suitable for disease analysis.

Reply ONLY with:

YES

or

NO

Reply YES if:
- The main focus is a plant leaf.
- The leaf is clearly visible.
- A person is holding the leaf.
- Multiple leaves are visible but one leaf is clearly the primary subject.
- The leaf is attached to the plant but clearly visible.
- The background contains hands, sky, soil, pots, or natural surroundings.

Reply NO if:
- There is no visible plant leaf.
- The image mainly shows a person.
- The image mainly shows an animal.
- The image mainly shows a vehicle.
- The image mainly shows a building.
- The image mainly shows food.
- The image is too blurry.
- The leaf is too small or heavily occluded to analyze.

Return ONLY:

YES

or

NO
"""

    try:
        with Image.open(image_path) as image:

            # Convert to RGB
            image = image.convert("RGB")

            # Resize to reduce RAM usage
            image.thumbnail((512, 512))

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=[prompt, image]
            )

        answer = response.text.strip().upper()

        return answer == "YES"

    except Exception as e:
        print("Gemini Leaf Validation Error:", e)

        # If Gemini fails, allow prediction
        return True