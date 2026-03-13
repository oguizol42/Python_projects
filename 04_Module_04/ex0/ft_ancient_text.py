def main() -> None:
    """Read an Ancient Fragment"""
    file_name: str = "ancient_fragment.txt"
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print()
        old_document = open(file_name, "r")
        old_document.close()
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...")
    except FileNotFoundError:
        print("You stupid idiot, don't you know that this file doesn't exist ?")

if __name__ == "__main__":
    main()


# $> python3 ft_ancient_text.py
# === CYBER ARCHIVES - DATA RECOVERY SYSTEM ===

# Accessing Storage Vault: ancient_fragment.txt
# Connection established...

# RECOVERED DATA:
# [FRAGMENT 001] Digital preservation protocols established 2087
# [FRAGMENT 002] Knowledge must survive the entropy wars
# [FRAGMENT 003] Every byte saved is a victory against oblivion

# Data recovery complete. Storage unit disconnected