from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        print("Space Station Data Validation")
        print("========================================")
        valid_space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
        print("Valid station created:")
        print(f"ID: {valid_space_station.station_id}")
        print(f"Name: {valid_space_station.name}")
        print(f"Crew: {valid_space_station.crew_size} people")
        print(f"Power: {valid_space_station.power_level}%")
        print(f"Oxygen: {valid_space_station.oxygen_level}%")
        print("Status: Operational")
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        print("\n========================================")
        print("Expected validation error:")
        invalid_space_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=26,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
        print("\nUnvalid station created:")
        print(f"ID: {invalid_space_station.station_id}")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
