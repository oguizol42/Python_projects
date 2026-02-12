class Plant:
    """Plant Informations"""

    def __init__(self, name: str, height: int, age: int):
        """def plant informations"""
        self.name = str(name)
        self.height = int(height)
        self.age_plant = int(age)

    def age(self, day: int) -> None:
        self.age_plant += int(day) - 1

    def grow(self, day: int) -> None:
        if day > 1:
            self.height += int(day) - 1

    def get_info(self, day: int) -> None:
        """Print Current Plant Status"""
        print("=== Day", int(day), "===")
        name = str(self.name) + ":"
        height = str(self.height) + "cm,"
        age = str(self.age_plant) + " days old"
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
    """ft_plant_growth.py"""
    p = init_three_plants()
    for i in range(len(p)):
        p[i].get_info(1)
        p[i].grow(7)
        p[i].age(7)
        p[i].get_info(7)


if __name__ == "__main__":
    main()
