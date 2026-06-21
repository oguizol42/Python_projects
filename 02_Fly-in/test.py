from fly_in import Drone_Map, Drones_Fly, Manage_flies
from graph import Map
from pydantic import ValidationError


def parsing_tests() -> None:
    """Test Functions Parsing"""
    pass


def displaying_map_settup_test(test_map_parsed: Drone_Map) -> None:
    """Test Displayong Map"""
    if test_map_parsed.map_text is None:
        print("No Map Loaded")
    else:
        print(test_map_parsed.map_text)
    if test_map_parsed.map_clean is None or test_map_parsed.map_clean == []:
        print("Map is not Cleaned")
    try:
        test_map_parsed.clean_map()
    except ValueError as e:
        print(e)
    if test_map_parsed.map_clean is not None and test_map_parsed.map_clean != []:
        print(test_map_parsed.map_clean)

    print("\n\nFinal Map Parsed:\n")
    print(f"Start hub: {test_map_parsed.start_hub}\n")
    print(f"Hubs list:\n{test_map_parsed.hub_list}\n")
    print(f"End hub: {test_map_parsed.end_hub}\n")
    print(f"Connections list:\n{test_map_parsed.connection_list}\n")

def displaying_map_setted(test_graph_map: Map) -> None:
    print("\nListe des zones traitees:")
    print("Start hub:")
    print(
            f"Nom: {test_graph_map.start_hub.name}, coord: [{test_graph_map.start_hub.x}, {test_graph_map.start_hub.y}] "
            f"Couleur: {test_graph_map.start_hub.color}, Priorite: {test_graph_map.start_hub.priority} "
            f"Max drones autorises: {test_graph_map.start_hub.max_drones_allow}"
            )

    print("\nHub list:")
    for clef, zone in test_graph_map.zones_list.items():
        print(
            f"Nom: {clef}, coord: [{zone.x}, {zone.y}] "
            f"Couleur: {zone.color}, Priorite: {zone.priority} "
            f"Max drones autorises: {zone.max_drones_allow}"
            )

    print("\nEnd hub::")
    print(
            f"Nom: {test_graph_map.end_hub.name}, coord: [{test_graph_map.end_hub.x}, {test_graph_map.end_hub.y}] "
            f"Couleur: {test_graph_map.end_hub.color}, Priorite: {test_graph_map.end_hub.priority} "
            f"Max drones autorises: {test_graph_map.end_hub.max_drones_allow}"
            )
    print(f"\nTaille de la map: {test_graph_map.size_map}")


def loading_test(test_file: Drone_Map) -> None:
    """Test Loading of Map File"""
    try:
        test_file.loading_map()
    except FileNotFoundError as e:
        print(e)
    except IsADirectoryError as e:
        print(e)


def main() -> None:
    """Test every functions"""
    test_map: Drone_Map = Drone_Map("maps_test/02_linear_path.txt")
    test_graph_map: Map = Map(test_map)

    test_map2: Drone_Map = Drone_Map("maps/easy/01_linear_path2")
    test_map3: Drone_Map = Drone_Map("maps/easy")

    print("TESTING WITHOUT FILE LOADED:")
    # displaying_map_settup_test(test_map)

    print("\nTESTING WITH GOOD MAP LOADED:")
    loading_test(test_map)
    try:
        test_map.map_parsing()
        # test_map.display_map()
        test_graph_map.recup_zones_list()
        displaying_map_settup_test(test_map)
        displaying_map_setted(test_graph_map)
    except ValueError as e:
        print(f"line {test_map.num_line_error}: {e}")
    except ValidationError as e:
        print(f"line {test_map.num_line_error}: {e}")
    print()

    print("\nTESTING BY LOADED A FILE THAT NOT EXIST:")
    loading_test(test_map2)

    print("\nTESTING BY LOADED A REPERTORY:")
    loading_test(test_map3)


if __name__ == "__main__":
    main()
