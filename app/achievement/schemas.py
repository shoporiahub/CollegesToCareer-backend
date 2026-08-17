from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class AchievementCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    issuer: str | None = None

    achievement_date: date | None = None

    description: str | None = None


class AchievementUpdate(BaseModel):
    title: str | None = None

    issuer: str | None = None

    achievement_date: date | None = None

    description: str | None = None


class AchievementResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    resume_id: str

    title: str

    issuer: str | None

    achievement_date: date | None

    description: str | None