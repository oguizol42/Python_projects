class Plant:
    """Plant Informations"""

    def __init__(self, name: str, height: int, age: int):
        """def plant informations"""
        self.name = str(name)
        self.height = int(height)
        self.age = int(age)

    def display_plant_info(self) -> None:
        """Display Plant Informations"""
        name = str(self.name) + ":"
        height = str(self.height) + "cm,"
        age = str(self.age) + " days old"
        print(name, height, age)


def init_three_plants() -> list[Plant]:
    """Initialising three plants objects"""
    p = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    return p


def main() -> None:
    """=== Garden Plant Registry ==="""
    p = init_three_plants()
    print("=== Garden Plant Registry ===")
    for i in range(len(p)):
        p[i].display_plant_info()


if __name__ == "__main__":
    main()
