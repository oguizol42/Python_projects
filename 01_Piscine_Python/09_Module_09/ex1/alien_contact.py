from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def custom_validation(self) -> "AlienContact":
        if not (self.contact_id[0] == "A" and self.contact_id[1] == "C"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if (
            self.contact_type == ContactType.physical
            and self.is_verified is False
        ):
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main() -> None:
    try:
        valid_alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )
        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")
        print(f"ID: {valid_alien_contact.contact_id}")
        print(f"Type: {valid_alien_contact.contact_type}")
        print(f"Location: {valid_alien_contact.location}")
        print(f"Signal: {valid_alien_contact.signal_strength}/10")
        print(f"Duration: {valid_alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_alien_contact.witness_count}")
        print(f"Message: '{valid_alien_contact.message_received}'")
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        print()
        print("======================================")
        print("Expected validation error:")
        invalid_alien_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
        )
        print(f"ID: {invalid_alien_contact.contact_id}")
        print(f"Type: {invalid_alien_contact.contact_type}")
        print(f"Location: {invalid_alien_contact.location}")
        print(f"Signal: {invalid_alien_contact.signal_strength}/10")
        print(f"Duration: {invalid_alien_contact.duration_minutes} minutes")
        print(f"Witnesses: {invalid_alien_contact.witness_count}")
        print(f"Message: '{invalid_alien_contact.message_received}'")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
