class Plant:
    """Plant Informations"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """def plant informations"""
        self.name = name
        self.height = height
        self.age_plant = age

    def age(self, day: int) -> None:
        if day > 0:
            self.age_plant += int(day)
            self.grow(day)

    def grow(self, day: int) -> None:
        if day > 0:
            self.height += int(day)

    def get_info(self) -> None:
        """Print Current Plant Status"""
        print(f"{self.name}: {self.height}cm, {self.age_plant} days old")


def init_three_plants() -> list[Plant]:
    """Initialising three plants objects"""
    plants_list = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]
    return plants_list


def main() -> None:
    """ft_plant_growth.py"""
    plants_list = init_three_plants()
    grow_list = []
    print("=== Day 1 ===")
    for i in range(len(plants_list)):
        plants_list[i].get_info()
        grow_list.append(plants_list[i].height)
    print("=== Day 7 ===")
    for i in range(len(plants_list)):
        plants_list[i].age(6)
        plants_list[i].get_info()
        grow_list[i] = plants_list[i].height - grow_list[i]
        print(f"Growth this week: +{grow_list[i]}cm")


if __name__ == "__main__":
    main()
