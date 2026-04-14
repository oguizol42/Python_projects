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

# Sproutling is a Grass type Creature
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount
# evolved:
# Bloomelle is a Grass/Fairy type Creature
# Bloomelle uses Petal Dance!
# Bloomelle heals itself and others for a large amount

# Testing Creature with transform capability
# base:
# Shiftling is a Normal type Creature
# Shiftling attacks normally.
# Shiftling shifts into a sharper form!
# Shiftling performs a boosted strike!
# Shiftling returns to normal.
# evolved:
# Morphagon is a Normal/Dragon type Creature
# Morphagon attacks normally.
# Morphagon morphs into a dragonic battle form!
# Morphagon unleashes a devastating morph strike!
# Morphagon stabilizes its form
