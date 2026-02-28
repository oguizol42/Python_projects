import sys

def create_dict(data_list: list) -> dict:
    """Create Dictionary from a List"""
    dictionary: dict = {}
    for data in data_list:
        data_split = data.split(":")
        dictionary.update({str(data_split[0]): int(data_split[1])})
    return dictionary

def items_counter(dictionary: dict) -> tuple[int, int]:
    """Count Items Total Uantity and Unique Items Quantity"""
    unique_qty = len(dictionary.keys())
    return unique_qty, 0

def main():
    """Inventory System"""
    inventory_list: list = []
    try:
        if len(sys.argv) > 1:
            dictionary = create_dict(sys.argv[1:])
            items_list = dictionary.items()
            print(f"{items_list}")
            test,test2 = items_counter(dictionary)
            print("=== Inventory System Analysis ===")
            print(f"Total items in inventory: {test2}")
            print(f"Unique item types: {test}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# $> python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1

# === Inventory System Analysis ===
# Total items in inventory: 12
# Unique item types: 5

# === Current Inventory ===
# potion: 5 units (41.7%)
# armor: 3 units (25.0%)
# shield: 2 units (16.7%)
# sword: 1 unit (8.3%)
# helmet: 1 unit (8.3%)

# === Inventory Statistics ===
# Most abundant: potion (5 units)
# Least abundant: sword (1 unit)

# === Item Categories ===
# Moderate: {'potion': 5}
# Scarce: {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}

# === Management Suggestions ===
# Restock needed: sword, helmet

# === Dictionary Properties Demo ===
# Dictionary keys: sword, potion, shield, armor, helmet
# Dictionary values: 1, 5, 2, 3, 1
# Sample lookup - 'sword'in inventory: True