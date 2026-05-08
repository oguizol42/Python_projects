#import sys
def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    seed_type = seed_type.capitalize()
    seed = "seeds:"
    if unit == "packets":
        unit = "packets available"
    elif unit == "grams":
        unit = "grams total"
    elif unit == "area":
        seed = "seeds: covers"
        unit = "square meters"
    else:
        unit = "Unknown unit type"
    print(seed_type, seed, quantity, unit)
#ft_seed_inventory(sys.argv[1], sys.argv[2], sys.argv[3])