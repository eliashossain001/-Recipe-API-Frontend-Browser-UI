import json
import math
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recipes_api.settings")
django.setup()

from recipes.models import Recipe

# Load the JSON file
with open("recipes.json", "r") as f:
    recipes = json.load(f)

for recipe in recipes:
    rating = recipe.get("rating")
    prep_time = recipe.get("prep_time")
    cook_time = recipe.get("cook_time")
    total_time = recipe.get("total_time")

    # Handle NaN
    def safe_number(val):
        if val is None:
            return None
        if isinstance(val, float) and math.isnan(val):
            return None
        if isinstance(val, str) and val.lower() == "nan":
            return None
        return val

    rating = safe_number(rating)
    prep_time = safe_number(prep_time)
    cook_time = safe_number(cook_time)
    total_time = safe_number(total_time)

    Recipe.objects.create(
        cuisine=recipe.get("cuisine"),
        title=recipe.get("title"),
        rating=rating,
        prep_time=prep_time,
        cook_time=cook_time,
        total_time=total_time,
        description=recipe.get("description"),
        nutrients=recipe.get("nutrients"),
        serves=recipe.get("serves")
    )

print("✅ Recipes loaded successfully!")
