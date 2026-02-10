def display_garden(name: str, height: int, age: int) -> None:
    """ Displaying garden plants informations """
    print("=== Welcome to My Garden ===")
    print("Name:", str(name))
    print("Height:", str(height))
    print("Age:", int(age), "days")
    print()
    print("=== End of Program ===")

def main() -> None:
    """=== Welcome to My Garden ==="""
    name = "Rose"
    height = "25cm"
    age = 30
    display_garden(name, height, age)
if __name__ == '__main__':
    main()