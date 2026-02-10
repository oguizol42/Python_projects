class Plant:
	""" Plant Informations """
	def __init__(self, name: str, height: int, age: int):
		""" def plant informations """
		self.name = str(name)
		self.height = int(height)
		self.age = int(age)

class SecurePlant:
	""" Security class Plant """
	def __init__(self, plant: Plant):
		""" def Plant to securise """
		self.__plant = plant
	def set_height(self) -> None:
		height = int(input("Enter a height: "))
		if height >= 0:
			self.__plant.height = int(height)
		else:
			print(f"Invalid operation attempted: height {height}cm [REJECTED]")
			print("Security: Negative height rejected")
	def set_age(self) -> None:
		age = int(input("Enter a age: "))
		if age >= 0:
			self.__plant.age = int(age)
		else:
			print(f"Invalid operation attempted: day {age}cm [REJECTED]")
			print("Security: Negative day rejected")
	def get_height(self) -> None:
		if self.__plant.height >= 0:
			
			print(f"Height updated: {self.__plant.height}cm [OK]")
		else:
			print(f"Invalid operation attempted: height {self.__plant.height}cm [REJECTED]")
			print("Security: Negative height rejected")
	def get_age(self) -> None:
		if self.__plant.age >= 0:
			print(f"Age updated: {self.__plant.age} days [OK]")
			print("")
		else:
			print(f"Invalid operation attempted: day {self.__plant.age}day [REJECTED]")
			print("Security: Negative day rejected")
			print("")
	def get_info(self) -> None:
		""" Print Plant Informations """
		if self.__plant.height >= 0:
			if self.__plant.age >= 0:
				print(f"Plant created: {self.__plant.name}")
		self.get_height()
		self.get_age()
		if self.__plant.height >= 0:
			if self.__plant.age >= 0:
				print(f"Current plant: {self.__plant.name} ({self.__plant.height}cm, {self.__plant.age} days)")
				print()


def init_plants() -> list[Plant]:
	""" Initialising list plants objects """
	p_data = [
		("Rose", 25, 30),
		("Oak", -200, 365),
		("Cactus", 5, -90),
		("Sunflower", 80, 45),
		("Fern", 15, 120)
	]
	p = [Plant(name, height, age) for name, height, age in p_data]
	return p

def main() -> None:
	""" === Garden Security System === """
	p = init_plants()
	print("=== Garden Security System ===")
	secur_p = SecurePlant(p[0])
	secur_p.get_info()
	secur_p.set_height()
	print()
	secur_p.get_info()
	secur_p.set_age()
	print()
	secur_p.get_info()

if __name__ == '__main__':
	main()

#•Provide controlled ways to modify plant data: set_height(), set_age()
#•Provide safe ways to access plant data: get_height(), get_age()

#=== Garden Security System ===
#Plant created: Rose
#Height updated: 25cm [OK]
#Age updated: 30 days [OK]
#Invalid operation attempted: height -5cm [REJECTED]
#Security: Negative height rejected
#Current plant: Rose (25cm, 30 days)