from pydantic import BaseModel, ConfigDict, Field


class LanguageCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    proficiency: str = Field(
        ...,
        max_length=50,
    )


class LanguageUpdate(BaseModel):
    name: str | None = None

    proficiency: str | None = None


class LanguageResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    resume_id: str

    name: str

    proficiency: str