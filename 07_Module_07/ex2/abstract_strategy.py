from abc import ABC, abstractmethod
from typing import cast
from ex0.creature_factory import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):

    # In case an invalid strategy-Creature combination is tested,
    # the is_valid method
    # returns False. If the act method is called with an invalid combination,
    # a dedicated
    # exception is raised with a clear message

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
            return (
                "Battle error, aborting tournament: Invalid Creature "
                f"'{creature.__class__.__name__}' for this normal strategy"
            )
        else:
            return f"{creature.attack()}"

    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        if isinstance(creature, Creature):
            return True
        else:
            return False


# Suitable for Creature with transform capabilities
class AggressiveStrategy(BattleStrategy):
    """Transform, attack, and revert during the tournament."""

    def act(self, creature: Creature) -> str:
        """Called by the tournament script"""
        if self.is_valid(creature) is False:
            return (
                "Battle error, aborting tournament: Invalid Creature "
                f"'{creature.__class__.__name__}' for this aggressive strategy"
            )
        else:
            # creature_cast = cast(TransformCapability, Creature)
            return (
                f"{creature.transform()}\n"
                f"{creature.attack()}\n"
                f"{creature.revert()}"
            )

    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        if isinstance(creature, TransformCapability):
            return True
        else:
            return False


# suitable for Creature with healing capabilities
class DefensiveStrategy(BattleStrategy):
    """Attack and then heal during the tournament"""

    def act(self, creature: Creature) -> str:
        """Called by the tournament script"""
        if self.is_valid(creature) is False:
            return (
                "Battle error, aborting tournament: Invalid Creature "
                f"'{creature.__class__.__name__}' for this defensive strategy"
            )
        else:
            # creature_cast = cast(HealCapability, Creature)
            return f"{creature.attack()}\n" f"{creature.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        """Is the Creature suitable for the strategy ?"""
        if isinstance(creature, HealCapability):
            return True
        else:
            return False
