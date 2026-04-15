# AMELIORER battle() POUR ORGANISER DES TOURNOIS ENTRE AUTANT DE CONCURANT QUE POSSIBLE
# FAIRE mypy


import ex0
import ex1
import ex2
from typing import Union


def battle(
    tournament: list[
        tuple[
            Union[
                ex0.FlameFactory,
                ex0.AquaFactory,
                ex1.HealingCreatureFactory,
                ex1.TransformCreatureFactory,
            ],
            Union[
                ex2.NormalStrategy,
                ex2.AggressiveStrategy,
                ex2.DefensiveStrategy,
            ],
        ]
    ],
) -> None:
    print("*** Tournament ***")
    print(f"{len(tournament)} opponents involved\n")
    print("* Battle *")
    print(tournament[0][0].describe())
    print(" vs.")
    print(tournament[1][0].describe())
    print(" now fight!")
    print(tournament[0][1].act(tournament[0][0]))
    if tournament[0][1].is_valid(tournament[0][0]) is True:
        print(tournament[1][1].act(tournament[1][0]))


# * Battle *
# Flameling is a Fire type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Flameling uses Ember!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount


def main() -> None:
    # • Create various Creature factories (from ex0 and ex1).
    flameling = ex0.FlameFactory().create_base()
    aquabub = ex0.AquaFactory().create_base()
    sproutling = ex1.HealingCreatureFactory().create_base()
    shiftling = ex1.TransformCreatureFactory().create_base()

    # • Create the three strategies.
    normal_strategy = ex2.NormalStrategy()
    aggressive_strategy = ex2.AggressiveStrategy()
    defensive_strategy = ex2.DefensiveStrategy()

    # • Define a single battle function that:
    tournament0: list[
        tuple[
            Union[
                ex0.FlameFactory,
                ex0.AquaFactory,
                ex1.HealingCreatureFactory,
                ex1.TransformCreatureFactory,
            ],
            Union[
                ex2.NormalStrategy,
                ex2.AggressiveStrategy,
                ex2.DefensiveStrategy,
            ],
        ]
    ] = [(flameling, normal_strategy), (sproutling, defensive_strategy)]

    tournament1: list[
        tuple[
            Union[
                ex0.FlameFactory,
                ex0.AquaFactory,
                ex1.HealingCreatureFactory,
                ex1.TransformCreatureFactory,
            ],
            Union[
                ex2.NormalStrategy,
                ex2.AggressiveStrategy,
                ex2.DefensiveStrategy,
            ],
        ]
    ] = [
        (flameling, aggressive_strategy),
        (sproutling, defensive_strategy),
    ]

    tournament2: list[
        tuple[
            Union[
                ex0.FlameFactory,
                ex0.AquaFactory,
                ex1.HealingCreatureFactory,
                ex1.TransformCreatureFactory,
            ],
            Union[
                ex2.NormalStrategy,
                ex2.AggressiveStrategy,
                ex2.DefensiveStrategy,
            ],
        ]
    ] = [
        (aquabub, normal_strategy),
        (sproutling, defensive_strategy),
        (shiftling, aggressive_strategy),
    ]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(tournament0)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(tournament1)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(tournament2)


if __name__ == "__main__":
    main()

#       ◦ takes a list of opponents in the tournament; each opponent is defined as a
#        tuple consisting of a CreatureFactory and a BattleStrategy.
#       ◦ makes each opponent fight once all other opponents.
#       ◦ organizes each fight using each Creature’s associated strategy.
#       ◦ handles correctly invalid Creature-strategy tuples


# Tournament 0 (basic)
# [ (Flameling+Normal), (Healing+Defensive) ]
# *** Tournament ***
# 2 opponents involved

# * Battle *
# Flameling is a Fire type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Flameling uses Ember!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount

# Tournament 1 (error)
# [ (Flameling+Aggressive), (Healing+Defensive) ]
# *** Tournament ***
# 2 opponents involved

# * Battle *
# Flameling is a Fire type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Battle error, aborting tournament: Invalid Creature 'Flameling' for this aggressive strategy

# Tournament 2 (multiple)
# [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]
# *** Tournament ***
# 3 opponents involved

# * Battle *
# Aquabub is a Water type Creature
# vs.
# Sproutling is a Grass type Creature
# now fight!
# Aquabub uses Water Gun!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount

# * Battle *
# Aquabub is a Water type Creature
# vs.
# Shiftling is a Normal type Creature
# now fight!
# Aquabub uses Water Gun!
# Shiftling shifts into a sharper form!
# Shiftling performs a boosted strike!
# Shiftling returns to normal.

# * Battle *
# Sproutling is a Grass type Creature
# vs.
# Shiftling is a Normal type Creature
# now fight!
# Sproutling uses Vine Whip!
# Sproutling heals itself for a small amount
# Shiftling shifts into a sharper form!
# Shiftling performs a boosted strike!
# Shiftling returns to normal.

# POUR TEST
# print(f"{normal_strategy.act(flameling)}")
# print(f"{aggressive_strategy.act(flameling)}")
# print(f"{defensive_strategy.act(flameling)}\n")

# print(f"{normal_strategy.act(aquabub)}")
# print(f"{aggressive_strategy.act(aquabub)}")
# print(f"{defensive_strategy.act(aquabub)}\n")

# print(f"{normal_strategy.act(sproutling)}")
# print(f"{aggressive_strategy.act(sproutling)}")
# print(f"{defensive_strategy.act(sproutling)}\n")

# print(f"{normal_strategy.act(shiftling)}")
# print(f"{aggressive_strategy.act(shiftling)}")
# print(f"{defensive_strategy.act(shiftling)}\n")
