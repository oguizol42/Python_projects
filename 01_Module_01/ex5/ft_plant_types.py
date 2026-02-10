class Plant:
	""" Plant Informations """
	def __init__(self, name: str, height: int, age: int):
		""" def plant informations """
		self.name = str(name)
		self.height = int(height)
		self.age = int(age)

class Flower(Plant):
	""" Flower informations """
	def __init__(self, name: str, height: int, age: int, color: str, bloom_str: str):
		""" Def Flower informations """
		super().__init__(name, height, age)
		self.color = color
		self.bloom_str = bloom_str
	def get_info(self) -> None:
		""" Print Infos """
		print()
		print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")
	def bloom(self) -> None:
		print(f"{self.name} is blooming {self.bloom_str}")

class Tree(Plant):
	""" Tree Informations """
	def __init__(self, name: str, height: int, age: int, trunk_diameter: int, produce_shade_int: int):
		""" Def Tree Informations """
		super().__init__(name, height, age)
		self.trunk_diameter = trunk_diameter
		self.produce_shade_int = produce_shade_int
	def get_info(self) -> None:
		""" Print Infos """
		print()
		print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter} cm diameter")
	def produce_shade(self) -> None:
		print(f"{self.name} provide {self.produce_shade_int} square meters of shade")

class Vegetable(Plant):
	""" Vegetable Informations """
	def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
		""" Def Vegetable Informations """
		super().__init__(name, height, age)
		self.harvest_season = str(harvest_season)
		self.nutritional_value = str(nutritional_value)
	def get_info(self) -> None:
		""" Print Infos """
		print()
		print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
	def print_nutritional_value(self) -> None:
		print(f"{self.name} is {self.nutritional_value}")

def init_list_flower() -> list[Flower]:
	""" Init List of Flowers """
	p_data = [
		("Rose", 25, 30, "red", "beautifully!"),
		("Marguerite", 30, 780, "white", "easily!")
	]
	flow = [Flower(name, height, age, color, bloom) for name, height, age, color, bloom in p_data]
	return flow

def init_list_tree() -> list[Tree]:
	""" Init List of Trees """
	p_data = [
		("Oak", 500, 1825, 50, 78),
		("Olivier", 700, 365000, 20000, 6)
	]
	tree = [Tree(name, height, age, trunk_diameter, produce_shade) for name, height, age, trunk_diameter, produce_shade in p_data]
	return tree

def init_list_vegetable() -> list[Vegetable]:
	""" Init List of Vegetables """
	p_data = [
		("Tomato", 80, 90, "summer", "rich in vitamin C"),
		("Kiwi", 7, 28, "autumn", "rich in vitamin C, K and E")
	]
	vegetables = [Vegetable(name, height, age, harvest_season, nutritional_value) for name, height, age, harvest_season, nutritional_value in p_data]
	return vegetables

def main() -> None:
	""" Plant Types """
	flowers_list = init_list_flower()
	trees_list = init_list_tree()
	vegetables_list = init_list_vegetable()
	print("=== Garden Plant Types ===")
	for i in range(2):
		flowers_list[i].get_info()
		flowers_list[i].bloom()
		trees_list[i].get_info()
		trees_list[i].produce_shade()
		vegetables_list[i].get_info()
		vegetables_list[i].print_nutritional_value()

if __name__ == '__main__':
	main()