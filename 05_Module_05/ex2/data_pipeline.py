import typing
from typing import Any, Union, Protocol
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Process Architecture of Processors"""
    def __init__(self):
        self.stack_datas: list[str] = []
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
            if 'log_level' not in data:
                return False
            if 'log_message' not in data:
                return False
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
                if key != 'log_level' and key != 'log_message':
                    return False
        elif isinstance(data, list):
            for one_data in data:
                if not isinstance(one_data, dict):
                    return False
                if 'log_level' not in one_data:
                    return False
                if 'log_message' not in one_data:
                    return False
                for key, value in one_data.items():
                    if not isinstance(key, str):
                        return False
                    if not isinstance(value, str):
                        return False
                    if key != 'log_level' and key != 'log_message':
                        return False
        else:
            return False
        return True

    def ingest(
        self, data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        """Process the Input Data"""
        value1: str
        value2: str
        if self.validate(data) is False:
            raise ValueError("Got exception: Improper dictionary data")
        if isinstance(data, list):
            for extract in data:
                for key, value in extract.items():
                    if key == 'log_level':
                        value1 = value
                    else:
                        value2 = value
                self.stack_datas.append(str(f"{value1}: {value2}"))
        else:
            for key, value in data.items():
                if key == 'log_level':
                    value1 = value
                else:
                    value2 = value
            self.stack_datas.append(str(f"{value1}: {value2}"))

    def output(self) -> tuple[int, str]:
        """Output Ingested Data"""
        return super().output()


class ExportPlugin(Protocol):
    """Protocols of Plugins"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin():
    """Print str on CSV format"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        cnt: int
        cnt = 0
        if isinstance(data, list):
            for one_data in data:
                if cnt > 0:
                    print(",", end ="")
                print(f"{one_data[1]}", end="")
                cnt += 1
    
class JSONPlugin():
    """Print str on JSON format"""
    def process_output(self, data: list[tuple[int, str]]) -> None:
        cnt: int
        cnt = 0
        if isinstance(data, list):
            print("{", end ="")
            for one_data in data:
                if cnt > 0:
                    print(", ", end ="")
                print(f'"item_{one_data[0]}": "{one_data[1]}"', end="")
                cnt += 1
            print("}", end ="")


class DataStream():
    """Process Stream Data"""

    def __init__(self) -> None:
        self.stack_instance: list[typing.Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Add DataProcessor Instance to the Stack"""
        if isinstance(proc, DataProcessor):
            self.stack_instance.append(proc)
        else:
            print(f"Error: {proc} is not a valid DataProcessor")

    def process_stream(self, stream: list[typing.Any]) -> None:
        """Send Datas to the Appropriate Instance"""
        check: bool
        if len(self.stack_instance) == 0 or len(stream) == 0:
            print("No processor found, no data")
        else:
            for data in stream:
                check = False
                for process in self.stack_instance:
                    if process.validate(data):
                        process.ingest(data)
                        check = True
                        break
                if check is False:
                    print(
                        "DataStream error - "
                        f"Can't process element in stream: {data}"
                    )

    def print_processors_stats(self) -> None:
        """Print Instances Statistics"""
        qty_processed: int
        qty_remained: int
        text: str
        print("== DataStream statistics ==")
        if len(self.stack_instance) > 0:
            for process in self.stack_instance:
                qty_remained = len(process.stack_datas)
                qty_processed = qty_remained + process.rank + 1
                text = process.__class__.__name__
                text = text.replace("Processor", " Processor")
                print(
                    f'{text}'
                    f": total {qty_processed} items processed,"
                    f" remaining {qty_remained} on processor"
                )
        else:
            print("ERROR: no instance registered")
    
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume nb Elements from Output of DataProcessor's Output and Print on Pluggin mode"""
        data_tuple: list[tuple[int, str]] = []
        loop: int = 0
        for instance in self.stack_instance:
            loop = len(instance.stack_datas)
            if loop > 0:
                if loop > nb:
                    loop = nb
                for _ in range(loop):
                    data_tuple.append(instance.output())
                if isinstance(plugin, CSVPlugin):
                    print("\nCSV Output:")
                elif isinstance(plugin, JSONPlugin):
                    print("\nJSON Output:")
                plugin.process_output(data_tuple)
                data_tuple = []
            

    def scenario_test(self) -> None:
        """Test Cases of DataStream"""
        numeric_process = NumericProcessor()
        text_process = TextProcessor()
        log_process = LogProcessor()
        print("=== Code Nexus - Data Stream ===\n")
        print("Initialize Data Stream...")
        try:
            self.process_stream([1, 'a'])
            print("Registering Numeric Processor\n")
            self.register_processor(numeric_process)
            print(
                "Send first batch of data on stream: ['Hello world', "
                "[3.14, -1, 2.71], [{'log_level': 'WARNING', '\n"
                "      log_message': 'Telnet access! Use ssh instead'}, "
                "{'log_level': 'INFO', 'log_message': 'User wil is\n"
                "      connected'}], 42, ['Hi', 'five']]"
            )
            self.process_stream(
                [
                    'Hello world', [3.14, -1, 2.71],
                    [
                        {
                            'log_level': 'WARNING',
                            'log_message': 'Telnet access! Use ssh instead'
                        },
                        {
                            'log_level': 'INFO',
                            'log_message': 'User wil is connected'
                        }
                    ],
                    42, ['Hi', 'five']
                ]
            )
            self.print_processors_stats()
            print("\nRegistering other data processors")
            self.register_processor(text_process)
            self.register_processor(log_process)
            print("Send the same batch again")
            self.process_stream(
                [
                    'Hello world', [3.14, -1, 2.71],
                    [
                        {
                            'log_level': 'WARNING',
                            'log_message': 'Telnet access! Use ssh instead'
                        },
                        {
                            'log_level': 'INFO',
                            'log_message': 'User wil is connected'
                        }
                    ],
                    42, ['Hi', 'five']
                ]
            )
            self.print_processors_stats()
            print(
                "\nConsume some elements from the data processors:"
                " Numeric 3, Text 2, Log 1"
            )
            numeric_process.output()
            numeric_process.output()
            numeric_process.output()
            text_process.output()
            text_process.output()
            log_process.output()
            self.print_processors_stats()
        except NameError as e:
            print(e)
        except IndexError as e:
            print(e)

    def scenario_test_pipeline(self) -> None:
        """Test Cases of DataStream"""
        numeric_process = NumericProcessor()
        text_process = TextProcessor()
        log_process = LogProcessor()
        csv_plugin = CSVPlugin()
        json_plugin = JSONPlugin()
        print("=== Code Nexus - Data Pipeline ===\n")
        print("Initialize Data Stream...")
        try:
            print("\n== DataStream statistics ==")
            self.process_stream([1, 'a'])
            print("\nRegistering Processors\n")
            self.register_processor(numeric_process)
            self.register_processor(text_process)
            self.register_processor(log_process)
            print(
                "Send first batch of data on stream: ['Hello world', "
                "[3.14, -1, 2.71], [{'log_level': 'WARNING', '\n"
                "      log_message': 'Telnet access! Use ssh instead'}, "
                "{'log_level': 'INFO', 'log_message': 'User wil is\n"
                "      connected'}], 42, ['Hi', 'five']]"
            )
            self.process_stream(
                [
                    'Hello world', [3.14, -1, 2.71],
                    [
                        {
                            'log_level': 'WARNING',
                            'log_message': 'Telnet access! Use ssh instead'
                        },
                        {
                            'log_level': 'INFO',
                            'log_message': 'User wil is connected'
                        }
                    ],
                    42, ['Hi', 'five']
                ]
            )
            print()
            self.print_processors_stats()
            print("\nSend 3 processed data from each processor to a CSV plugin:")
            self.output_pipeline(3, csv_plugin)
            print("\n")
            self.print_processors_stats()
            print(
                "Send another batch of data: [21, ['I love AI', "
                "'LLMs are wonderful', 'Stay healthy'], [{'log_level': '"
            )
            print(
                "     ERROR', 'log_message': '500 server crash'}, {'log_level':"
                " 'NOTICE', 'log_message': 'Certificate"
            )
            print("     expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']\n")
            self.process_stream(
                [
                    21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
                    [
                        {'log_level': 'ERROR', 'log_message': '500 server crash'},
                        {
                            'log_level': 'NOTICE',
                            'log_message': 'Certificate expires in 10 days'
                        }
                    ], [32, 42, 64, 84, 128, 168], 'World hello'
                ]
            )
            self.print_processors_stats()
            print("\nSend 5 processed data from each processor to a JSON plugin:")
            self.output_pipeline(5, json_plugin)
            print()
            print()
            self.print_processors_stats()        
        except NameError as e:
            print(e)
        except IndexError as e:
            print(e)


def main() -> None:
    """=== Code Nexus - Data Pipeline ==="""
    test = DataStream()
    test.scenario_test_pipeline()

if __name__ == "__main__":
    main()
