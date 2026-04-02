from typing import Any, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Basic Class of Data Processor"""

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    """Processing Numeric Values"""

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            self.sum_datas: int = sum(data)
            self.qty_datas: int = len(data)
            self.average_datas: float = round(
                self.sum_datas / self.qty_datas, 1
            )
            return (
                f"Processing data: {data}\n"
                "Validation: Numeric data verified\n"
                f"{self.format_output('Output: ')}"
            )

        else:
            return ""

    def validate(self, data: Any) -> bool:
        try:
            check: int
            if not isinstance(data, list):
                raise TypeError("ERROR: Data is not correct")
            for check in data:
                if not isinstance(check, int):
                    raise TypeError("ERROR: Data is not list of numbers")
            return True
        except TypeError as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        return (
            f"{super().format_output(result)}"
            f"Processed {self.qty_datas} numeric values, sum={self.sum_datas},"
            f" avg={self.average_datas}"
        )


class TextProcessor(DataProcessor):
    """Processing Text Values"""

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            self.size_string: int = len(data)
            self.qty_words: int = len(data.split())
            return (
                f'Processing data: "{data}"\n'
                "Validation: Text data verified\n"
                f"{self.format_output('Output: ')}"
            )

        else:
            return ""

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise TypeError("ERROR: Data is not text")
            return True
        except TypeError as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        return (
            f"{super().format_output(result)}"
            f"Processed text: {self.size_string} characters, "
            f"{self.qty_words} words"
        )


class LogProcessor(DataProcessor):
    """Processing Log Values"""

    def process(self, data: Any) -> str:
        if self.validate(data) is True:
            self.key_str = data[0]
            self.value_str = data[1]
            if self.key_str == "ERROR":
                self.result: str = "[ALERT] "
            elif self.key_str == "INFO":
                self.result: str = "[INFO] "
            return (
                f'Processing data: "{self.key_str}: {self.value_str}"\n'
                "Validation: Log entry verified\n"
                f'{self.format_output("Output: ")}'
            )
        else:
            return ""

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, tuple):
                raise TypeError("ERROR: Data is not tuple")
            elif len(data) != 2:
                raise ValueError("ERROR: Data is not tuple of two strings")
            elif not isinstance(data[0], str) or not isinstance(data[1], str):
                raise ValueError("ERROR: Data is not tuple of two strings")

            return True
        except (TypeError, ValueError) as e:
            print(e)
            return False

    def format_output(self, result: str) -> str:
        return (
            f"{super().format_output(result)}{self.result}{self.key_str} "
            f"level detected: {self.value_str}"
        )


def main() -> None:
    """CODE NEXUS - DATA PROCESSOR FOUNDATION"""
    data_process: Optional[Any] = None
    object_list: list[Any] = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello Babies"),
        (LogProcessor(), ("INFO", "System ready")),
    ]
    n: int = 1
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    try:
        data_process = NumericProcessor()
        print(data_process.process([1, 2, 3, 4, 5]))
    except NameError as e:
        print(e)

    print("\nInitializing Text Processor...")
    try:
        data_process = TextProcessor()
        print(data_process.process("Hello Nexus World"))
    except NameError as e:
        print(e)

    print("\nInitializing Log Processor...")
    try:
        data_process = LogProcessor()
        print(data_process.process(("ERROR", "Connection timeout")))
    except NameError as e:
        print(e)
        return 1

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    for object, arg_object in object_list:
        print(f"Result {n}: ", end="")
        object.process(arg_object)
        print(object.format_output(""))
        n += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
