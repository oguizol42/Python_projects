from typing import Any, List
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    """Process Architecture of Processors"""
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        pass

    def output():
        """Output Ingested Data"""
        pass


class NumericProcessor(DataProcessor):
    """Process Numeric Datas"""
    def __init__(self, integer: int, avirgule: float, listing: list[Any]) -> None:
        pass

    # Validation des donnees
    def validate(self, data: Any) -> bool:
        """Check the Input Data"""
        pass

    # empilement des donnees si valide (appel a validate) sinon leve une erreur
    def ingest(self, data: Any) -> None:
        """Process the Input Data"""
        pass

    # sort la plus ancienne donnee stockee (FIFO)
    def output():
        """Output Ingested Data"""
        super().output()


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
    def __init__(self, dictionnary: dict(str, str)):
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