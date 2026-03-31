from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Basic Class of Data Processor"""

    @abstractmethod
    def process():
        pass

    @abstractmethod
    def validate():
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    """Processing Numeric Values"""

    def __init__(self, data: Any) -> None:
        self.data = data

    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            check: int
            if not isinstance(data, List):
                raise TypeError("ERROR: Data is not correct")
            for check in data:
                if not isinstance(check, int):
                    raise TypeError("ERROR: Data is not correct")
            print("Validation: Numeric data verified")
            return True
        except TypeError as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        print(super().format_output(result), end="")
        sum_datas: int = sum(self.data)
        qty_datas: int = len(self.data)
        average_datas: float = round(sum_datas / qty_datas, 1)
        return (
            f"Processed {qty_datas} numeric values, sum={sum_datas},"
            f" avg={average_datas}"
        )


class TextProcessor(DataProcessor):
    """Processing Text Values"""

    def __init__(self, data) -> None:
        self.data = data

    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise TypeError("ERROR: Data is not correct")
            self.data = str(data)
            print("Validation: Text data verified")
            return True
        except TypeError as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        print(super().format_output(result), end="")
        size_string: int = len(self.data)
        qty_words: int = len(self.data.split())
        return f"Processed text: {size_string} characters, {qty_words} words"


class LogProcessor(DataProcessor):
    """Processing Log Values"""

    def __init__(self, data) -> None:
        self.data: Dict = data

    def process(self, data: Any) -> str:
        for key_str, value_str in data.items():
            pass
        return f"Processing data: {key_str}: {value_str}"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise TypeError("ERROR: Data is not correct")
            self.data = str(data)
            print("Validation: Text data verified")
            return True
        except TypeError as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        print(super().format_output(result), end="")
        size_string: int = len(self.data)
        qty_words: int = len(self.data.split())
        return f"Processed text: {size_string} characters, {qty_words} words"


def main():
    """CODE NEXUS - DATA PROCESSOR FOUNDATION"""
    data_process: Optional[any] = None
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    try:
        data_process = NumericProcessor([1, 2, 3, 4, 5])
    except NameError as e:
        print(e)
        return 1
    print(data_process.process(data_process.data))
    if data_process.validate(data_process.data) is True:
        print(data_process.format_output("Output: "))
    print()

    print("Initializing Text Processor...")
    try:
        data_process = TextProcessor("Hello Nexus World")
    except NameError as e:
        print(e)
        return 1
    print(data_process.process(data_process.data))
    if data_process.validate(data_process.data) is True:
        print(data_process.format_output("Output: "))
    print()

    print("Initializing Log Processor...")
    try:
        data_process = LogProcessor({"ERROR": "Connection timeout"})
    except NameError as e:
        print(e)
        return 1
    print(data_process.process(data_process.data))
    # if data_process.validate(data_process.data) is True:
    #     print(data_process.format_output("Output: "))
    print()

    # Initializing Log Processor...


# Processing data: "ERROR: Connection timeout"
# Validation: Log entry verified
# Output: [ALERT] ERROR level detected: Connection timeout


if __name__ == "__main__":
    main()


# $> python3 stream_processor.py
# === CODE NEXUS - DATA PROCESSOR FOUNDATION ===

# Initializing Numeric Processor...
# Processing data: [1, 2, 3, 4, 5]
# Validation: Numeric data verified
# Output: Processed 5 numeric values, sum=15, avg=3.0

# Initializing Text Processor...
# Processing data: "Hello Nexus World"
# Validation: Text data verified
# Output: Processed text: 17 characters, 3 words

# Initializing Log Processor...
# Processing data: "ERROR: Connection timeout"
# Validation: Log entry verified
# Output: [ALERT] ERROR level detected: Connection timeout

# === Polymorphic Processing Demo ===

# Code Nexus Polymorphic Data Streams in the Digital Matrix
# Processing multiple data types through same interface...
# Result 1: Processed 3 numeric values, sum=6, avg=2.0
# Result 2: Processed text: 12 characters, 2 words
# Result 3: [INFO] INFO level detected: System ready

# Foundation systems online. Nexus ready for advanced streams.
