import ex0
import ex1
import ex2
from ex0.creature_factory import CreatureFactory
from ex2.abstract_strategy import BattleStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(0, (len(opponents) - 1)):
        for j in range((i + 1), len(opponents)):

            factory_a, strat_a = opponents[i]
            factory_b, strat_b = opponents[j]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("\n* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")

            if not strat_a.is_valid(creature_a):
                raise Exception(
                    f"Invalid Creature '{creature_a.name}' for this strategy"
                )

            if not strat_b.is_valid(creature_b):
                raise Exception(
                    f"Invalid Creature '{creature_b.name}' for this strategy"
                )

            print(strat_a.act(creature_a))
            print(strat_b.act(creature_b))


def main() -> None:
    # • Create various Creature factories (from ex0 and ex1).
    flame_factory = ex0.FlameFactory()
    aqua_factory = ex0.AquaFactory()
    healing_creature_factory = ex1.HealingCreatureFactory()
    transform_creature_factory = ex1.TransformCreatureFactory()

    # • Create the three strategies.
    normal_strategy = ex2.NormalStrategy()
    aggressive_strategy = ex2.AggressiveStrategy()
    defensive_strategy = ex2.DefensiveStrategy()

    # • Define a single battle function that:
    tournament0 = [
        (flame_factory, normal_strategy),
        (healing_creature_factory, defensive_strategy),
    ]

    tournament1 = [
        (flame_factory, aggressive_strategy),
        (healing_creature_factory, defensive_strategy),
    ]

    tournament2 = [
        (aqua_factory, normal_strategy),
        (healing_creature_factory, defensive_strategy),
        (transform_creature_factory, aggressive_strategy),
    ]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(tournament0)

    try:
        print("\nTournament 1 (error)")
        print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
        battle(tournament1)
    except Exception as e:
        print(f"Battle error, aborting tournament: {e}")

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(tournament2)


if __name__ == "__main__":
    main()
