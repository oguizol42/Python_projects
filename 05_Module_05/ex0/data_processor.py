from typing import Any, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Process Architecture of Processors"""
    def __init__(self):
        self.stack_datas: list = []
        self.rank: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        pass

    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        output_str: str
        if len(self.stack_datas) > 0:
            self.rank += 1
            output_str = self.stack_datas.pop(0)
            return self.rank, output_str
        raise IndexError("The stack is empty or is not exist")


class NumericProcessor(DataProcessor):
    """Process Numeric Datas"""

    def __init__(self):
        super().__init__()

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

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        """Process the Input Data"""
        if self.validate(data) is False:
            raise ValueError("Got exception: Improper numeric data")
        if isinstance(data, list):
            for extract in data:
                self.stack_datas.append(str(extract))
        else:
            self.stack_datas.append(str(data))

    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        return super().output()


class TextProcessor(DataProcessor):
    """Process String Datas"""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        if not isinstance(data, str):
            if not isinstance(data, list):
                return False
        if isinstance(data, list):
            for check in data:
                if not isinstance(check, str):
                    return False
        return True

    def ingest(self, data: Union[str, list[str]]) -> None:
        """Process the Input Data"""
        if self.validate(data) is False:
            raise ValueError("Got exception: Improper string data")
        if isinstance(data, list):
            for extract in data:
                self.stack_datas.append(str(extract))
        else:
            self.stack_datas.append(str(data))

    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        return super().output()


class LogProcessor(DataProcessor):
    """Process Log Datas"""

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
        elif isinstance(data, list):
            for one_data in data:
                if not isinstance(one_data, dict):
                    return False
                for key, value in one_data.items():
                    if not isinstance(key, str):
                        return False
                    if not isinstance(value, str):
                        return False
        else:
            return False
        return True

    def ingest(
        self, data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        """Process the Input Data"""
        cnt: int = 0
        final_string: str
        if self.validate(data) is False:
            raise ValueError("Got exception: Improper dictionary data")
        if isinstance(data, list):
            for extract in data:
                cnt = 0
                for value in extract.values():
                    if cnt == 0:
                        final_string = value
                        cnt += 1
                    else:
                        final_string += ": " + value
                self.stack_datas.append(str(final_string))
        else:
            cnt = 0
            for value in data.values():
                if cnt == 0:
                    final_string = value
                    cnt += 1
                else:
                    final_string += ": " + value
            self.stack_datas.append(str(final_string))

    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        return super().output()


def main() -> None:
    """Code Nexus - Data Processor"""
    instance_test: Any
    rank: int
    value_txt: str
    print("=== Code Nexus - Data Processor ===\n")

    try:
        try:
            print("Testing Numeric Processor...")
            instance_test = NumericProcessor()
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
            instance_test.ingest([1, 2, 3, 4, 5])
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

    try:
        try:
            print("\nTesting Text Processor...")
            instance_test = TextProcessor()
            print(
                f"Trying to validate input '42': {instance_test.validate(42)}"
            )
            print(
                "Processing data: ['Hello', 'Nexus', 'World']: "
            )
            instance_test.ingest(['Hello', 'Nexus', 'World'])
            print("Extracting 1 value...")
            rank, value_txt = instance_test.output()
            print(f"Text value {rank}: {value_txt}")
        except ValueError as e:
            print(e)
    except NameError as e:
        print(e)
    except IndexError as e:
        print(e)

    try:
        print("\nTesting Log Processor...")
        instance_test = LogProcessor()
        print(
            "Trying to validate input 'Hello': "
            f"{instance_test.validate('Hello')}"
        )
        print(
            "Processing data: [{'log_level': "
            "'NOTICE', 'log_message': 'Connection to server'}, "
            "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]: "
        )
        instance_test.ingest(
            [
                {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
            ]
        )
        print("Extracting 2 values...")
        rank, value_txt = instance_test.output()
        print(f"Text value {rank}: {value_txt}")
        rank, value_txt = instance_test.output()
        print(f"Text value {rank}: {value_txt}")
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)
    except IndexError as e:
        print(e)


if __name__ == "__main__":
    main()
