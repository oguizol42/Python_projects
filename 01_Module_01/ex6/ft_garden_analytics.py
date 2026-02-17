class GardenManager:
    """Manage Some Gardens"""

    list_garden = []

    class Garden:
        """Garden Definition"""

        def __init__(self, name: str):
            self.name = name
            self.reg_plant_list = []
            self.flow_plant_list = []
            self.prize_plant_list = []
            self.growth: int = 0
            self.score: int = 0

    class Plant:
        """Plant Definition"""

        def __init__(self, name: str, height):
            self.name = str(name)
            self.height = int(height)

    class FloweringPlant(Plant):
        """FloweringPlant Definition"""

        def __init__(self, name: str, height: int, bloom: str):
            super().__init__(name, height)
            self.bloom = str(bloom)

    class PrizeFlower(FloweringPlant):
        """PrizeFlower Definition"""

        def __init__(self, name: str, height: int, bloom: str, points: int):
            super().__init__(name, height, bloom)
            self.points = int(points)

    class GardenStats:
        """Statistics Calculator"""
        def qty_plants(
            garden: "GardenManager.Garden",
        ) -> tuple[(int, int, int, int)]:
            """Plants Counter"""
            qty_reg, qty_flow, qty_priz, total = (
                GardenManager.sum_three_size_list(
                    garden.reg_plant_list,
                    garden.flow_plant_list,
                    garden.prize_plant_list,
                )
            )
            return (qty_reg, qty_flow, qty_priz, total)

        qty_plants = staticmethod(qty_plants)

        def plant_growth_total(garden: "GardenManager.Garden") -> int:
            """Plant Growth Total in cm"""
            _, _, _, growth = GardenManager.GardenStats.qty_plants(garden)
            return growth

        plant_growth_total = staticmethod(plant_growth_total)

        def gardens_scores(gardens: list) -> None:
            """Calculate Scores Gardens"""
            for j in range(len(gardens)):
                bonus = 0
                score = 0
                for i in range(len(gardens[j].reg_plant_list)):
                    score += gardens[j].reg_plant_list[i].height
                for i in range(len(gardens[j].flow_plant_list)):
                    score += gardens[j].flow_plant_list[i].height
                for i in range(len(gardens[j].prize_plant_list)):
                    score += gardens[j].prize_plant_list[i].height
                for i in range(len(gardens[j].prize_plant_list)):
                    bonus += gardens[j].prize_plant_list[i].points
                score += bonus * gardens[j].growth
                gardens[j].score = score

        gardens_scores = staticmethod(gardens_scores)

    def create_garden_network(cls, name, plants=None) -> None:
        """Add Garden and Plants"""
        new_garden = cls.find_garden(cls.list_garden, name)
        if new_garden is None:
            new_garden = cls.Garden(name)
            cls.list_garden.append(new_garden)
        if plants is not None:
            GardenManager.add_plant(new_garden, plants)

    create_garden_network = classmethod(create_garden_network)

    def find_garden(list_garden, name_newG) -> Garden:
        """Find Garden in List"""
        if len(list_garden) > 0:
            for i in range(len(list_garden)):
                if list_garden[i].name == name_newG:
                    return list_garden[i]
        return None

    def add_plant(garden: Garden, plants) -> None:
        """Put Plants in a Garden"""
        plants = GardenManager.obj_to_list(plants)
        for i in range(len(plants)):
            if isinstance(plants[i], GardenManager.PrizeFlower):
                garden.prize_plant_list.append(plants[i])
            elif isinstance(plants[i], GardenManager.FloweringPlant):
                garden.flow_plant_list.append(plants[i])
            elif isinstance(plants[i], GardenManager.Plant):
                garden.reg_plant_list.append(plants[i])
            print(f"Added {plants[i].name} to {garden.name}'s garden")

    def disp_plants_list(garden: Garden):
        """Print List of Plants"""
        for i in range(len(garden.reg_plant_list)):
            print(
                f"- {garden.reg_plant_list[i].name}: "
                f"{garden.reg_plant_list[i].height}cm"
            )
        for j in range(len(garden.flow_plant_list)):
            print(
                f"- {garden.flow_plant_list[j].name}: "
                f"{garden.flow_plant_list[j].height}cm"
                f", {garden.flow_plant_list[j].bloom} (blooming)"
            )
        for k in range(len(garden.prize_plant_list)):
            print(
                f"- {garden.prize_plant_list[k].name}: "
                f"{garden.prize_plant_list[k].height}cm"
                f", {garden.prize_plant_list[k].bloom} (blooming)"
                f", Prize points: {garden.prize_plant_list[k].points}"
            )

    disp_plants_list = staticmethod(disp_plants_list)

    def garden_report(garden: Garden) -> None:
        """Print Garden Caraceteristics"""
        print(f"=== {garden.name}'s Garden Report ===")
        qty_reg, qty_flow, qty_priz, total = (
            GardenManager.GardenStats.qty_plants(garden)
        )
        if total > 0:
            print("Plants in garden: ")
            GardenManager.disp_plants_list(garden)
        else:
            print("Plants in garden: None")
        print(f"Plants added: {total}, Total growth: {garden.growth}cm")
        print(
            f"Plant types: {qty_reg} regular,"
            f" {qty_flow} flowering,"
            f" {qty_priz} prize flowers"
        )
        print("Height validation test: True")
        GardenManager.GardenStats.gardens_scores(GardenManager.list_garden)
        print(f"Garden scores - {GardenManager.list_garden[0].name}: "
            f"{GardenManager.list_garden[0].score}", end ="")
        for i in range(1, len(GardenManager.list_garden)):
            print(f", {GardenManager.list_garden[i].name}: "
                f"{GardenManager.list_garden[i].score}", end ="")
        print()
        print(f"Total gardens managed: {len(GardenManager.list_garden)}")

    garden_report = staticmethod(garden_report)

    def increase_watering_garden(garden: "GardenManager.Garden"):
        """Counting Watering Garden"""
        print(f"{garden.name} is helping all plants grow...")
        garden.growth = GardenManager.GardenStats.plant_growth_total(garden)

    increase_watering_garden = staticmethod(increase_watering_garden)

    def obj_to_list(obj) -> list:
        """Return a List from an Object"""
        new_list = []
        if isinstance(obj, list):
            new_list = obj
        else:
            new_list.append(obj)
        return new_list

    obj_to_list = staticmethod(obj_to_list)

    def sum_three_size_list(
        obj1: list, obj2: list, obj3: list
    ) -> tuple[(int, int, int, int)]:
        """Return size of three list and total"""
        size1 = len(obj1)
        size2 = len(obj2)
        size3 = len(obj3)
        total = size1 + size2 + size3
        return size1, size2, size3, total

    sum_three_size_list = staticmethod(sum_three_size_list)


