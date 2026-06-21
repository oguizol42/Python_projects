from fly_in import Drone_Map
from parsing import MapParsing
from typing import Optional

class Map:
    def __init__(self, map_parsed: Drone_Map) -> None:
        self.map_parsed: Drone_Map = map_parsed
        self.size_map: tuple[int, int]
        self.current_turn: int = 0
        self.start_hub: Map.Zone
        self.end_hub: Map.Zone
        self.zones_list: dict[str, Map.Zone] = {}
        self.connections_list: list[Map.Connection] = []
        self.drones_list: list[Map.Drone] = []

    class Zone:
        def __init__(self) -> None:
            self.name: str
            self.coord_x: int
            self.coord_y: int
            self.color: Optional[str] = None
            self.priority: str = "normal"
            self.max_drones_allow: int = 1
            self.drones_in_zone: list[Map.Drone] = []
            self.connections: list[Map.Connection] = []

    def calcul_size_map(self, coord_x: int, coord_y: int):
        """Calcul Size of the Map"""
        if coord_x < self.min_x:
                self.min_x = coord_x
        elif coord_x > self.max_x:
            self.max_x = coord_x
        if coord_y < self.min_y:
            self.min_y = coord_y
        elif coord_y > self.max_y:
            self.max_y = coord_y

        self.size_map = (
            self.max_x - self.min_x,
            self.max_y - self.min_y
        )

    def recup_zone(self, zone_parsed) -> "Map.Zone":
        """Recup One Zone from Map Parsed and Calcul Map Size"""
        self.max_x: int = 0
        self.max_y: int = 0
        self.min_x: int = 0
        self.min_y: int = 0

        zone = Map.Zone()
        zone.name = zone_parsed[0].name
        zone.x = zone_parsed[0].coord_x
        zone.y = zone_parsed[0].coord_y
        zone.color = zone_parsed[1].color
        zone.priority = zone_parsed[1].zone_type
        zone.max_drones_allow = zone_parsed[1].max_drones

        self.calcul_size_map(zone.x, zone.y)

        return zone


    def recup_zones_list(self) -> None:
        """Recup Eevry Zones from Map Parsed and Calcul Map Size"""
        for zone_parsed in self.map_parsed.hub_list:
            (self.zones_list)[zone_parsed[0].name] = self.recup_zone(zone_parsed)

        self.start_hub = self.recup_zone(self.map_parsed.start_hub)
        self.end_hub = self.recup_zone(self.map_parsed.end_hub)

    class Connection:
        def __init__(self) -> None:
            self.zone_1: Map.Zone
            self.zone_2: Map.Zone
            self.max_link_capacity: int = 1
            self.drones_in_connection: list[Map.Drone] = []

    class Drone:
        def __init__(self) -> None:
            self.current_zone: Optional[Map.Zone] = None
            self.current_connection: Optional[Map.Connection] = None
            self.destination_zone: Optional[Map.Zone] = None
            self.remaining_turn: int = 0

        def drone_moving(self) -> None:
            """Manage Moving of Drone"""
            # Deplacement des drones
            # Test si deplacement possible 
            # Modification des donnes de chaque zone, connections et drones,
            # en temps reel, au fil des tours
            # Comptage des tours
            # Affichage en temps reel
            pass

        def check_moving(self, dest: "Map.Zone") -> bool:
            """Check if Drone Moving is Allowed"""
            return True

    def print_map(self) -> None:
        """Displaying Graphic Map"""
        pass


# Recupere la map parsée

# class Map
    # Taille de la map
    
    # Nombre de tours deja effectue

    # Initialise pour chaque zone (class Zone)
        # Emplacement (coordonnees x, y)
        # Couleur
        # Regle de priorité (normal, blocked, restricted, priority)
        # Nombre de drones autorises en simultanés
        # Liste des drones present
        # Liste des connections

    # Class Connection
        # zone 1
        # zone 2
        # liste des drones presents
        # nombre de drones autorises

# ◦ normal – Standard zone with 1 turn movement cost (default)
# ◦ blocked – Inaccessible zone. Drones must not enter or pass through this zone.
# Any path using it is invalid.
# ◦ restricted – A sensitive or dangerous zone. Movement to this zone costs 2
# turns.
# ◦ priority – A preferred zone. Movement to this zone costs 1 turn but should
# be prioritized in pathfinding.

    # class Drone
        # zone courente ou None 
        # connection courente ou None 
            # Si connection:
                # zone de destination
                # Decomptage des tours de transit 
        # (cas ou drone dans une connection vers zone restreinte
        # doit etre egale a zero pour que le drone puisse entrer dans la zone)

    # def drone_moving
        # Deplacement des drones
        # Test si deplacement possible 
        # Modification des donnes de chaque zone, connections et drones,
        # en temps reel, au fil des tours
        # Comptage des tours
        # Affichage en temps reel

    # Affichage