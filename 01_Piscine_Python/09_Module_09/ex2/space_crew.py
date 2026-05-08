from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validation_rules(self) -> "SpaceMission":
        command_or_captain: bool = False
        experienced_count: int = 0
        if not self.mission_id[0] == "M":
            raise ValueError('Mission ID must start with "M"')
        for member in self.crew:
            if member.rank in (Rank.commander, Rank.captain):
                command_or_captain = True
            if member.years_experience > 5:
                experienced_count += 1
            if member.is_active is False:
                raise ValueError("All crew members must be active")
        if command_or_captain is False:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365 and experienced_count < len(self.crew) / 2:
            raise ValueError(
                "Long missions (> 365 days) "
                "need 50% experienced crew (5+ years)"
                )
        return self


def main() -> None:
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        crew_member: list[CrewMember] = [
            CrewMember(
                member_id="SC35MC",
                name="Sarah Connor",
                rank=Rank.commander,
                age=45,
                specialization="Mission Command",
                years_experience=25
            ),
            CrewMember(
                member_id="JS25N",
                name="John Smith",
                rank=Rank.lieutenant,
                age=25,
                specialization="Navigation",
                years_experience=6
            ),
            CrewMember(
                member_id="AJ27E",
                name="Alice Johnson",
                rank=Rank.officer,
                age=27,
                specialization="Engineering",
                years_experience=7
            )
        ]
        valid_mission = SpaceMission(
                            mission_id="M2024_MARS",
                            mission_name="Mars Colony Establishment",
                            destination="Mars",
                            launch_date=datetime.now(),
                            duration_days=900,
                            crew=crew_member,
                            budget_millions=2500.0
                        )
        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")
        for member in valid_mission.crew:
            print(f"- {member.name} ({member.rank})- {member.specialization}")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
    try:
        print("\n=========================================")
        print("Expected validation error:")
        crew_member2: list[CrewMember] = [
            CrewMember(
                member_id="SC35HIC",
                name="Sarah Croche",
                rank=Rank.cadet,
                age=45,
                specialization="Household Ironing Cooking",
                years_experience=25
            ),
            CrewMember(
                member_id="JS25N",
                name="John Smith",
                rank=Rank.lieutenant,
                age=25,
                specialization="Navigation",
                years_experience=6
            ),
            CrewMember(
                member_id="AJ27E",
                name="Alice Johnson",
                rank=Rank.officer,
                age=27,
                specialization="Engineering",
                years_experience=7
            )
        ]
        invalid_mission = SpaceMission(
                            mission_id="M2025_AVRIL",
                            mission_name="I Don t Know",
                            destination="Nowhere",
                            launch_date=datetime.now(),
                            duration_days=900,
                            crew=crew_member2,
                            budget_millions=50.0
                        )
        print(f"Mission: {invalid_mission.mission_name}")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
