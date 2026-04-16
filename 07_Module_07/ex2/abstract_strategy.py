from abc import ABC, abstractmethod
from ex0.creature_factory import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Called by the tournament script"""
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        pass


# Suitable for any Creature
class NormalStrategy(BattleStrategy):
    """Use the attack method during the tournament"""

    def act(self, creature: Creature) -> str:
        """Called by the tournament script"""
        if self.is_valid(creature) is False:
            raise Exception(
                "Invalid Creature "
                f"'{creature.name}' for this normal strategy"
            )
        else:
            return f"{creature.attack()}"

    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        return hasattr(creature, "attack")


# Suitable for Creature with transform capabilities
class AggressiveStrategy(BattleStrategy):
    """Transform, attack, and revert during the tournament."""

    def act(self, creature: Creature) -> str:
        """Called by the tournament script"""
        if not isinstance(creature, TransformCapability):
            raise Exception(
                "Invalid Creature "
                f"'{creature.name}' for this aggressive strategy"
            )
        else:
            return (
                f"{creature.transform()}\n"
                f"{creature.attack()}\n"
                f"{creature.revert()}"
            )

    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        return hasattr(creature, "transform") and hasattr(creature, "revert")


# suitable for Creature with healing capabilities
class DefensiveStrategy(BattleStrategy):
    """Attack and then heal during the tournament"""

    def act(self, creature: Creature) -> str:
        """Called by the tournament script"""
        if not isinstance(creature, HealCapability):
            raise Exception(
                "Invalid Creature "
                f"'{creature.name}' for this defensive strategy"
            )
        else:
            return f"{creature.attack()}\n" f"{creature.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        return hasattr(creature, "heal")
