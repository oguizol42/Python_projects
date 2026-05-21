import parsing

# from pydantic import BaseModel, Field, ValidationError, model_validator
# from typing import Optional
# from enum import Enum


class Drone_Map(parsing.MapParsing):
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
    test_map.map_parsing()
    test_map.display_map()

    print()
    test_map2.loading_map()
    print()
    test_map3.loading_map()


if __name__ == "__main__":
    main()
