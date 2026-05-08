from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return f"{spell_name} ({validate_ingredients(ingredients)})"
