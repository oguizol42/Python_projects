import alchemy
import alchemy.elements


def main() -> None:
    """Scared Scroll"""
    print("=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): ", end="")
    print(alchemy.elements.create_fire())
    print("alchemy.elements.create_water(): ", end="")
    print(alchemy.elements.create_water())
    print("alchemy.elements.create_earth(): ", end="")
    print(alchemy.elements.create_earth())
    print("alchemy.elements.create_air(): ", end="")
    print(alchemy.elements.create_air())
    print()
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): ", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.elements.create_water(): ", end="")
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")
    print()
    print("Package metadata:")
    print("Version: 1.0.0")
    print("Author: Master Pythonicus")


if __name__ == "__main__":
    main()
