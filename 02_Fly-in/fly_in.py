# import parsing
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum


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

    # PARSING

    class Colors(str, Enum):
        green = "green"
        yellow = "yellow"
        red = "red"
        gray = "gray"

    # * Verifier premiere ligne, elle doit etres ecrite comme suit: using nb_drones: <positive_integer>

    # * Tout nombre de drones doit etre gerable:
    #     - nombre negatif: Quantity of <nb_drones> drone is not correct
    #     - 0: With a quantity of 0 drone, nothing happend

    # * Presence d'exactement:
    #     - 1 start_hub: zone
    #     - 1 end_hub: zone
    # * Chaque nom de zone doit:
    #     - Avoir un nom unique
    #     - Des caracteres valides
    #     - Ne comporter aucun trait ni espace
    # * Chaque zone doit:
    #     - avoir des coordonnes valides (integer superieur ou egal a 0)
    #     - metadata: [zone=... color=...]
    #         color = None par defaut
    #         zone = normal par defaut
    #     -  Zone types must be one of: normal, blocked, restricted, priority. Any invalid
    #             type must raise a parsing error.

    # * connection: <zone1>-<zone2> [metadata]
    #     - metadata: [max_link_capacity=...]
    #     - max_link_capacity = 1 par defaut
    # * une meme connection ne doit apparaitre qu'une fois:
    #     connection: a-b et connection: b-a sont identiques

    class CheckMap(BaseModel):
        """Check Every Variables which Define Map"""

    def parse_metadata(self) -> bool:
        """check Metadata"""
        pass
        # 1/ Pour chaque variable de map, tranformer les metadata en tuple[str, str]
        # 2/ Verifier si le nombre de tuple present est coherent
        # 3/ Verifier si il n'a pas plusieurs metadata pour le meme type de data
        # 4/ verifier si les datas presents correspondent a leur variable attribue suivant leur nom
        # 5/ verifier, par une base model, si les metatadas sont valides
        # 6/ Creer les variables maps definitives
    def check_datas_format(str) -> tuple[str, str, str, Optional[str]]:
        """Check Datas Format"""
        # 1/ Si juste metadata -> None
        # 2/ Split "[" (metadata)
        # 3/ Si metadata ne fini pas par "]" -> None


    def parse_map(self) -> bool:
        """Check File Content"""
        map_list: list[str] = []
        map_list_clean: list[str] = []
        str_tempo: list[str] = []
        tuple_tempo: tuple[str, str]
        list_data_check: list[str] = []

        nb_drones: str
        start_hub: tuple [str, str, str, Optional[str]]
        end_hub: tuple [str, str, str, Optional[str]]
        hub: list [tuple [str, str, str, Optional[str]]]
        connection: list [tuple [str, str, str, Optional[str]]]

        # 1/ Verifier si une map est chargee: self.map_text ne doit pas etre None
        # Check if map is charged
        if self.map_text is None:
            return False

        # 2/ Enlever toutes les lignes ou morceau de ligne commencant par # (ce sont des commentaires)
        # Clean map datas
        map_list = self.map_text.split("\n")
        print(f"map_list:\n{map_list}")
        for one_line in map_list:
            str_tempo = one_line.split("#")
            if len(str_tempo[0]) > 1:
                map_list_clean.append(str_tempo[0])
        if len(map_list_clean) < 6:
            return False

        # 3/ Verifier si premiere ligne:
        #    using nb_drones: <donnee>
        # Check first line
        tuple_tempo = map_list_clean[0].split(":")
        if len(tuple_tempo) < 2 or tuple_tempo[0] != "nb_drones":
            return False
        nb_drones = tuple_tempo[1]
        list_data_check.append(tuple_tempo[0])

        # 4/ Pour chaque ligne recuperer dans des variables temporaires:
        #   - nb_drones:  <donnee>                              -> str
        #   - start_hub: <name> <x> <y> [metadata]              -> tuple [str, str, str, Optional[str]]
        #   - end_hub: <name> <x> <y> [metadata]                -> tuple [str, str, str, Optional[str]]
        #   - hub: <name> <x> <y> [metadata]                    -> list [tuple [str, str, str, Optional[str]]]
        #   - connection: <name1>-<name2> [metadata]            -> list [tuple [str, str, str, Optional[str]]]
        for i in range(1, len(map_list_clean)):
            tuple_tempo = map_list_clean[i].split(":")
            if len(tuple_tempo) < 2 or tuple_tempo[1] in list_data_check:
                return False
            elif (
                tuple_tempo[0] == "start_hub"
                and tuple_tempo[0] in list_data_check
            ):
                return False
            elif (
                tuple_tempo[0] == "end_hub"
                and tuple_tempo[0] in list_data_check
            ):
                return False
            elif tuple_tempo[0] == "nb_drones":
                return False
            if tuple_tempo[0] == "start_hub" or tuple_tempo[0] == "end_hub":
                list_data_check.append(tuple_tempo[0])
            


        # 5/ Check des donnees recuperees dans un BaseModel
        # 6/ Check des metadata dans un basemodel dedie

    # class CheckMap(BaseModel):
    #     """Check Every Variables which Define Map"""

    #     # destination: str = Field(min_length=3, max_length=50)
    #     # duration_days: int = Field(ge=1, le=3650)

    #     nb_drones: int
    #     start_hub: tuple[str, int, int, Optional[Colors]]
    #     end_hub: tuple[str, int, int, Optional[Colors]]
    #     zone_list: list[tuple[str, int, int, Optional[str], Optional[Colors]]]

    #     @model_validator(mode="after")
    #     def map_validation_rules(self) -> "CheckMap":
    #         name_list: list[str] = []

    #         # check numer of drones
    #         if not self.nb_drones > 0:
    #             raise ValueError("There are not enough drones")

    #         # check zones
    #         name_list.append(self.start_hub[0])
    #         if self.end_hub[0] in name_list:
    #             raise ValueError(
    #                 f"The name: '{self.end_hub[0]}' is already exist"
    #             )
    #         name_list.append(self.end_hub[0])

    #         return self

    # def parse_map(self) -> bool:
    #     """Check File Content"""
    #     if self.map_text is None:
    #         return False
    #     return True

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
    test_map.parse_map()
    test_map.display_map()

    print()
    test_map2.loading_map()
    print()
    test_map3.loading_map()


if __name__ == "__main__":
    main()
