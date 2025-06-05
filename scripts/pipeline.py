import pandas as pd
import json
from scripts.classify import classify_post_type
from scripts.extract import extract_post_data

# Load captions
df = pd.read_csv('data/captions_dataset.csv')
results = []

for _, row in df.iterrows():
    caption = row['raw_caption']
    post_type = classify_post_type(caption)
    print(f"Classified as: {post_type}")
    if post_type in ['recipe', 'workout']:
        extracted = extract_post_data(caption, post_type)
        results.append({
            'post_id': row['post_id'],
            'post_type': post_type,
            'structured_data': extracted
        })

with open('outputs/extracted_results.json', 'w') as f:
    json.dump(results, f, indent=2)
