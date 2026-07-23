from google import genai
from config import GEMINI_API_KEY

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