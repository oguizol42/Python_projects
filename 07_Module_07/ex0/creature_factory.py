from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Fire"

    def attack(self) -> str:
        return f"{self.name} uses Ember!"

    def describe(self) -> str:
        return f"{super().describe()}"


class Pyrodon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"

    def describe(self) -> str:
        return f"{super().describe()}"


class Aquabub(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"

    def describe(self) -> str:
        return f"{super().describe()}"


class Torragon(Creature):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.type = "Water"

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"

    def describe(self) -> str:
        return f"{super().describe()}"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon")
