def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = [
        "earth",
        "air",
        "fire",
        "water"
    ]
    if any(ingredient in ingredients.lower() for ingredient in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

# • A function validate_ingredients(ingredients: str) that returns a string with
# the ingredients and the “VALID” or “INVALID” keyword. The ingredients are
# valid if they include at least one of the allowed ingredients from the spellbook (case
# insensitive).
# Now duplicate both files to obtain dark_spellbook.py and dark_validator.py, and
# change the function names as well. Let’s say that dark magic uses the following ingredients: “bats”, “frogs”, “arsenic”, and “eyeball”.
# Time to test a few spells! Create two scripts to demonstrate that light magic avoids
# circular dependencies and laboratory explosions, and that dark magic is dangerous and
# explodes because of circular dependencies:
# • ft_kaboom_0.py will access the grimoire module directly and then record a light
# spell, flawlessly. There are multiple ways to avoid circular dependencies; you pick
# one. Be prepared to explain the different approaches during the evaluation.
# • ft_kaboom_1.py will secretly access the dark_spellbook.py directly and then try
# to record a dark spell. This must fail and raise an exception (you can choose to
# catch it or not; it’s only for pedagogical purposes), indicating that your alchemist
# laboratory has just exploded.