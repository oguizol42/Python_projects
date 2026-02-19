def check_temperature(temp_str: str) -> int | None:
    """Check Temperature Entry"""
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")
        print()
        return None
    try:
        if temp < 0:
            raise ValueError(
                f"Error: {temp_str}°C is too cold for plants (min 0°C)"
            )
        elif temp > 40:
            raise ValueError(
                f"Error: {temp_str}°C is too hot for plants (max 40°C)"
            )
    except ValueError as e:
        print(e)
        print()
        return None

    print(f"Temperature {temp}°C is perfect for plants!")
    print()
    return temp


def test_temperature_input() -> None:
    """Test Function check_temperature()"""
    print("=== Garden Temperature Checker ===")
    print()
    print("Testing temperature: 25")
    check_temperature("25")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("Testing temperature: 100")
    check_temperature("100")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
