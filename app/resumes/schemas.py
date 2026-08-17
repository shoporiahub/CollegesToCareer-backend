from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ResumeCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    email: EmailStr

    phone: str = Field(
        ...,
        min_length=8,
        max_length=20,
    )

    headline: str | None = None
    summary: str | None = None

    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    pincode: str | None = None

    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None
    website_url: str | None = None

    profile_photo: str | None = None

    # Selected template
    template_id: str

    theme: str = "blue"
    font: str = "inter"

    is_default: bool = False


class ResumeUpdate(BaseModel):
    title: str | None = None

    first_name: str | None = None
    last_name: str | None = None

    email: EmailStr | None = None
    phone: str | None = None

    headline: str | None = None
    summary: str | None = None

    address: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    pincode: str | None = None

    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None
    website_url: str | None = None

    profile_photo: str | None = None

    # User can change the selected template
    template_id: str | None = None

    theme: str | None = None
    font: str | None = None

    is_default: bool | None = None


class ResumeResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    # Resume ID is now a generated string
    id: str

    title: str

    first_name: str
    last_name: str

    email: EmailStr
    phone: str

    headline: str | None
    summary: str | None

    address: str | None
    city: str | None
    state: str | None
    country: str | None
    pincode: str | None

    linkedin_url: str | None
    github_url: str | None
    portfolio_url: str | None
    website_url: str | None

    profile_photo: str | None

    # Selected template
    template_id: str

    theme: str
    font: str

    status: str

    is_default: bool