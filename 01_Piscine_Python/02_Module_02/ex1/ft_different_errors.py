def garden_operations() -> None:
    """Generates Errors"""
    try:
        # Value Error
        int("abc")
    except ValueError:
        pass
    try:
        # ZeroDivisionError
        15 / 0
    except ZeroDivisionError:
        pass
    try:
        # FileNotFoundError
        open("this_file_does_not_exist.txt", "r")
    except FileNotFoundError:
        pass
    try:
        # KeyError
        my_dict = {"a": 1, "b": 2}
        print(my_dict["z"])
    except KeyError:
        pass


def test_error_types() -> None:
    """Handle Errors"""
    print("=== Garden Error Types Demo ===")

    print()
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print("Caught ValueError: ", e)

    print()
    print("Testing ZeroDivisionError...")
    try:
        15 / 0
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError: ", e)

    print()
    print("Testing FileNotFoundError...")
    try:
        open("this_file_does_not_exist.txt", "r")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: ", e)

    print()
    print("Testing KeyError...")
    try:
        my_dict = {"a": 1, "b": 2}
        print(my_dict["z"])
    except KeyError as e:
        print("Caught KeyError: ", e)

    print()
    print("Testing multiple errors together...")
    try:
        int("abc")
        15 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
