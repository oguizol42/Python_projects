from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """Transmutation to Gold"""
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """Stone to Transmuting"""
    return f"Stone transmuted to gem using {create_earth()}"
