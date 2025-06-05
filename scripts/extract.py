import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_post_data(caption, post_type):
    prompt = f"""
You are an AI that extracts structured fitness data from influencer-style social media captions. The post_type is '{post_type}'.

### If Recipe:
- recipe_name
- macros_per_serving
- ingredients (quantity, unit, item)
- steps

### If Workout:
- workout_goal
- workout_type
- exercises (name, duration, focus)
- weekly_frequency

Caption:
"""{caption}"""
Return only JSON.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message['content']
