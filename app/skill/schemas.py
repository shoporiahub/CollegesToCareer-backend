from pydantic import BaseModel, ConfigDict, Field


class SkillCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    category: str | None = None

    proficiency: str | None = None


class SkillUpdate(BaseModel):
    name: str | None = None

    category: str | None = None

    proficiency: str | None = None


class SkillResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    resume_id: str

    name: str

    category: str | None

    proficiency: str | None