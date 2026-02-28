import sys


def manage_qty(dictionary: dict, items_list: list) -> None:
    """Create News Dict Categories Nested"""
    one_item: list = []
    all_items: dict = {}
    moderate: dict = {}
    scarce: dict = {}
    restock: dict = {}
    for one_item in items_list:
        if one_item[1] >= 4:
            moderate[one_item[0]] = one_item[1]
            all_items[one_item[0]] = one_item[1]
        else:
            scarce[one_item[0]] = one_item[1]
            all_items[one_item[0]] = one_item[1]
            if one_item[1] <= 1:
                restock[one_item[0]] = one_item[1]
    dictionary.update({"moderate": moderate})
    dictionary.update({"scarce": scarce})
    dictionary.update({"restock": restock})
    dictionary.update({"all_items": all_items})


def properties_demo(
    dictionary: dict, clef_test: str, items_list: list
) -> None:
    """Print Properties Dictionary"""
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    for i in range(len(items_list)):
        print(items_list[i][0], end="")
        if i < (len(items_list) - 1):
            print(", ", end="")
    print()
    print("Dictionary values: ", end="")
    for i in range(len(items_list)):

        print(items_list[i][1], end="")
        if i < (len(items_list) - 1):
            print(", ", end="")
    print()
    print(
        f"Sample lookup - '{clef_test}'in inventory:",
        clef_test in dictionary["all_items"],
    )


def abundance_evaluator(items_list: list) -> tuple[list, list]:
    """Evalute the Most Quantity and the Least Quantity of Items"""
    most: list = items_list[0]
    least: list = items_list[0]
    for one_item in items_list:
        if most[1] < one_item[1]:
            most = list(one_item)
        if least[1] > one_item[1]:
            least = list(one_item)
    return most, least


def create_dict(data_list: list) -> dict:
    """Create Dictionary from a List"""
    dictionary: dict = {}
    for data in data_list:
        data_split = data.split(":")
        dictionary.update({str(data_split[0]): int(data_split[1])})
    return dictionary


def items_counter(dictionary: dict) -> tuple[int, int]:
    """Count Items Total Uantity and Unique Items Quantity"""
    total_items_qty: int = 0
    unique_items_qty = len(dictionary.keys())
    for qty in dictionary.values():
        total_items_qty += int(qty)
    return unique_items_qty, total_items_qty


def main():
    """Inventory System"""
    most: list = []
    least: list = []
    try:
        if len(sys.argv) > 1:
            dictionary = create_dict(sys.argv[1:])
            items_list = list(dictionary.items())
            unique_items_qty, total_items_qty = items_counter(dictionary)
            print("=== Inventory System Analysis ===")
            print(f"Total items in inventory: {total_items_qty}")
            print(f"Unique item types: {unique_items_qty}")
            print()
            print("=== Current Inventory ===")
            for one_item in items_list:
                percent: float = 100 * (one_item[1] / total_items_qty)
                print(f"{one_item[0]}: {one_item[1]} units ({percent:.1f}%)")
            print()
            most, least = abundance_evaluator(items_list)
            print("=== Inventory Statistics ===")
            print(f"Most abundant: {most[0]} ({most[1]} units)")
            print(f"Least abundant: {least[0]} ({least[1]} unit)")
            print()
            manage_qty(dictionary, items_list)
            print("=== Item Categories ===")
            print(f"Moderate: {dictionary['moderate']}")
            print(f"Scarce: {dictionary['scarce']}")
            print()
            print("=== Management Suggestions ===")
            print(f"Restock needed: {dictionary['restock']}")
            print()
            properties_demo(dictionary, "sword", items_list)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
