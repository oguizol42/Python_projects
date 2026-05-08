from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers"""
    ops: dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: max(a, b),
        "min": lambda a, b: min(a, b)
    }
    if not spells:
        return 0
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """partial applications"""
    fire = partial(base_enchantment, 50, "fire")
    water = partial(base_enchantment, 50, "water")
    air = partial(base_enchantment, 50, "air")
    return {
            "fire": fire,
            "water": water,
            "air": air
        }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Cached fibonacci"""
    if n < 2:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """single dispatch system"""
    @singledispatch
    def dispatcher(x: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @dispatcher.register
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @dispatcher.register
    def _(x: list) -> str:
        return f"Multi-cast: {len(x)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer([2, 5, 3, 90], 'add')}")
    print(f"Product: {spell_reducer([2, 12, 10, 1000], 'multiply')}")
    print(f"Max: {spell_reducer([2, 12, 10, 40, 25, 30], 'max')}")
    # print(spell_reducer([], 'multiply'))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher('fireball'))
    print(dispatcher([3, 'fireball', 42]))
    print(dispatcher(4.2))


if __name__ == "__main__":
    main()
