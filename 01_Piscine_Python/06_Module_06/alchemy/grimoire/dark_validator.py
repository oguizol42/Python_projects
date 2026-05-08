from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    if any(ingredient in ingredients.lower() for ingredient in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
