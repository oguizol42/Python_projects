from typing import Any, List, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Process Architecture of Processors"""

    # Validation des donnees
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        pass

    # empilement des donnees si valide (appel a validate) sinon leve une erreur
    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        pass

    # sort la plus ancienne donnee stockee (FIFO)
    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        output_str: str
        if len(self.stack_numeric) > 0:
            self.rank += 1
            output_str = self.stack_numeric.pop(0)
            return self.rank, output_str
        raise IndexError("The stack is empty or is not exist")


class NumericProcessor(DataProcessor):
    """Process Numeric Datas"""

    def __init__(self):
        # self.stack_list: list = [Union(int, float, list(Union(int, float)))]
        self.stack_numeric: list = []
        self.rank: int = -1

    # Validation des donnees
    # ingests int, float, and lists of both types (includingmixed-type lists)
    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        if not isinstance(data, int):
            if not isinstance(data, float):
                if not isinstance(data, list):
                    return False
        if isinstance(data, list):
            for check in data:
                if not isinstance(check, int):
                    if not isinstance(check, float):
                        return False
        return True

    # empilement des donnees si valide (appel a validate) sinon leve une erreur
    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        if self.validate(data) is False:
            if isinstance(data, str):
                raise ValueError("Invalide Data")
        self.stack_numeric.append(str(data))

    # sort la plus ancienne donnee stockee (FIFO)
    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        return super().output()


class TextProcessor(DataProcessor):
    """Process String Datas"""

    def __init__(self, string: str, string_list: list[str]) -> None:
        pass

    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        pass

    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        pass

    def output():
        """Output Ingested Data"""
        pass


class LogProcessor(DataProcessor):
    """Process Log Datas"""

    def __init__(self, dictionnary: dict[str, str]):
        pass

    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        pass

    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        pass

    def output():
        """Output Ingested Data"""
        pass


def main() -> None:
    """Code Nexus - Data Processor"""
    instance_test: any
    rank: int
    value_txt: str
    print("=== Code Nexus - Data Processor ===\n")

    try:
        try:
            print("Testing Numeric Processor...")
            instance_test = NumericProcessor()
            instance_test.ingest(1)
            instance_test.ingest(2)
            instance_test.ingest(3)
            print(
                f"Trying to validate input '42': {instance_test.validate(42)}"
            )
            print(
                "Trying to validate input 'Hello': "
                f"{instance_test.validate('Hello')}"
            )
            print(
                "Test invalid ingestion of string 'foo'"
                " without prior validation:"
            )
            instance_test.ingest("foo")
        except ValueError:
            print("Got exception: Improper numeric data")
        try:
            print("Processing data: [1, 2, 3, 4, 5]")
            print("Extracting 3 values...")
            for n in range(3):
                rank, value_txt = instance_test.output()
                print(f"Numeric value {rank}: {value_txt}")
        except ValueError as e:
            print(e)

    except NameError as e:
        print(e)
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()


# === Code Nexus - Data Processor ===

# Testing Numeric Processor...
# Trying to validate input '42': True
# Trying to validate input 'Hello': False
# Test invalid ingestion of string 'foo' without prior validation:
# Got exception: Improper numeric data
# Processing data: [1, 2, 3, 4, 5]
# Extracting 3 values...
# Numeric value 0: 1
# Numeric value 1: 2
# Numeric value 2: 3

# Testing Text Processor...
# Trying to validate input '42': False
# Processing data: ['Hello', 'Nexus', 'World']
# Extracting 1 value...
# Text value 0: Hello

# Testing Log Processor...
# Trying to validate input 'Hello': False
# Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR
# ', 'log_message': 'Unauthorized access!!'}]
# Extracting 2 values...
# Log entry 0: NOTICE: Connection to server
# Log entry 1: ERROR: Unauthorized access!!
