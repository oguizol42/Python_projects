import math


def parsing(string: str) -> tuple:
    """Transforme une chaine de caractere en tuple"""
    string_lst = string.split(",")
    coord = (int(string_lst[0]), int(string_lst[1]), int(string_lst[2]))
    return coord


def calcul_distance(pos1: tuple, pos2: tuple) -> float:
    """Calcul Distance Between Two Points"""
    x1 = int(pos1[0])
    x2 = int(pos2[0])
    y1 = int(pos1[1])
    y2 = int(pos2[1])
    z1 = int(pos1[2])
    z2 = int(pos2[2])
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return result


def main() -> None:
    """Manage Points On Map"""
    print("=== Game Coordinate System ===")
    print()
    try:
        pos: tuple = (10, 20, 5)
        map_orig: tuple = (0, 0, 0)
    except ValueError as e:
        print(e)
    else:
        print(f"Position created: ({pos[0]}, {pos[1]}, {pos[2]})")
        dist = calcul_distance(pos, map_orig)
        print(
            f"Distance between ({map_orig[0]}, {map_orig[1]}, "
            f"{map_orig[2]}) and ({pos[0]}, {pos[1]}, {pos[2]}): {dist}"
        )
    print()
    try:
        string: str = "3,4,0"
        print(f"Parsing coordinates: {string}")
        test_parsing: tuple = parsing(string)
        print(f"Parsed position: {test_parsing}")
        dist = calcul_distance(map_orig, test_parsing)
        print(f"Distance between {map_orig} and {test_parsing}: {dist}")
        print()
        string: str = "abc,def,ghi"
        print(f"Parsing invalid coordinates: {string}")
        error: tuple = parsing(string)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
        print()
    else:
        print(error)
    print("Unpacking demonstration:")
    X, Y, Z = test_parsing
    print(f"Player at x={X}, y={Y}, z={Z}")
    print(f"Coordinates: X={X}, Y={Y}, Z={Z}")


if __name__ == "__main__":
    main()
