class Plant:
	""" Plant Informations """
	def __init__(self, name: str, height: int, age: int):
		""" def plant informations """
		self.name = str(name)
		self.height = int(height)
		self.age = int(age)
	def get_info(self) -> None:
		""" Print Plant Informations """
		print(f"Created: {self.name} ({self.height}cm, {self.age} days)")
def init_plants() -> list[Plant]:
	""" Initialising list plants objects """
	p_data = [
		("Rose", 25, 30),
		("Oak", 200, 365),
		("Cactus", 5, 90),
		("Sunflower", 80, 45),
		("Fern", 15, 120)
	]
	p = [Plant(name, height, age) for name, height, age in p_data]
	return p

def main() -> None:
	"""=== Plant Factory Output ==="""
	p = init_plants()
	print("=== Plant Factory Output ===")
	for i in range(len(p)):
		p[i].get_info()
	print("Total plants created:", len(p))
	
if __name__ == '__main__':
	main()