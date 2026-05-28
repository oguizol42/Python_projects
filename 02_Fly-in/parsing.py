from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum

# PARSING

# Fichier Exemple:

# nb_drones: 5

# start_hub: hub 0 0 [color=green]
# end_hub: goal 10 10 [color=yellow]
# hub: roof1 3 4 [zone=restricted color=red]
# hub: roof2 6 2 [zone=normal color=blue]
# hub: corridorA 4 3 [zone=priority color=green max_drones=2]
# hub: tunnelB 7 4 [zone=normal color=red]
# hub: obstacleX 5 5 [zone=blocked color=gray]
# connection: hub-roof1
# connection: hub-corridorA
# connection: roof1-roof2
# connection: roof2-goal
# connection: corridorA-tunnelB [max_link_capacity=2]
# connection: tunnelB-goal


# • The first line defines the number of drones using nb_drones: <number>.
# • Zone definition on each line using type prefixes:
# ◦ start_hub: <name> <x> <y> [metadata] marks the starting zone.
# ◦ end_hub: <name> <x> <y> [metadata] marks the end zone.
# ◦ hub: <name> <x> <y> [metadata] defines a regular zone.
# ◦ The connection syntax forbids dashes in zone names (see below).
# • All metadata is optional and enclosed in brackets [...] with default values:
# ◦ zone=<type> (default: normal)
# ◦ color=<value> (default: none)
# ◦ max_drones=<number> (default: 1) - Maximum drones that can occupy this
# zone simultaneously
# ◦ Tags inside brackets can appear in any order.
# • Zone types:
# 9
# Fly-in Drones are interesting.
# ◦ normal – Standard zone with 1 turn movement cost (default)
# ◦ blocked – Inaccessible zone. Drones must not enter or pass through this zone.
# Any path using it is invalid.
# ◦ restricted – A sensitive or dangerous zone. Movement to this zone costs 2
# turns.
# ◦ priority – A preferred zone. Movement to this zone costs 1 turn but should
# be prioritized in pathfinding.
# • Colors:
# ◦ Colors are optional and can be used for visual representation (terminal output
# or graphical display).
# ◦ Accepted values for color are any valid single-word strings (e.g., red, blue,
# gray). There is no fixed list of allowed colors.
# ◦ When colors are specified, the implementation should provide visual feedback
# through colored terminal output or graphical representation.
# • Connections are defined using connection: <name1>-<name2> [metadata]:
# ◦ Define a bidirectional connection (edge) between two zones.
# ◦ The connection syntax forbids dashes in zone names.
# ◦ Optional metadata can be specified in brackets [...]:
# ∗ max_link_capacity=<number> (default: 1) - Maximum drones that can
# traverse this connection simultaneously
# • Comments start with ’#’ and are ignored.


# The input file must respect the expected structure and syntax:
# • The first line must define the number of drones using nb_drones: <positive_integer>.
# • The program must be able to handle any number of drones.
# • There must be exactly one start_hub: zone and one end_hub: zone.
# • Each zone must have a unique name and valid integer coordinates.
# • Zone names can use any valid characters except dashes and spaces.
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
# indicating the line and cause.


