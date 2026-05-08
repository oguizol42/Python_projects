def main() -> None:
    """Read an Ancient Fragment"""
    file_name: str = "ancient_fragment.txt"
    reading: int
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        old_document = open(file_name, "r")
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...")
        print()
        print("RECOVERED DATA:")
        reading = old_document.read()
        print(reading)

        old_document.close()
        print()
        print("Data recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print(
            "You stupid idiot, don't you know that this file doesn't exist ?"
        )


if __name__ == "__main__":
    main()
