from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactCreate(BaseModel):
    full_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    subject: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    message: str = Field(
        ...,
        min_length=10,
        max_length=5000,
    )


class ContactResponse(ContactCreate):

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int

    created_at: datetime