def main() -> None:
    """Archive Creation"""
    file_name: str = "new_discovery.txt"
    data_0: str = "[ENTRY 001] New quantum algorithm discovered\n"
    data_1: str = "[ENTRY 002] Efficiency increased by 347%\n"
    data_2: str = "[ENTRY 003] Archived by Data Archivist trainee"
    file_descriptor: int
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    try:
        file_descriptor = open(file_name, "w")
        print("Storage unit created successfully...")
        print()
        print("Inscribing preservation data...")
        print(data_0)
        file_descriptor.write(data_0)
        print(data_1)
        file_descriptor.write(data_1)
        print(data_2)
        file_descriptor.write(data_2)
        print()
        file_descriptor.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")

    except FileNotFoundError as e:
        print(e)
    pass


if __name__ == "__main__":
    main()
