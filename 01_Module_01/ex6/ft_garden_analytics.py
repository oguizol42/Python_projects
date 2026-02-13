# > python3 ft_garden_analytics.py
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

# class GardenManager
#   => Gere plusieurs jardins
#   => @classmethode create_garden_network()
#   => methode(imbriquee) GardenStats()
#         => calcul statistiques
# class Plant
# 		=> attributs: nom et taille en cm
# class FloweringPlant
# 		=> herite de class Plant
# 		=> attribut: floraison(blooming)    -     exemple: red flowers(blooming)
# class PrizeFlower
# 		=> herite de class FloweringPlant (et donc de class Plant)
# 		=> attribut: prize points

# Caracteristiques d'une classe Garden: (sous class de GardenManager)
# 		- nom (self)
# 		- liste de plantes (self)

# Caracteristiques class PlantList: (sous class de jardin)
# 		- nom (self)
# 		- type: class Plante ou class FloweringPlant ou class PrizeFlower (self)


class GardenManager:
    gardens_list = []  # Instance Garden list

    class Garden:
        class Plant:
            def __init__(self, name, height):
                self.name = name
                self.height = height

        class FloweringPlant(Plant):
            def __init__(self, bloom):
                self.bloom = bloom

        class PrizeFlower(FloweringPlant):
            def __init__(self, points):
                self.points = points

        def __init__(self, name_garden):
            self.name_garden = name_garden

    def create_garden_network(cls, garden):
        cls.gardens_data.append(garden)

    create_garden_network = classmethod(create_garden_network)

    def print_list_gardens(list):
        for i in range(len(list)):
            print(f"{list[i]}'s garden")

    print_list_gardens = staticmethod(print_list_gardens)


def test():
    babibel = GardenManager.Garden("Alice")

    GardenManager.create_garden_network("Alice")
    GardenManager.create_garden_network("Bob")
    GardenManager.create_garden_network("Jacouille")
    GardenManager.print_list_gardens(GardenManager.gardens_data)


if __name__ == "__main__":
    test()
