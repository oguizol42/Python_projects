from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Manager of Transmuting Stone to Gold"""
    return (
        f"Philosopher’s stone created using {lead_to_gold()}"
        f" and {healing_potion()}"
    )


def elixir_of_life() -> str:
    """Creat Elixir of Life"""
    return "Elixir of life: eternal youth achieved!"
