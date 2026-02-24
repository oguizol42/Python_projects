import math
import sys


def main():
    """Calcul Distances Between 3D Points"""
    try:
        print("=== Game Coordinate System ===")
        print()
        pos_base: tuple = int(0, 0, 0)
        # position: tuple = int(10, "bob", 5)
        print("Position created:", position)
        print("Distance between:", pos_base, "and", position, ":")
        # pos_player: tuple = (3, 4, 0)
    except ValueError:
        print()
        print('Parsing invalid coordinates: "abc,def,ghi"')
        print(
            "Error parsing coordinates: "
            "invalid literal for int() with base 10: 'abc'"
        )
        # print('Error details - Type: ValueError, Args: '
        #       '("invalid literal for int() with base 10: 'abc'",)'
        # )
    finally:
        print()
        print("Unpacking demonstration:")
        # print(f"Player at x=", {pos_player[0]}, " y=", {pos_player[1]}, " z=", {pos_player[2]}")
        # print("Coordinates: X=3, Y=4, Z=0")


if __name__ == "__main__":
    main()

# $> python3 ft_coordinate_system.py

# === Game Coordinate System ===

# Position created: (10, 20, 5)
# Distance between (0, 0, 0) and (10, 20, 5): 22.91

# Parsing coordinates: "3,4,0"
# Parsed position: (3, 4, 0)
# Distance between (0, 0, 0) and (3, 4, 0): 5.0

# Parsing invalid coordinates: "abc,def,ghi"
# Error parsing coordinates: invalid literal for int() with base 10: 'abc'
# Error details - Type: ValueError, Args: ("invalid literal for int() with base 10: 'abc'",)

# Unpacking demonstration:
# Player at x=3, y=4, z=0
# Coordinates: X=3, Y=4, Z=0
