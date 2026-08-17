from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class ExperienceCreate(BaseModel):
    company: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    position: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    employment_type: str | None = None
    location: str | None = None

    start_date: date
    end_date: date | None = None

    is_current: bool = False

    description: str | None = None


class ExperienceUpdate(BaseModel):
    company: str | None = None
    position: str | None = None

    employment_type: str | None = None
    location: str | None = None

    start_date: date | None = None
    end_date: date | None = None

    is_current: bool | None = None

    description: str | None = None


class ExperienceResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str
    resume_id: str

    company: str
    position: str

    employment_type: str | None
    location: str | None

    start_date: date
    end_date: date | None

    is_current: bool

    description: str | None