class MapParsing:
    def __init__(self) -> None:
        self.map_clean: list[str] = []
        self.types_used: list[str] = []
        self.name_used: list[str] = []
        self.coord_list: list[tuple[int, int]] = []
        self.hub_list: list[tuple[MapParsing.HubData, MapParsing.HubMeta]]
        self.connection_list: list[
            tuple[MapParsing.ConnectionData, MapParsing.ConnectionMeta]
        ]

    # Recupere map_str sans les commentaires dans self.map_clean
    #           => def clean_map(self, map_str) -> str:
    def clean_map(self) -> None:
        """Clean Map Datas"""
        if self.map_text is None or self.map_text == []:
            raise ValueError("No datas read")
        map_list: list[str] = self.map_text.split("\n")
        for one_line in map_list:
            tuple_tempo = one_line.split("#")
            if len(tuple_tempo[0]) > 1:
                self.map_clean.append(tuple_tempo[0])
        if len(self.map_clean) < 6:
            self.map_clean = []
            raise ValueError("Not enough values in the map definition")

    class DatasType(str, Enum):
        nb_drones = "nb_drones"
        start_hub = "start_hub"
        end_hub = "end_hub"
        hub = "hub"
        connection = "connection"

    class HubMeta(BaseModel):
        pass

    class HubData(BaseModel):
        pass

    class ConnectionMeta(BaseModel):
        pass

    class ConnectionData(BaseModel):
        pass

    def check_type(self, line: str) -> str:
        """Check and Return type or a raise"""
        if line is None:
            raise ValueError("There is no line in argument")
        type_tuple: tuple[str , str] = line.split(":")
        if len(type_tuple) != 2:
            raise ValueError("There is no type argument identifiable")
        if type_tuple[0] not in [c.value for c in MapParsing.DatasType]:
            raise ValueError(f"'{type_tuple[0]}' is not correct type")
        if type_tuple[0] in self.types_used:
            raise ValueError(f"'{type_tuple[0]}' is used several times")

        if type_tuple[0] == "nb_drones" or type_tuple[0] == "start_hub" or type_tuple[0] == "end_hub":
            self.types_used.append(type_tuple[0])

        return type_tuple[0]

    def map_parsing(self) -> None:
        """Parsing of All the Map"""
        tuple_tempo: tuple
        type: str = None
        nb_drones_str: str



        try:
            self.clean_map()
            for i in range(len(self.map_clean)):
                type = self.check_type(self.map_clean[i])

                # TEMPO
                print(f"{i}: {type}")

                if i == 0:
                    # CHeck first line
                    if not type == "nb_drones":
                        raise ValueError(f"The first type is '{type}' but it should have been 'nb_drones'")
                    tuple_tempo = self.map_clean[i].split(" ")
                    if not len(tuple_tempo) == 2:
                        raise ValueError(f"Definition of {type} is not valid")
                    nb_drones_str = tuple_tempo[1]

                    # TEMPO
                    print(f"\nIl y a {nb_drones_str} drone(s)\n")

                    continue
                    

            # check first line


        except ValueError as e:
            print(e)


# Recupere map_str sans les commentaires dans self.map_clean
#           => def clean_map(self, map_str) -> str:




# map_parsing(self)
# Checker chaque ligne:
#   - premiere ligne: nb_drones: <number>

# Puis pour chaque ligne:
#   - def check_type(self, str) -> str
#       * Verifie si le type est correct
#               => sinon raise
#       * Si nb_drones ou start_hub deja utilise ou end_hub deja utilise
#               => raise
#       * type: str = def check_type(self, ligne)

#   Si type pas connection
#        => def check_name(self, str)
#           * si nom deja utilise (present dans self.name_list)
#                   => raise
#           * si nom contient tiret ou espaces
#                   => raise
#           * ajout du nom dans self.name_list
#        => def check_meta_hub(self, str) -> str
#           * si meta pas coeherente
#                   => raise
#        => def check_hub(self, str)
#           * Si coordonnees ne sont pas des int positifs
#               => sinon raise
#           * Si coordonnees deja utilisees
#               => raise
#           * Ajout des coordonnees dans self.coord_list
#           * Ajout du hub dans self.hub_list


#   Sinon
#       => def check_datas_connection(self)

# start_hub: <name> <x> <y> [metadata]
# end_hub: <name> <x> <y> [metadata]
# hub: <name> <x> <y> [metadata]
#       * [metadata] -> zone=<type> (default: normal)
#           * normal – Standard zone with 1 turn movement cost (default)
#           * blocked – Inaccessible zone. Drones must not enter or pass through this zone.
#                       Any path using it is invalid.
#           * restricted – A sensitive or dangerous zone. Movement to this zone costs 2
#                       turns.
#           * priority – A preferred zone. Movement to this zone costs 1 turn but should
# be prioritized in pathfinding.
#       * [metadata] -> color=<value> (default: none)
#       * [metadata] -> max_drones=<number> (default: 1)
#   - def check_hub(self, str)

# connection: <point A>-<point B> [metadata] -> syntax forbids dashes in zone names
#       * [metadata] -> max_link_capacity=<number> (default: 1)
#   - def normalise_connection(self) -> str,str => retourne une string contenant les donnees separeees d'un espace
#                                               + une string contenant les metadonnees
#                                              Fait un raise si probleme
#   -def check_meta_connection(self, str) -> str
#       * si meta pas coeherente
#           => raise
#   -def check_datas_connection(self) -> None => execute def normalise_connection()
#                                             def check_meta_connection()
#                                             analyse si connections correspondent a des zones existantes
#                                             verifie si cette connection a deja ete creee avant (self.list_connections)
#                                                   => raise si c'est le cas
#                                                   => sinon ajout de cette connection et sa reciproque a self.list_connections
#                                                      ajout des connections avec leur meta a chaque zones correspondantes

# FAIRE DES CLASSES DEFINISSANT LES METAS
