from typing import Callable, Union


def mage_counter() -> Callable:
    """Create a counting closure"""
    count: int = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Power Accumulator"""
    total = initial_power
    def accumulator(to_add: int) -> int:
        nonlocal total
        total = to_add + total
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    """Enchantment Functions"""
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    """Memory Management System"""
    dictionary: dict[str, int] = {}

    def store(key: str, value: int):
        dictionary[key] = value

    def recall(key: str) -> Union[int, str]:
        if key in dictionary:
            return dictionary[key]
        else:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter_a: Callable[[], int] = mage_counter()
    counter_b: Callable[[], int] = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    test_accumulator: Callable[[int], int]
    print("\nTesting spell accumulator...")
    test_accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {test_accumulator(20)}")
    print(f"Base 100, add 30: {test_accumulator(30)}")

    test_enchantment1: Callable[[str], str]
    test_enchantment2: Callable[[str], str]
    print("\nTesting enchantment factory...")
    test_enchantment1 = enchantment_factory("Flaming")
    test_enchantment2 = enchantment_factory("Frozen")
    print(test_enchantment1('Sword'))
    print(test_enchantment2('Shield'))

    print("\nTesting memory vault...")
    vault: dict[str, Callable] = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]('secret', 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
