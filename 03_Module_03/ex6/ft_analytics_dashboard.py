def dictionary() -> dict:
    """Create a Dcitionary of Players"""
    new_dict: dict = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
    }
    return new_dict


def tuple_list() -> list:
    """Create a List of Tuples"""
    new_list: list = [
        ("alice", 2300, True),
        ("bob", 900, True),
        ("charlie", 2150, True),
        ("diana", 2050, False),
    ]
    return new_list


def main() -> None:
    high_scores_list: list = [str]
    scores_list: list = [int]
    players_list: list = [str]
    new_list: list = []
    new_dict: dict = {}
    # player: str
    # score: int
    # state: bool

    """Game Analytics Dashboard"""
    print("=== Game Analytics Dashboard ===")
    new_list = tuple_list()
    print()
    high_scores_list = [
        player for player, score, _ in new_list if score > 2000
    ]
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
    print("Player scores:", new_dict)

    print("Score categories: ")  # {'high': 3, 'medium': 2, 'low': 1}
    print("Achievement counts: ")  # {'alice': 5, 'bob': 3, 'charlie': 7}


if __name__ == "__main__":
    main()


# === List Comprehension Examples ===
# High scorers (>2000): ['alice', 'charlie', 'diana']
# Scores doubled: [4600, 3600, 4300, 4100]
# Active players: ['alice', 'bob', 'charlie']

# === Dict Comprehension Examples ===
# Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
# Score categories: {'high': 3, 'medium': 2, 'low': 1}
# Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}

# === Set Comprehension Examples ===
# Unique players: {'alice', 'bob', 'charlie', 'diana'}
# Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
# Active regions: {'north', 'east', 'central'}

# === Combined Analysis ===
# Total players: 4
# Total unique achievements: 12
# Average score: 2062.5
# Top performer: alice (2300 points, 5 achievements)

# $> python3 ft_analytics_dashboard.py
# === Game Analytics Dashboard ===

# === List Comprehension Examples ===
# High scorers (>2000): ['alice', 'charlie', 'diana']
# Scores doubled: [4600, 3600, 4300, 4100]
# Active players: ['alice', 'bob', 'charlie']

# === Dict Comprehension Examples ===
# Player scores: {'alice': 2300, 'bob': 1800, 'charlie': 2150}
# Score categories: {'high': 3, 'medium': 2, 'low': 1}
# Achievement counts: {'alice': 5, 'bob': 3, 'charlie': 7}

# === Set Comprehension Examples ===
# Unique players: {'alice', 'bob', 'charlie', 'diana'}
# Unique achievements: {'first_kill', 'level_10', 'boss_slayer'}
# Active regions: {'north', 'east', 'central'}

# === Combined Analysis ===
# Total players: 4
# Total unique achievements: 12
# Average score: 2062.5
# Top performer: alice (2300 points, 5 achievements)
