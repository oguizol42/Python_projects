class WaterError(Exception):
    """Class Error of Watering"""

    pass


def water_plants(plant_list: list) -> None:
    """Watering Plants"""
    print("Opening watering system")
    check = True
    try:
        for i in range(len(plant_list)):
            print(f"Watering {plant_list[i]}")
            i += 1
            if plant_list[i] == "invalid":
                i = len(plant_list)
                print("Error: Cannot water None - invalid plant!")
                raise WaterError()

    except WaterError:
        check = False
        pass
    finally:
        print("Closing watering system (cleanup)")
        if check == "True":
            print("Watering completed successfully!")
        else:
            print("Cleanup always happens, even with errors!")


def test_watering_system() -> None:
    """Tests Behavior with Good and Bad Plants"""
    plants = creat_good_plant_list()
    print()
    print("Testing normal watering...")
    water_plants(plants)
    print()
    print("Testing with error...")
    plants = creat_bad_plant_list()
    water_plants(plants)


def creat_bad_plant_list() -> list:
    """Create a List of Plants"""
    plants = ["tomato", "invalid", "lettuce", "invalid", "carrots", "invalid"]
    return plants


def creat_good_plant_list() -> list:
    """Create a List of Plants"""
    plants = ["tomato", "True", "lettuce", "True", "carrots", "True"]
    return plants


def main():

    print("=== Garden Watering System ===")
    test_watering_system()


if __name__ == "__main__":
    main()

# === Garden Watering System ===
# Testing normal watering...
# Opening watering system
# Watering tomato
# Watering lettuce
# Watering carrots
# Closing watering system (cleanup)
# Watering completed successfully!
# Testing with error...
# Opening watering system
# Watering tomato
# Error: Cannot water None - invalid plant!
# Closing watering system (cleanup)
# Cleanup always happens, even with errors!
