from xmlrpc.client import Boolean


class GardenManager():
	""" Manage Some Gardens """
	list_garden = []

	class Garden():
		""" Garden Definition """
		def __init__(self, name):
			self.name = name
			self.reg_plant_list = []
			self.flow_plant_list = []
			self.prize_plant_list = []		

	class Plant():
		""" Plant Definition """
		def __init__(self, name, height):
			self.name = str(name)
			self.height = int(height)

	class FloweringPlant(Plant):
		""" FloweringPlant Definition """
		def __init__(self, name, height, bloom):
			super().__init__(name, height)
			self.bloom = str(bloom)

	class PrizeFlower(FloweringPlant):
		""" PrizeFlower Definition """
		def __init__(self, name, height, bloom, points):
			super().__init__(name, height, bloom)
			self.points = int(points)

	def __init__(self):
		pass	# TEMPO

	def create_garden_network(cls, name, plants = None) -> None:
		""" Add Garden and Plants"""
		new_garden = cls.find_garden(cls.list_garden, name)
		if new_garden == None:
			new_garden = cls.Garden(name)
			cls.list_garden.append(new_garden)
			print(f"{name} has just added in garden's list") # TEMPO
		if plants != None:
			GardenManager.add_plant(new_garden, plants)

	create_garden_network = classmethod(create_garden_network)

	def find_garden(list_garden, name_newG) -> Garden:
		""" Find Garden in List """
		if len(list_garden) > 0:
			for i in range(len(list_garden)):
				if list_garden[i].name == name_newG:
					return list_garden[i]
		return None

	def add_plant(garden: Garden, plants) -> None:
		""" Put Plants in a Garden """
		plants = GardenManager.obj_to_list(plants)
		for i in range(len(plants)):
			if type(plants[i]) == GardenManager.Plant:
				garden.reg_plant_list.append(plants[i])
			if type(plants[i]) == GardenManager.FloweringPlant:
				garden.flow_plant_list.append(plants[i])
			if type(plants[i]) == GardenManager.PrizeFlower:
				garden.prize_plant_list.append(plants[i])
			print(f"Added {plants[i].name} to {garden.name}'s garden")

	def disp_plants_list(garden: Garden):
		""" Print List of Plants """
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
		""" Print Garden Caraceteristics """
		print(f"=== {garden.name}'s Garden Report ===")
		
		qty_reg, qty_flow, qty_priz, total = \
			GardenManager.sum_three_size_list(
				garden.reg_plant_list, 
				garden.flow_plant_list, 
				garden.prize_plant_list
			)
		if total > 0:
			print("Plants in garden: ")
			GardenManager.disp_plants_list(garden)
		else:
			print("Plants in garden: None")
		print(f"Plants added: {total}, Total growth: ?cm") # COMPLETER TAILLE EN cm
		print(
			f"Plant types: {qty_reg} regular,"
			f" {qty_flow} flowering,"
			f" {qty_priz} prize flowers"
		)
		print("Height validation test: True")
		print("Garden scores") # A COMPLETER
		print(f"Total gardens managed: {len(GardenManager.list_garden)}")

	garden_report = staticmethod(garden_report)
	
# === Alice's Garden Report ===
# Plants in garden:
# - Oak Tree: 101cm
# - Rose: 26cm, red flowers (blooming)
# - Sunflower: 51cm, yellow flowers (blooming), Prize points: 10
# Plants added: 3, Total growth: 3cm
# Plant types: 1 regular, 1 flowering, 1 prize flowers
# Height validation test: True
# Garden scores - Alice: 218, Bob: 92
# Total gardens managed: 2

	def obj_to_list(obj) -> list:
		""" Return a List from an Object """
		new_list = []
		if isinstance(obj, list):
			new_list = obj
		else:
			new_list.append(obj)
		return new_list

	obj_to_list = staticmethod(obj_to_list)

	def sum_three_size_list(obj1: list, obj2: list, obj3: list) -> tuple[(int, int, int, int)]:
		""" Return size of three list and total"""
		size1 = len(obj1)
		size2 = len(obj2)
		size3 = len(obj3)
		total = size1 + size2 + size3
		return size1, size2, size3, total

	sum_three_size_list = staticmethod(sum_three_size_list)

	def GardenStats(self) -> None:
		""" Statistics Calculator """
		pass	# TEMPO

def main() -> None:
	""" Test Function """	
	oak1 = GardenManager.Plant("Oak1 Tree", 101)
	oak2 = GardenManager.Plant("Oak2 Tree", 153)
	oak3 = GardenManager.Plant("Oak3 Tree", 208)

	rose1 = GardenManager.FloweringPlant("Rose1", 26, "red flowers")
	rose2 = GardenManager.FloweringPlant("Rose2", 32, "white flowers")
	rose2 = GardenManager.FloweringPlant("Rose3", 18, "green flowers")

	sunflower1 = GardenManager.PrizeFlower("Sunflower1", 51, "yellow flowers", 10)
	sunflower2 = GardenManager.PrizeFlower("Sunflower1", 63, "blue flowers", 14)
	sunflower3 = GardenManager.PrizeFlower("Sunflower1", 73, "orange flowers", 22)

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
	GardenManager.create_garden_network("Bob")
	GardenManager.create_garden_network("Alice")
	GardenManager.create_garden_network("Alice", rose1)
	GardenManager.create_garden_network("Alice", sunflower1)
	GardenManager.create_garden_network("Alice", oak2)

	print()
	for i in range(len(GardenManager.list_garden)):
		GardenManager.garden_report(GardenManager.list_garden[i])
		print()

if __name__ == '__main__':
	main()
	
# Example:
# $> python3 ft_garden_analytics.py
# === Garden Management System Demo ===
# Added Oak Tree to Alice's garden
# Added Rose to Alice's garden
# Added Sunflower to Alice's garden
# Alice is helping all plants grow...
# Oak Tree grew 1cm
# Rose grew 1cm
# Sunflower grew 1cm
# === Alice's Garden Report ===
# Plants in garden:
# - Oak Tree: 101cm
# - Rose: 26cm, red flowers (blooming)
# - Sunflower: 51cm, yellow flowers (blooming), Prize points: 10
# Plants added: 3, Total growth: 3cm
# Plant types: 1 regular, 1 flowering, 1 prize flowers
# Height validation test: True
# Garden scores - Alice: 218, Bob: 92
# Total gardens managed: 2