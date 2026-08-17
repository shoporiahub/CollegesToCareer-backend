from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class ProjectCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    organization: str | None = None

    technologies: str | None = None

    github_url: str | None = None

    live_url: str | None = None

    start_date: date | None = None

    end_date: date | None = None

    description: str | None = None


class ProjectUpdate(BaseModel):
    title: str | None = None

    organization: str | None = None

    technologies: str | None = None

    github_url: str | None = None

    live_url: str | None = None

    start_date: date | None = None

    end_date: date | None = None

    description: str | None = None


class ProjectResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    resume_id: str

    title: str

    organization: str | None

    technologies: str | None

    github_url: str | None

    live_url: str | None

    start_date: date | None

    end_date: date | None

    description: str | None