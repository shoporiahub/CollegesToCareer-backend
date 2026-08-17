from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class CertificationCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    issuing_organization: str

    issue_date: date | None = None

    expiry_date: date | None = None

    credential_id: str | None = None

    credential_url: str | None = None

    description: str | None = None


class CertificationUpdate(BaseModel):
    name: str | None = None

    issuing_organization: str | None = None

    issue_date: date | None = None

    expiry_date: date | None = None

    credential_id: str | None = None

    credential_url: str | None = None

    description: str | None = None


class CertificationResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    resume_id: str

    name: str

    issuing_organization: str

    issue_date: date | None

    expiry_date: date | None

    credential_id: str | None

    credential_url: str | None

    description: str | None