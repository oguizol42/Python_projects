from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum

# PARSING


class MapParsing:
    """Parsing Map Datas"""

    def __init__(self, map_text: str = None) -> None:
        self.map_text = map_text

    class Colors(str, Enum):
        green = "green"
        yellow = "yellow"
        red = "red"
        gray = "gray"

    class DatasType(str, Enum):
        nb_drones = "nb_drones"
        start_hub = "start_hub"
        end_hub = "end_hub"
        hub = "hub"
        connection = "connection"

    def check_hub(self, hub_str: str) -> bool:
        """Checking Hub elements"""
        return True

    def check_connection(self, connection_str: str) -> bool:
        """Checking Hub elements"""
        return True

    def map_parsing(self) -> bool:
        """Check File Content"""
        map_list_tuple: list = []
        meta_tuple_str: tuple[str, Optional[str], Optional[str]] = []

        map_list: list[str] = []
        map_list_clean: list[str] = []
        tuple_tempo: tuple[str, str]
        tuple_tempo_datas: tuple[str, str]
        list_data_check: list[str] = []

        nb_drones_str: str
        hub_str: tuple[
            str,
            str,
            str,
            Optional[tuple[str, Optional[str], Optional[str], Optional[str]]],
        ]
        start_hub_str: tuple[str, str, str, Optional[str]]
        end_hub_str: tuple[str, str, str, Optional[str]]
        hub_list_str: list[tuple[str, str, str, Optional[str]]]
        connection_str: list[tuple[str, str, str, Optional[str]]]

        # Clean map datas
        map_list = self.map_text.split("\n")
        for one_line in map_list:
            tuple_tempo = one_line.split("#")
            if len(tuple_tempo[0]) > 1:
                map_list_clean.append(tuple_tempo[0])
        if len(map_list_clean) < 6:
            return False

        for i in range(len(map_list_clean)):
            tuple_tempo_datas = map_list_clean[i].split(":")

            if not len(tuple_tempo_datas) == 2:
                return False
            elif i == 0 and not tuple_tempo_datas[0] == "nb_drones":
                return False
            elif i > 0 and tuple_tempo_datas[0] == "nb_drones":
                return False
            # elif tuple_tempo_datas[0] not in self.DatasType:
            #     return False

            # Recup meta
            tuple_tempo_datas = map_list_clean[i].split("]")
            if len(tuple_tempo_datas) == 2:
                tuple_tempo_datas = tuple_tempo_datas[0].split("[")
                meta_tuple = tuple_tempo_datas[1].split(" ")

            tuple_tempo_datas = tuple_tempo_datas[0].split(" ")

            # Recup number of drones
            if i == 0:
                nb_drones_str = tuple_tempo_datas[1]
                continue

            # Recup type
            if tuple_tempo_datas[0] == "connection:":
                if self.check_connection(tuple_tempo_datas[1]) is False:
                    return False
            elif (
                tuple_tempo_datas[0] == "start_hub:"
                or tuple_tempo_datas[0] == "end_hub:"
                or tuple_tempo_datas[0] == "hub:"
            ):
                if self.check_hub(tuple_tempo_datas[1]) is False:
                    return False
            else:
                return False

            print(f"type: {tuple_tempo_datas[0]}")

        # TEST
        print(f"\nmap_list: \n{map_list}")
        print(f"\nmap_list_clean: \n{map_list_clean}")
        print(f"\nnb_drones_str: {nb_drones_str}")

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
