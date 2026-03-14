def tuple_list() -> list:
    """Create a List of Tuples"""
    new_list: list = [
        ("alice", 2300, True),
        ("bob", 900, True),
        ("charlie", 2150, True),
        ("diana", 2050, False),
    ]
    return new_list


def tuple_list2() -> list:
    """Create a List of Tuples"""
    new_list: list = [
        ("alice", 2300, 5),
        ("bob", 900, 4),
        ("charlie", 2150, 2),
        ("diana", 2050, 1),
    ]
    return new_list


def dictionary() -> dict:
    """Create a Dcitionary of Players"""
    players_list: list = []
    players_list = tuple_list()
    new_dict = {name: score for name, score, _ in players_list}
    return new_dict


def scores_categories_determining(scores_list: list) -> dict:
    """Counte Quantities of Scores for each Category"""
    dictionary: dict = {
        "high": 0,
        "medium": 0,
        "low": 0,
    }
    score: int = 0
    for score in scores_list:
        if score > 2200:
            dictionary["high"] += 1
        elif 2000 <= score <= 2200:
            dictionary["medium"] += 1
        else:
            dictionary["low"] += 1
    return dictionary


def set_creator() -> tuple[set, list]:
    """Create Set of Elements"""
    players_list: list = [
        "alice",
        "alice",
        "alice",
        "bob",
        "charlie",
        "diana",
        "bob",
        "charlie",
        "diana",
        "bob",
        "charlie",
        "diana",
        "bob",
        "charlie",
        "diana",
    ]
    players: set = set()
    players = {join for join in players_list}
    alice: set = {
        "first kill",
        "north",
        "east",
        "central",
    }
    bob: set = {
        "level_10",
        "north",
        "east",
        "central",
    }
    charlie: set = {
        "boss_slayer",
        "north",
        "east",
        "central",
    }
    diana: set = {
        "north",
        "east",
        "central",
    }
    set_list: list = [alice, bob, charlie, diana]
    return players, set_list


def unique_achievement_sets(set_list: list) -> set:
    """Create a Set of Unique Achievements"""
    set_final: set = set()
    set0: set = set_list[0]
    set1: set = set_list[1]
    set2: set = set_list[2]
    set3: set = set_list[3]
    set0 = set0.difference(set_list[1], set_list[2], set_list[3])
    set1 = set1.difference(set_list[0], set_list[2], set_list[3])
    set2 = set2.difference(set_list[0], set_list[1], set_list[3])
    set3 = set3.difference(set_list[1], set_list[2], set_list[0])
    set_final = set0.union(set1, set2, set3)
    return set_final


def active_regions_set(set_list: list) -> set:
    set_final: set = set_list[0]
    set_intermedary: set = {}
    for set_intermedary in set_list:
        set_final = set_final.intersection(set_intermedary)
    return set_final


def average_calcul(new_list: list) -> float:
    """Calcul the Average Score"""
    average: int = 0
    scores_list: list = []
    scores_list = [result[1] for result in new_list]
    average = sum(scores_list) / len(scores_list)
    return average


def find_player_with_score(score: int, players_list: list) -> str:
    """Find a Player Name by his Score"""
    player: list = []
    for player in players_list:
        if player[1] == score:
            return player[0]


def find_high_score(players_list: list) -> int:
    """Return the  High Score"""
    scores: list = []
    scores = [player[1] for player in players_list]
    return max(scores)


def qty_achievements_totale(players_list: list) -> int:
    """Return Quantity totale of achievements"""
    qty_totale: list = [achievement[2] for achievement in players_list]
    return sum(qty_totale)


def find_achievements_player(name: str, players_list: list) -> int:
    """Return Achievements's Quantity of one Player"""
    for player in players_list:
        if player[0] == name:
            return player[2]


def main() -> None:
    high_scores_list: list[str]
    scores_list: list[int]
    players_list: list[str]
    new_list: list = []
    set_list: list = []
    new_dict: dict = {}
    dictionary_cat: dict = {}
    players: set = set()
    unique_set = set()
    common_set = set()
    player_name: str
    high_score: int = 0
    average: float
    achievements_total: int = 0
    achievements_player: int = 0

    """Game Analytics Dashboard"""
    print("=== Game Analytics Dashboard ===")
    new_list = tuple_list()
    print()
    high_scores_list = [
        player for player, score, _ in new_list if score > 2000
    ]
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scores_list}")
    scores_list = [score * 2 for _, score, _ in new_list]
    print(f"Scores doubled: {scores_list}")
    players_list = [player for player, _, state in new_list if state is True]
    print(f"Active players: {players_list}")
    print()
    print("=== Dict Comprehension Examples ===")
    new_dict = dictionary()
    players_list = [player for player in new_dict.keys()]
    scores_list = [score for score in new_dict.values()]
    dictionary_cat = scores_categories_determining(scores_list)
    print("Player scores:", new_dict)
    print("Score categories:", dictionary_cat)
    for index in new_dict:
        new_dict[index] = len(index)
    print("Achievement counts:", new_dict)
    print()
    print("=== Set Comprehension Examples ===")
    players, set_list = set_creator()
    unique_set = unique_achievement_sets(set_list)
    print("Unique players:", players)
    print("Unique achievements:", unique_set)
    common_set = active_regions_set(set_list)
    print("Active regions:", common_set)
    print()
    print("=== Combined Analysis ===")
    new_list = tuple_list2()
    print("Total players:", len(new_list))
    high_score = find_high_score(new_list)
    player_name = find_player_with_score(high_score, new_list)
    achievements_player = find_achievements_player(player_name, new_list)
    achievements_total = qty_achievements_totale(new_list)
    print(f"Total unique achievements: {achievements_total}")
    average = average_calcul(new_list)
    print("Average score:", average)
    print(
        f"Top performer: {player_name} ({high_score} points,"
        f"{achievements_player} achievements)"
    )


if __name__ == "__main__":
    main()
