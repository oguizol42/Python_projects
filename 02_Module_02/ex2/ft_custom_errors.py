class GardenError(Exception):
    """Class Parent Errors"""

    pass


class PlantError(GardenError):
    """Class Child of GardenError"""

    pass


class WaterError(GardenError):
    """Class Child of GardenError"""

    pass


def main():
    """Main de Test"""
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    except PlantError as e:
        print(e)
    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    except WaterError as e:
        print(e)
    print()
    print("Testing catching all garden errors...")
    try:
        raise GardenError()
    except GardenError:
        try:
            raise PlantError(
                "Caught a garden error: The tomato plant is wilting!"
            )
        except PlantError as e:
            print(e)
        try:
            raise WaterError(
                "Caught WaterError: Not enough water in the tank!"
            )
        except WaterError as e:
            print(e)

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
