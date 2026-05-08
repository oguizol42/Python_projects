class SecurePlant:
    """Security class Plant"""

    def __init__(self, name: str, height: int, age: int) -> None:
        """def Plant to securise"""
        self.__name = name
        self.__height = 0
        self.__age = 0
        if age >= 0 and height >= 0:
            print(f"Plant created: {self.__name}")
        self.set_height(height)
        if height >= 0:
            self.set_age(age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(
                f"Invalid operation attempted: height {height}cm" " [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: day {age} days [REJECTED]")
            print("Security: Negative day rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
            print()

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        """Print Plant Informations"""
        print(
            f"Current plant: {self.__name} ({self.__height}cm, "
            f"{self.__age} days)"
        )


def main() -> None:
    """=== Garden Security System ==="""
    print("=== Garden Security System ===")
    p1 = SecurePlant("Rose", 25, 30)
    SecurePlant("Oak", -5, 365)
    print()
    p1.get_info()


if __name__ == "__main__":
    main()
