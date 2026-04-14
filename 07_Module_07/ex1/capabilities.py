from abc import ABC, abstractmethod
from ex0.creature_factory import CreatureFactory, Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class HealingCreatureFactory(CreatureFactory):
    def __init__(self) -> None:
        self.base_name = "Sproutling"
        self.class_base = HealingCreatureFactory.Sproutling
        self.evolved_name = "Bloomelle"
        self.class_evolved = HealingCreatureFactory.Bloomelle

    class Sproutling(Creature, HealCapability):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self.type = "Grass"
            self.target: str = "itself"

        def attack(self) -> str:
            return f"{self.name} uses Vine Whip!"

        def describe(self) -> str:
            return f"{super().describe()}"

        def heal(self) -> str:
            return f"{self.name} heals {self.target} for a small amount"

    class Bloomelle(Creature, HealCapability):
        def __init__(self, name: str) -> None:
            super().__init__("Bloomelle")
            self.type = "Grass/Fairy"
            self.target: str = "itself and others"

        def attack(self) -> str:
            return f"{self.name} uses Petal Dance!"

        def describe(self) -> str:
            return f"{super().describe()}"

        def heal(self) -> str:
            return f"{self.name} heals {self.target} for a large amount"

    def create_base(self) -> Sproutling:
        return self.class_base(self.base_name)

    def create_evolved(self) -> Bloomelle:
        return self.class_evolved(self.evolved_name)


class TransformCreatureFactory(CreatureFactory):
    class Shiftling(Creature, TransformCapability):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self.type = "Normal"
            self.normal: bool = True

        def attack(self) -> str:
            if self.normal is True:
                return f"{self.name} attacks normally"
            else:
                return f"{self.name} performs a boosted strike!"

        def describe(self) -> str:
            return f"{super().describe()}"

        def transform(self) -> str:
            self.normal = False
            return f"{self.name} shifts into a sharper form!"

        def revert(self) -> str:
            self.normal = True
            return f"{self.name} returns to normal."

    class Morphagon(Creature, TransformCapability):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            self.type = "Normal/Dragon"
            self.normal: bool = True

        def attack(self) -> str:
            if self.normal is True:
                return f"{self.name} attacks normally"
            else:
                return f"{self.name} unleashes a devastating morph strike!"

        def describe(self) -> str:
            return f"{super().describe()}"
        
        def transform(self) -> str:
            self.normal = False
            return f"{self.name} morphs into a dragonic battle form!"

        def revert(self) -> str:
            self.normal = True
            return f"{self.name} returns to normal."

    def create_base(self) -> Shiftling:
        return self.class_base(self.base_name)

    def create_evolved(self) -> Morphagon:
        return self.class_evolved(self.evolved_name)


# class TransformCapability(ABC):
#     @abstractmethod
#     def transform(self, state: str) -> str:
#         pass

#     @abstractmethod
#     def revert(self, state: str) -> str:
#         pass
