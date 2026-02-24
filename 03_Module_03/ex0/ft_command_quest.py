import sys


def main() -> None:
    """take Users Arguments"""
    argc = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if argc == 1:
        print("No arguments provided!")
    else:
        for i in range(1, argc):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
