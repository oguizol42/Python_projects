from typing import Callable


def spell_combiner(
            spell1: Callable[[str, int], str],
            spell2: Callable[
                        [str, int],
                        str
                        ]
            ) -> Callable[
                    [str, int],
                    tuple[str, str]
                    ]:
    def combined(target: str, power: int) -> tuple[str, str]:
        string1: str = spell1(target, power)
        string2: str = spell2(target, power)
        return (string1, string2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        power = power * multiplier
        return (base_spell(target, power))
    return amplifier


def conditional_caster(
                condition: Callable[[str, int], bool],
                spell: Callable[
                        [str, int],
                        str
                        ]
                ) -> Callable[[str, int], str]:
    def conditionnal(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditionnal


def spell_sequence(spells: list[Callable[
                            [str, int],
                            str],
                            ]) -> Callable[
                                    [str, int],
                                    list[str]
                                    ]:
    def sequenced(target: str, power: int) -> list[str]:
        return list(map(lambda x: x(target, power), spells))
    return sequenced


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def hit(target: str, power: int) -> str:
    return f"Hit fight {target} with {power} destruction power"


def babybel(target: str, power: int) -> str:
    return f"Babybel and {target} are a power of {power}"


def condition_example(target: str, power: int) -> bool:
    if power > 50:
        return True
    else:
        return False


def main() -> None:
    print("Testing spell combiner...")
    combined: Callable = spell_combiner(hit, heal)
    print(f"Combined spell result: {combined('dragon', 10000)}")

    print("\nTesting power amplifier...")
    amplified: Callable = power_amplifier(hit, 3)
    print(f"Original: 10, Amplified: {amplified('Dragon', 10)}")

    print("\nTesting conditional caster...")
    condition: Callable = conditional_caster(condition_example, heal)
    print(f"{condition('Babybel', 51)}")
    print("\nNow with power == 50:")
    print(f"{condition('Kiri', 50)}")

    list_functions: list[Callable] = [
        heal,
        hit,
        babybel
    ]
    print("\nTesting spell sequence...")
    spell_seq: Callable = spell_sequence(list_functions)
    print(f"{spell_seq('Vache qui ri', 1994)}")


if __name__ == "__main__":
    main()
