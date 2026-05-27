from fly_in import Drone_Map, Drones_Fly, Manage_flies


def parsing_tests() -> None:
    """Test Functions Parsing"""
    pass


def main() -> None:
    """Test every functions"""
    test_map: Drone_Map = Drone_Map("maps/easy/01_linear_path.txt")
    test_map2: Drone_Map = Drone_Map("maps/easy/01_linear_path2")
    test_map3: Drone_Map = Drone_Map("maps/easy")

    print("TESTING WITHOUT FILE LOADED:")
    test_map.display_map()

    print("\nTESTING WITH GOOD MAP LOADED:")
    test_map.loading_map()
    test_map.map_parsing()
    test_map.display_map()

    print("\nTESTING BY LOADED A FILE THAT NOT EXIST:")
    test_map2.loading_map()

    print("\nTESTING BY LOADED A REPERTORY:")
    test_map3.loading_map()


if __name__ == "__main__":
    main()
