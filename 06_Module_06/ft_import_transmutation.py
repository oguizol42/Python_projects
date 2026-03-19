import alchemy.elements
from alchemy.elements import create_water
from alchemy.elements import (
    create_earth,
    create_fire,
)
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal


def main() -> None:
    """Import Transmutation Mastery"""
    print("=== Import Transmutation Mastery ===")
    print()
    print("Method 1 - Full module import:")
    print("alchemy.elements.create_fire(): ", end="")
    print(alchemy.elements.create_fire())
    print()
    print("Method 2 - Specific function import:")
    print("create_water(): ", end="")
    print(create_water())
    print()
    print("Method 3 - Aliased import:")
    print(heal())
    print()
    print("Method 4 - Multiple imports:")
    print("create_earth(): ", end="")
    print(create_earth())
    print("create_fire(): ", end="")
    print(create_fire())
    print("strength_potion(): ", end="")
    print(strength_potion())
    print()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()


# === Import Transmutation Mastery ===

# Method 1 - Full module import:
# alchemy.elements.create_fire(): Fire element created

# Method 2 - Specific function import:
# create_water(): Water element created

# Method 3 - Aliased import:
# heal(): Healing potion brewed with Fire element created and Water element created

# Method 4 - Multiple imports:
# create_earth(): Earth element created
# create_fire(): Fire element created
# strength_potion(): Strength potion brewed with Earth element created and Fire element created

# All import transmutation methods mastered!
