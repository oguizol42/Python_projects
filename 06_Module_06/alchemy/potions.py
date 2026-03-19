from alchemy.elements import (
    create_fire,
    create_water,
    create_earth,
    create_air,
)


def healing_potion() -> str:
    """Healing Potion"""
    return f"heal(): Healing potion brewed with {create_fire()}"
    f" and {create_water()}"


def strength_potion() -> str:
    """Strength Potion"""
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Invisibility Potion"""
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion() -> str:
    """Wisdom Potion"""
    return f"Wisdom potion brewed with all elements: {create_fire()} "
    f"{create_water()}, "
    f"{create_earth()}, "
    f"{create_air()}"
