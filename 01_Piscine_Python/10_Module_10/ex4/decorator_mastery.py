from functools import wraps
from typing import Callable, Any
import time


def spell_timer(func: Callable) -> Callable:
    """Time execution decorator"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result: Any
        print(f"Casting {func.__name__}...")
        start: float = time.perf_counter()
        result = func(*args, **kwargs)
        end: float = time.perf_counter()
        duration: float = end - start
        print(f"Spell completed in {round(duration, 3)} seconds")
        print(f"Result: {func.__name__} cast!")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Parameterized validation decorator"""
    def decorator_factory(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator_factory


def retry_spell(max_attempts: int) -> Callable:
    """Retry decorator"""
    def check_spell(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... (attempt"
                        f" {n + 1}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return check_spell


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if all(c.isalpha() or c.isspace() for c in name):
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    for i in range(5000000):
        pass
    return "This function do nothing of special"


@power_validator(15)
def spell_test(spell_name: str, power: int) -> str:
    return "A new inutile function"


@retry_spell(3)
def spell_test2(spell_name: str, power: int) -> str:
    return "A new inutile function"


@retry_spell(3)
def spell_test3() -> str:
    return "A new inutile function"


def main() -> None:
    print("Testing spell timer...")
    fireball()

    print("\nTesting power_validator...")
    print("With a high value level")
    print(spell_test("36", 36))
    print("With a low value level")
    print(spell_test("36", 10))

    print("\nTesting retrying spell...")
    print(spell_test2())
    print("Waaaaaaagh spelled !")

    print("\nTesting retrying spell... with error")
    print(spell_test2("babybel", 1))
    print(spell_test2.__name__)

    print("\nTesting retrying spell...with error again")
    print(spell_test2("babybel", 1))
    print(spell_test2.__name__)

    print("\nTesting MageGuild...")
    mage_guild = MageGuild()
    print(mage_guild.validate_mage_name("b o n j o u r"))
    print(mage_guild.validate_mage_name("b o n, j o u r"))
    print(mage_guild.cast_spell("Lightning", 15))
    print(mage_guild.cast_spell("Babybel", 9))


if __name__ == "__main__":
    main()
