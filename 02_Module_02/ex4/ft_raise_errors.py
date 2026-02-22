def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int) -> None:
    """Check if Plant is Valid"""
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif not 1 <= water_level <= 10:
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
        else:
            raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    elif not 2 <= sunlight_hours <= 12:
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Test Several Errors Situations"""
    print("=== Garden Plant Health Checker ===")
    try:
        print()
        print("Testing good values...")
        check_plant_health("tomato", 1, 2)
    except ValueError as e:
        print(e)
    try:
        print()
        print("Testing empty plant name...")
        check_plant_health(None, 1, 2)
    except ValueError as e:
        print(e)
    try:
        print()
        print("Testing bad water level...")
        check_plant_health("tomato", 15, 2)
    except ValueError as e:
        print(e)
    try:
        print()
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 1, 0)
    except ValueError as e:
        print(e)
    print()
    print("All error raising tests completed!")

if __name__ == '__main__':
    test_plant_checks()