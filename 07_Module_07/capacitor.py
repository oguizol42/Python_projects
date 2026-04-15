import ex1


print("Testing Creature with healing capability")
print("base:")

sproutling = ex1.HealingCreatureFactory().create_base()
print(f"{sproutling.describe()}")
print(f"{sproutling.attack()}")
print(f"{sproutling.heal()}")

print(" evolved:")
bloomelle = ex1.HealingCreatureFactory().create_evolved()
print(f"{bloomelle.describe()}")
print(f"{bloomelle.attack()}")
print(f"{bloomelle.heal()}")

print("\nTesting Creature with transform capability")
print("base:")
shiftling = ex1.TransformCreatureFactory().create_base()
print(f"{shiftling.describe()}")
print(f"{shiftling.attack()}")
print(f"{shiftling.transform()}")
print(f"{shiftling.attack()}")
print(f"{shiftling.revert()}")
print(" evolved:")
morphagon = ex1.TransformCreatureFactory().create_evolved()
print(f"{morphagon.describe()}")
print(f"{morphagon.attack()}")
print(f"{morphagon.transform()}")
print(f"{morphagon.attack()}")
print(f"{morphagon.revert()}")
