import ex0

print("Testing factory")
flameling = ex0.FlameFactory().create_base()
pyrodon = ex0.FlameFactory().create_evolved()
print(f"{flameling.describe()}")
print(f"{flameling.attack()}")
print(f"{pyrodon.describe()}")
print(f"{pyrodon.attack()}")

print("\nTesting factory")
aquabub = ex0.AquaFactory().create_base()
torragon = ex0.AquaFactory().create_evolved()
print(f"{aquabub.describe()}")
print(f"{aquabub.attack()}")
print(f"{torragon.describe()}")
print(f"{torragon.attack()}")

print("\nTesting battle")
print(
    f"{flameling.describe()}\n"
    " vs.\n"
    f"{aquabub.describe()}\n"
    " fight\n"
    f"{flameling.attack()}\n"
    f"{aquabub.attack()}"
)
