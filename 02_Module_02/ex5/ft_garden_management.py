class GardenManager():
    """Manage a Garden of Plants"""
    class Plant():
        """Plants Caracteristics"""
        def __init__(self, plant_name: str, water_level: int, sunlight_hours: int) -> None:
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

    def check_plant_health(plant: Plant) -> None:
        """Check if Plant is Valid"""
        if not plant.name:
            raise GardenManager.PlantNameError("Error: Plant name cannot be empty!")
        elif not 1 <= plant.water_level <= 10:
            if plant.water_level > 10:
                raise GardenManager.WaterError(f"Error: Water level {plant.water_level} is too high (max 10)")
            else:
                raise GardenManager.WaterError(f"Error: Water level {plant.water_level} is too low (min 1)")
        elif not 2 <= plant.sunlight_hours <= 12:
            if plant.sunlight_hours > 12:
                raise GardenManager.SunlightHoursError(f"Error: Sunlight hours {plant.sunlight_hours} is too high (max 12)")
            else:
                raise GardenManager.SunlightHoursError(f"Error: Sunlight hours {plant.sunlight_hours} is too low (min 2)")
    
    check_plant_health = staticmethod(check_plant_health)

    def add_plant(self, name: str, water_level: int, sunlight_hours: int) -> None:
        """Add Plant in Garden"""
        plant = GardenManager.Plant(name, water_level, sunlight_hours)
        try:
            GardenManager.check_plant_health(plant)
        except GardenManager.PlantNameError as e:
            raise GardenManager.PlantNameError(e)
        except:
            self.plants.append(plant)
            
        else:            
            self.plants.append(plant)

    def water_plants(self) -> None:
        """Watering Plants"""
        print("Opening watering system")
        try:
            for plant in self.plants:
                if not plant.name:
                    raise GardenManager.PlantNameError("Error: Cannot water None - invalid plant!")
                else:
                    plant.water_level += 1
                    print(f"Watering {plant.name} - success")

        except GardenManager.PlantNameError as e:
            raise GardenManager.PlantNameError(e)
        finally:
            print("Closing watering system (cleanup)")


def test_garden_management():
    """Test Several Errors Situations"""
    garden = GardenManager()
    i = 0
    print("=== Garden Management System ===")
    print()
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 4, 8)
    except GardenManager.PlantNameError as e:
        print(e)
    else:
        print(f"Added {garden.plants[i].name} successfully")
    try:
        garden.add_plant("lettuce", 1, 15)
    except GardenManager.PlantNameError as e:
        print(e)
    else:
        i += 1
        print(f"Added {garden.plants[i].name} successfully")
    try:
        garden.add_plant("", 1, 14)
    except GardenManager.PlantNameError as e:
        print(e)
    else:
        i += 1
        print(f"Added {garden.plants[i].name} successfully")
    print()
    print("Watering plants...")
    try:
        garden.water_plants()
    except GardenManager.PlantNameError as e:
        print(e)
    print()
    print("Checking plant health...")
    for plant in garden.plants:
        try:
            GardenManager.check_plant_health(plant)
        except GardenManager.PlantNameError as e:
            print(e)
        except GardenManager.WaterError as e:
            print(e)
        except GardenManager.SunlightHoursError as e:
            print(e)
        else:
            print(f"{plant.name}: healthy (water: {plant.water_level}, sun: {plant.sunlight_hours})")
    print()
    print("Testing error recovery...")

if __name__ == '__main__':
    test_garden_management()


# test_garden_management() function that demonstrates:
# •Adding plants with both valid and invalid inputs
# •Watering plants with proper cleanup (using finally)
# •Checking plant health and handling validation errors
# •Error recovery - showing the system continues working after errors
# •Integration of all error handling techniques learned

# === Garden Management System ===

# Adding plants to garden...
# Added tomato successfully
# Added lettuce successfully
# Error adding plant: Plant name cannot be empty!

# Watering plants...
# Opening watering system
# Watering tomato - success
# Watering lettuce - success
# Closing watering system (cleanup)

# Checking plant health...
# tomato: healthy (water: 5, sun: 8)
# Error checking lettuce: Water level 15 is too high (max 10)

# Testing error recovery...
# Caught GardenError: Not enough water in tank
# System recovered and continuing...

# Garden management system test complete!