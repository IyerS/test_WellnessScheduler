# Fitness Caption Extractor 🏋️🥗

This project extracts structured fitness and nutrition data from influencer social media post captions.

## Features
- Classifies posts as recipe or workout
- Extracts structured content using OpenAI GPT
- Outputs JSON data for downstream use

## Usage
1. Store your OpenAI API key in `.env`
2. Add captions to `data/captions_dataset.csv`
3. Run the pipeline:
```bash
python scripts/pipeline.py
```

## Folder Structure
- `data/`: Input captions
- `scripts/`: Classification, extraction, and orchestration logic
- `outputs/`: Extracted JSON data

## Dependencies
```bash
pip install -r requirements.txt
```

## Note
Video analysis planned for v2.0. This MVP works on caption text only.

![Python](https://img.shields.io/badge/python-3.10+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)

