from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class EducationCreate(BaseModel):
    institution: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    degree: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    field_of_study: str | None = None

    start_date: date
    end_date: date | None = None

    grade: str | None = None
    description: str | None = None


class EducationUpdate(BaseModel):
    institution: str | None = None
    degree: str | None = None

    field_of_study: str | None = None

    start_date: date | None = None
    end_date: date | None = None

    grade: str | None = None
    description: str | None = None


class EducationResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    resume_id: str

    institution: str
    degree: str

    field_of_study: str | None

    start_date: date
    end_date: date | None

    grade: str | None
    description: str | None