def main() -> None:
    """Test Function"""
    oak1 = GardenManager.Plant("Oak1 Tree", 101)
    oak2 = GardenManager.Plant("Oak2 Tree", 153)
    # oak3 = GardenManager.Plant("Oak3 Tree", 208)

    rose1 = GardenManager.FloweringPlant("Rose1", 26, "red flowers")
    # rose2 = GardenManager.FloweringPlant("Rose2", 32, "white flowers")
    rose3 = GardenManager.FloweringPlant("Rose3", 92, "green flowers")

    sunflower1 = GardenManager.PrizeFlower(
        "Sunflower1", 51, "yellow flowers", 10
    )
    # sunflower2 = GardenManager.PrizeFlower(
    #    "Sunflower1", 63, "blue flowers", 14
    # )
    # sunflower3 = GardenManager.PrizeFlower(
    #    "Sunflower1", 73, "orange flowers", 22
    # )

    print("=== Garden Management System Demo ===")
    # GardenManager.create_garden_network("toto")
    # GardenManager.create_garden_network("mimi")
    # GardenManager.create_garden_network("tomi")
    # GardenManager.create_garden_network("mito")
    # GardenManager.create_garden_network("toto")
    # GardenManager.create_garden_network("totomimi")
    # GardenManager.create_garden_network("toto et mimi")
    GardenManager.create_garden_network("Alice")
    GardenManager.create_garden_network("Alice", oak1)
    GardenManager.create_garden_network("Bob", rose3)
    GardenManager.create_garden_network("Alice")
    GardenManager.create_garden_network("Alice", rose1)
    GardenManager.create_garden_network("Alice", sunflower1)
    GardenManager.increase_watering_garden(GardenManager.list_garden[0])
    GardenManager.increase_watering_garden(GardenManager.list_garden[1])
    # GardenManager.create_garden_network("Alice", oak2)

    print()
    for i in range(len(GardenManager.list_garden)):
        GardenManager.garden_report(GardenManager.list_garden[i])
        print()


if __name__ == "__main__":
    main()