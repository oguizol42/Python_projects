from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    return f"{spell_name} ({validate_ingredients(ingredients)})"
