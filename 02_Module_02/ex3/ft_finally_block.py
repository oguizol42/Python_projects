class WaterError(Exception):
    """Class Error of Watering"""

    pass


def water_plants(plants_list: list) -> None:
    """Watering Plants"""
    print("Opening watering system")
    check = True
    try:
        for plant in plants_list:
            if plant is None:
                raise WaterError("Error: Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")

    except WaterError as e:
        print(e)
        check = False
    finally:
        print("Closing watering system (cleanup)")
        if check is True:
            print("Watering completed successfully!")
        else:
            print()
            print("Cleanup always happens, even with errors!")


def test_watering_system() -> None:
    """Tests Behavior with Good and Bad Plants"""
    plants = create_good_plant_list()
    print()
    print("Testing normal watering...")
    water_plants(plants)
    print()
    print("Testing with error...")
    plants = create_bad_plant_list()
    water_plants(plants)


def create_bad_plant_list() -> list:
    """Create a List of Plants"""
    plants = ["tomato", None, "lettuce", "carrots"]
    return plants


def create_good_plant_list() -> list:
    """Create a List of Plants"""
    plants = ["tomato", "lettuce", "carrots"]
    return plants


def main():

    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()
