def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0
        }
    return {
        "max_power": (max(mages, key=lambda x: x["power"]))["power"],
        "min_power": (min(mages, key=lambda x: x["power"]))["power"],
        "avg_power": round(
            (sum(map(lambda x: x["power"], mages))) / len(mages), 2
            )
    }


def main() -> None:
    list_dict_result: list[dict]
    dict_result: dict
    spells_result: list[str]

    artifacts: list[dict] = [
        {
            "name": "Crystal",
            "power": 85,
            "type": "Orb"
        },
        {
            "name": "Fire",
            "power": 92,
            "type": "Staff"
        }
    ]

    mages: list[dict] = [
        {
            "name": "Crystal",
            "power": 85,
            "element": "Orb"
        },
        {
            "name": "Fire",
            "power": 92,
            "element": "Staff"
        },
        {
            "name": "Water",
            "power": 45,
            "element": "ba"
        },
        {
            "name": "Air",
            "power": 48,
            "element": "by"
        },
        {
            "name": "Anonymous",
            "power": 50,
            "element": "bel"
        }
    ]

    spells: list[str] = [
        "fireball",
        "heal",
        "shield"
    ]

    print("Testing artifact sorter...")
    list_dict_result = artifact_sorter(artifacts)
    print(f"{list_dict_result[0]['name']} ", end="")
    print(f"{list_dict_result[0]['type']} ", end="")
    print(f"({list_dict_result[0]['power']} power) ", end="")
    print(f"comes before {list_dict_result[1]['name']} ", end="")
    print(f"{list_dict_result[1]['type']}", end="")
    print(f" ({list_dict_result[1]['power']} power)")

    print("\nTesting power_filter...")
    print(power_filter(mages, 50))

    print("\nTesting spell transformer...")
    spells_result = spell_transformer(spells)
    for spell in spells_result:
        print(f"{spell} ", end="")
    print()

    print("\nTesting mage_stats...")
    dict_result = mage_stats(mages)
    print(f"{dict_result}")


if __name__ == "__main__":
    main()
