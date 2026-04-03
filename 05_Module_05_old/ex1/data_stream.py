from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union

class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """ Process a batch of data """
        pass


    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        """ Filter data based on criteria """
        if not isinstance(data_batch, list) or len(data_batch) < 1:
            empty_list: list[0] = [False]
            return empty_list
        return data_batch


    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """ Return stream statistics """
        pass

class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        """ Process a batch of data """
        self.data_batch = data_batch
        qty_reading: int = len(data_batch)
        if data_batch[0] is False:
            return "ERROR: data is not list of floats"
        return f"{qty_reading} readings processed"


    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        """ Filter data based on criteria """
        data_batch = super().filter_data(data_batch)
        if data_batch[0] is not False:
            for check in data_batch:
                if not isinstance(check, float):
                    empty_list: list[0] = [False]
                    return empty_list
        return data_batch


    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """ Return stream statistics """
        keys_list: list(str) = ["temp", "humidity", "pressure"]
        data_dict: Dict = {}
        for n in range(len(keys_list)):
            data_dict[keys_list[n]] = " not provided"
        if self.data_batch[0] is not False:
            n = 0
            for data in self.data_batch:
                data_dict[keys_list[n]] = data
                n += 1
        return data_dict


    @staticmethod
    def print_caracteristics(stats: Dict, result: str):
        """Display Results"""
        if isinstance(stats, dict):
            keys_list: List = [key for key in stats.keys()]
            print(f"Processing sensor batch: [", end="")
            for key in keys_list:
                if key == keys_list[0]:
                    print(f"{key}:{stats[key]}", end = "")
                else:
                    print(f", {key}:{stats[key]}", end = "")
            print("]")
            print(f"Sensor analysis: {result}", end="")
            if isinstance(stats[keys_list[0]], float):
                print(f", avg {keys_list[0]}: {stats[keys_list[0]]}°C")
            print()


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        """ Process a batch of data """
        pass


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        """ Process a batch of data """
        pass

class StreamProcessor():
    """Manage Data Processing"""
    # Recupere en entree batch de donnees et Stream
    def __init__(self, stream_process: Any, data_batch: List[Any]) -> None:
        self.stream_process = stream_process
    # Filtres les donnees recus:
        self.data: Any = self.stream_process.filter_data(data_batch, "")
    # Traite les donnes et retourne la chaine de caractere correspondant a l'affichage:
        self.result_str: str = self.stream_process.process_batch(self.data)
    # Range chaque données utiles dans un dictionnaire:
        self.stream_stat: Dict = self.stream_process.get_stats()


def main() -> None:
    """=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ==="""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    try:   
        # creation des batch de donnees
        data_batch = [22.5, 65.0, 1013.0]
        # data_batch = [22.5, 65.0]
        # creation de chaque instances de Stream
        stream_process = SensorStream()
        # Confie l'orchestration du traitement des donnes via les methode de stream a StreamProcessor
        management = StreamProcessor(stream_process, data_batch)
        # Affichage du resultat
        print("Initializing Sensor Stream...")
        print("Stream ID: SENSOR_001, Type: Environmental Data")
        SensorStream().print_caracteristics(management.stream_stat, management.result_str)
    except NameError as e:
        print(e)


if __name__ == "__main__":
    main()
# === CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

# Initializing Sensor Stream...
# Stream ID: SENSOR_001, Type: Environmental Data
# Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
# Sensor analysis: 3 readings processed, avg temp: 22.5°C

# Initializing Transaction Stream...
# Stream ID: TRANS_001, Type: Financial Data
# Processing transaction batch: [buy:100, sell:150, buy:75]
# Transaction analysis: 3 operations, net flow: +25 units

# Initializing Event Stream...
# Stream ID: EVENT_001, Type: System Events
# Processing event batch: [login, error, logout]
# Event analysis: 3 events, 1 error detected

# === Polymorphic Stream Processing ===
# Processing mixed stream types through unified interface...

# Batch 1 Results:
# - Sensor data: 2 readings processed
# - Transaction data: 4 operations processed
# - Event data: 3 events processed

# Stream filtering active: High-priority data only
# Filtered results: 2 critical sensor alerts, 1 large transaction

# All streams processed successfully. Nexus throughput optimal.