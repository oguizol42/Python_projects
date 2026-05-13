from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum


class Colors(str, Enum):
    green = "green"
    yellow = "yellow"
    red = "red"
    gray = "gray"


class Drone_Map:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.map_text: str = None

    def loading_map(self) -> None:
        """Loading Map from File"""
        try:
            fd: int = open(self.file_name, "r")
            self.map_text: str = fd.read()
            fd.close()
        except FileNotFoundError as e:
            print(e)
        except IsADirectoryError as e:
            print(e)

    def display_map(self) -> None:
        """Display Graphical Map from File"""
        try:
            if self.map_text is None:
                raise AttributeError("No Map Loaded")
            print(self.map_text)
        except AttributeError as e:
            print(e)

    # Voir ci possible de faire une classe parsing dans la classe Drone_Map
    # pour recuperer des donnees valides
    class CheckMap(BaseModel):
        """Check Every Variables which Define Map"""

        # destination: str = Field(min_length=3, max_length=50)
        # duration_days: int = Field(ge=1, le=3650)

        nb_drones: int
        start_hub: tuple[str, int, int, Optional[Colors]]
        end_hub: tuple[str, int, int, Optional[Colors]]
        zone_list: list[tuple[str, int, int, Optional[str], Optional[Colors]]]

        @model_validator(mode="after")
        def map_validation_rules(self) -> "CheckMap":
            name_list: list[str] = []

            # check numer of drones
            if not self.nb_drones > 0:
                raise ValueError("There are not enough drones")

            # check zones
            name_list.append(self.start_hub[0])
            if self.end_hub[0] in name_list:
                raise ValueError(
                    f"The name: '{self.end_hub[0]}' is already exist"
                )
            name_list.append(self.end_hub[0])

            return self

    def parse_map(self) -> bool:
        """Check File Content"""
        if self.map_text is None:
            return False
        return True


# The input file must respect the expected structure and syntax:
# • The first line must define the number of drones using nb_drones: <positive_integer>.
# • The program must be able to handle any number of drones.
# • There must be exactly one start_hub: zone and one end_hub: zone.
# • Each zone must have a unique name and valid integer coordinates.
# • Zone names can use any valid characters but dashes and spaces.
# • Connections must link only previously defined zones using connection: <zone1>-<zone2>
# [metadata].
# • The same connection must not appear more than once (e.g., a-b and b-a are con-
# sidered duplicates).
# • Any metadata block (e.g., [zone=... color=...] for zones, [max_link_capacity=...]
# for connections) must be syntactically valid.
# • Zone types must be one of: normal, blocked, restricted, priority. Any invalid
# type must raise a parsing error.
# • Capacity values (max_drones for zones, max_link_capacity for connections) must
# be positive integers.
# • Any other parsing error must stop the program and return a clear error message
# indicating the line and cause


# Map File Loading
# Map Parsing
# Map Display


class Drones_Fly:
    def __init__(self, qty_drones: int) -> None:
        pass

    class Drone:
        def __init__(self, qty_drones: int) -> None:
            pass


# Creating each Drones From class Drone
# Moving Algorythm
# Memorising Moving of Each turn for each Drone


class Manage_flies:
    def __init__(self) -> None:
        pass


# Manage Drones List Creation
#   (after Loading and Parsing of Map by class Drone_Map)
# Excute Algorythm (by Drone_Fly class)


def main() -> None:
    test_map: Drone_Map = Drone_Map("maps/easy/01_linear_path.txt")
    test_map2: Drone_Map = Drone_Map("maps/easy/01_linear_path2")
    test_map3: Drone_Map = Drone_Map("maps/easy")

    test_map.display_map()
    print()
    test_map.loading_map()
    print()
    test_map.display_map()

    print()
    test_map2.loading_map()
    print()
    test_map3.loading_map()


if __name__ == "__main__":
    main()
