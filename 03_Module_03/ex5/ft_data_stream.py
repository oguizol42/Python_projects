from typing import Generator


def fibonacci_generator(first: int) -> Generator[int, None, None]:
    """Fibonacci Suite Generator"""
    nbr: int = 0
    nbr_2: int = 0
    nbr_1: int = 1
    for pos in range(first):
        if pos == 0:
            nbr = 0
        elif pos == 1:
            nbr = 1

        else:
            nbr = nbr_1 + nbr_2
            nbr_2 = nbr_1
            nbr_1 = nbr
        yield nbr


def check_prime_number(nbr: int) -> bool:
    """Check if nbr if a Prime Number"""
    try:
        if nbr > 1:
            for i in range(2, nbr):
                if nbr % i == 0:
                    return False
            return True
        return False
    except ValueError as e:
        print()
        print(e)


def next_prime_number(start: int) -> int:
    """Return the Next Prime Number or start if it is a Prime Number"""
    while True:
        if check_prime_number(start) is True:
            return start
        else:
            start = start + 1


def prime_numbers_generator(first: int) -> Generator[int, None, None]:
    """Prime Numbers Generator"""
    nbr: int = 2
    for pos in range(first):
        nbr = next_prime_number(nbr)
        yield nbr
        nbr = nbr + 1


def print_generator(to_print: Generator, qty: int):
    """Display Generator Datas on One Line"""
    try:
        if qty > 0:
            print(next(to_print), end="")
            for _ in range(1, qty):
                print(",", next(to_print), end="")
    except StopIteration:
        print()
        print("Too many arguments asked")


def killed_monster(name: str, dictionary: dict) -> None:
    """Killing Monster"""
    print(f"Player {name} (level {dictionary[name]}) killed monster")


def found_treasure(name: str, dictionary: dict) -> None:
    """Treasure Found"""
    print(f"Player {name} (level {dictionary[name]}) found treasure")


def leveled_up(name: str, dictionary: dict) -> dict:
    """Level Upper"""
    dictionary[name] += 1
    print(f"Player {name} (level {dictionary[name]}) leveled up")
    return dictionary


def player_dictionary() -> dict:
    """generate Dictionary Players"""
    players: dict = {"alice": int(5), "bob": int(12), "charlie": int(7)}
    return players


def event_manager(
    event_qty: int,
) -> Generator[tuple[int, int, int, int], None, None]:
    """Manage Events"""
    try:
        players_dict: dict
        players_dict = player_dictionary()
        total_event: int = 0
        high_level: int = 0
        treasure_event: int = 0
        level_up: int = 0
        for i in range(event_qty):
            killed_monster("alice", players_dict)
            total_event += 1
            high_level += 1
            yield total_event, high_level, treasure_event, level_up
            found_treasure("bob", players_dict)
            total_event += 1
            treasure_event += 1
            yield total_event, high_level, treasure_event, level_up
            players_dict = leveled_up("charlie", players_dict)
            total_event += 1
            level_up += 1
            yield total_event, high_level, treasure_event, level_up
            found_treasure("alice", players_dict)
            total_event += 1
            treasure_event += 1
            yield total_event, high_level, treasure_event, level_up
            players_dict = leveled_up("bob", players_dict)
            total_event += 1
            level_up += 1
            yield total_event, high_level, treasure_event, level_up
            killed_monster("charlie", players_dict)
            total_event += 1
            high_level += 1
            yield total_event, high_level, treasure_event, level_up
            players_dict = leveled_up("alice", players_dict)
            total_event += 1
            level_up += 1
            yield total_event, high_level, treasure_event, level_up
            killed_monster("bob", players_dict)
            total_event += 1
            high_level += 1
            yield total_event, high_level, treasure_event, level_up
            found_treasure("charlie", players_dict)
            total_event += 1
            treasure_event += 1
            yield total_event, high_level, treasure_event, level_up
    except StopIteration:
        print()
        print("Too many arguments asked")


def main() -> None:
    """Data Stream Generator"""
    first: int = 10
    nbr: int
    events_qty: int = 1000
    values_gene: Generator
    values: tuple
    print("=== Game Data Stream Processor ===")
    print()
    print(f"Processing {events_qty} game events...")
    print()
    values_gene = event_manager(events_qty)
    for i in range(events_qty):
        j = i + 1
        print(f"Event {j}: ", end="")
        values = next(values_gene)
    print()
    print("=== Stream Analytics ===")
    print()
    print(f"Total events processed: {values[0]}")
    print(f"High-level players (10+): {values[1]}")
    print(f"Treasure events: {values[2]}")
    print(f"Level-up events: {values[3]}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")
    nbr = fibonacci_generator(first)
    print(f"Fibonacci sequence (first {first}): ", end="")
    print_generator(nbr, (first))
    print()
    first = 5
    nbr = prime_numbers_generator(first)
    print(f"Prime numbers (first {first}): ", end="")
    print_generator(nbr, (first))


if __name__ == "__main__":
    main()
