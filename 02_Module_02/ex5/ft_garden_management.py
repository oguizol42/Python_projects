class GardenManager:
    """Manage a Garden of Plants"""

    class Plant:
        """Plants Caracteristics"""

        def __init__(
            self, plant_name: str, water_level: int, sunlight_hours: int
        ) -> None:
            self.name = plant_name
            self.water_level = water_level
            self.sunlight_hours = sunlight_hours

    class PlantNameError(Exception):
        """No Name or Name String Empty"""

        pass

    class WaterError(Exception):
        """Watering of Plant Not correct"""

        pass

    class SunlightHoursError(Exception):
        """Sunlight Hours of plant Not Correct"""

        pass

    def __init__(self) -> None:
        self.plants = []
        self.water_in_tank: int = 20

    def check_plant_health(self, plant: Plant) -> None:
        """Check if Plant is Valid"""
        if not plant.name:
            raise GardenManager.PlantNameError(
                "Error: Plant name cannot be empty!"
            )
        elif not 1 <= plant.water_level <= 10:
            if plant.water_level > 10:
                raise GardenManager.WaterError(
                    f"Error: Water level {plant.water_level} "
                    "is too high (max 10)"
                )
            else:
                raise GardenManager.WaterError(
                    f"Error: Water level {plant.water_level} "
                    "is too low (min 1)"
                )
        elif not 2 <= plant.sunlight_hours <= 12:
            if plant.sunlight_hours > 12:
                raise GardenManager.SunlightHoursError(
                    f"Error: Sunlight hours {plant.sunlight_hours} "
                    "is too high (max 12)"
                )
            else:
                raise GardenManager.SunlightHoursError(
                    f"Error: Sunlight hours {plant.sunlight_hours} "
                    "is too low (min 2)"
                )

    def check_tank_water(self) -> None:
        """Checking Level of Water in Tank"""
        if self.water_in_tank < 1:
            raise GardenManager.WaterError(
                "Caught GardenError: Not enough water in tank"
            )

    def fill_tank(self):
        """Fill the Tank of Water"""
        self.water_in_tank = len(self.plants) * 10

    def add_plant(
        self, name: str, water_level: int, sunlight_hours: int
    ) -> None:
        """Add Plant in Garden"""
        plant = GardenManager.Plant(name, water_level, sunlight_hours)
        self.check_plant_health(plant)
        self.plants.append(plant)

    def water_plants(self) -> None:
        """Watering Plants"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                try:
                    if not plant.name:
                        raise GardenManager.PlantNameError(
                            "Error: Cannot water None - invalid plant!"
                        )
                    else:
                        if self.water_in_tank > 0:
                            plant.water_level += 1
                            self.water_in_tank -= 1
                            print(f"Watering {plant.name} - success")
                        else:
                            raise GardenManager.WaterError(
                                "Caught GardenError: Not enough water in tank"
                            )

                except GardenManager.PlantNameError as e:
                    print(e)
                except GardenManager.WaterError as e:
                    raise GardenManager.WaterError(e)
        finally:
            print("Closing watering system (cleanup)")


def create_plants_list() -> list:
    """Create List of Plants"""
    plants_list = [("tomato", 4, 8), ("lettuce", 1, 3), ("", 1, 14)]
    return plants_list


def test_garden_management():
    """Test Several Errors Situations"""
    garden = GardenManager()
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    plants_list = create_plants_list()
    for plant in plants_list:
        try:
            garden.add_plant(plant[0], plant[1], plant[2])
        except GardenManager.PlantNameError as e:
            print("Error adding plant: ", end="")
            print(e)
        except GardenManager.WaterError as e:
            print("Error adding plant: ", end="")
            print(e)
        except GardenManager.SunlightHoursError as e:
            print("Error adding plant: ", end="")
            print(e)
        else:
            print(f"Added {plant[0]} successfully")
    print()
    print("Watering plants...")
    try:
        garden.water_plants()
    except GardenManager.PlantNameError as e:
        print(e)
    except GardenManager.WaterError as e:
        print(e)
    print()
    print("Checking plant health...")
    garden.plants[1].sunlight_hours = 15
    for plant in garden.plants:
        try:
            garden.check_plant_health(plant)
        except GardenManager.PlantNameError as e:
            print(e)
        except GardenManager.WaterError as e:
            print(e)
        except GardenManager.SunlightHoursError as e:
            print(e)
        else:
            print(
                f"{plant.name}: healthy (water: {plant.water_level}, "
                "sun: {plant.sunlight_hours})"
            )
    print()
    print("Testing error recovery...")
    garden.water_in_tank = 0
    try:
        garden.check_tank_water()
    except GardenManager.WaterError as e:
        print(e)
        garden.fill_tank()
        try:
            garden.check_tank_water()
        except GardenManager.WaterError as e:
            print(e)
        else:
            print("System recovered and continuing...")
    print()
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
