import sys


def main() -> None:
    """Manage Scores"""
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> .."
        )
    else:
        for i in range(1, len(sys.argv)):
            try:
                scores.append(int(sys.argv[i]))
            except ValueError:
                print(f"oops, I typed {sys.argv[i]} instead of a number")
        if len(scores) > 0:
            print(f"Scores processed: {scores}")
            total_players: int = len(scores)
            print(f"Total players: {total_players}")
            total: int = sum(scores)
            print(f"Total score: {total}")
            average: float = total / len(scores)
            print(f"Average score: {average}")
            high_score = max(scores)
            print(f"High score: {high_score}")
            low_score = min(scores)
            print(f"Low score: {low_score}")
            score_range: int = high_score - low_score
            print(f"Score range: {score_range}")
        else:
            print(
                "No scores provided. Usage: python3 ft_score_analytics.py "
                "<score1> <score2> .."
            )


if __name__ == "__main__":
    main()
