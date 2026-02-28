def find_unique_two_sets(set1: set, set2: set) -> set:
    """Create a set of Unique Datas Between Two Sets"""
    rare1 = set1.difference(set2)
    rare2 = set2.difference(set1)
    rare = rare1.union(rare2)
    return rare


def find_unique_three_sets(set1: set, set2: set, set3: set) -> set:
    """Create a set of Unique Datas Between Three Sets"""

    rare1_2 = set1.difference(set2)
    rare1 = rare1_2.difference(set3)
    rare2_1 = set2.difference(set1)
    rare2 = rare2_1.difference(set3)
    rare3_1 = set3.difference(set1)
    rare3 = rare3_1.difference(set2)
    rare = rare1.union(rare2)
    rare = rare.union(rare3)
    return rare


def main() -> None:
    """=== Achievement Tracker ==="""
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }
    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()
    print("=== Achievement Analytics ===")
    unique = alice.union(bob)
    unique = unique.union(charlie)
    print(f"All unique achievements: {unique}")
    size = len(unique)
    print(f"Total unique achievements: {size}")
    common_alice_bob = alice.intersection(bob)
    common = common_alice_bob.intersection(charlie)
    print(f"Common to all players: {common}")

    rare = find_unique_three_sets(alice, bob, charlie)
    print(f"Rare achievements (1 player): {rare}")

    print(f"Alice vs Bob common: {common_alice_bob}")
    alice_unique = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
