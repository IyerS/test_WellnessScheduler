def classify_post_type(text):
    text = text.lower()
    if any(keyword in text for keyword in ['ingredients', 'calories', 'macros', 'servings']):
        return 'recipe'
    elif any(keyword in text for keyword in ['plank', 'core', 'reps', 'routine', 'workout']):
        return 'workout'
    else:
        return 'other'
