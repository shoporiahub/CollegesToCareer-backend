from pydantic import BaseModel, ConfigDict, Field


class TemplateCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=255,
    )

    slug: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    image: str = Field(
        ...,
        min_length=1,
        max_length=500,
    )

    template_text: str = Field(
        ...,
        min_length=2,
        max_length=500,
    )

    filename: str = Field(
        ...,
        min_length=1,
        max_length=500,
    )

    description: str = Field(
        ...,
        min_length=2,
    )

    price: float = Field(
        ...,
        ge=0,
    )

    highlights: list[str] = Field(
        default_factory=list,
    )

    is_active: bool = True

    sort_order: int = Field(
        default=0,
        ge=0,
    )


class TemplateUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=255,
    )

    slug: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    image: str | None = Field(
        default=None,
        min_length=1,
        max_length=500,
    )

    template_text: str | None = Field(
        default=None,
        min_length=2,
        max_length=500,
    )

    filename: str | None = Field(
        default=None,
        min_length=1,
        max_length=500,
    )

    description: str | None = Field(
        default=None,
        min_length=2,
    )

    price: float | None = Field(
        default=None,
        ge=0,
    )

    highlights: list[str] | None = None

    is_active: bool | None = None

    sort_order: int | None = Field(
        default=None,
        ge=0,
    )


class TemplateHighlightResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    template_id: str

    highlight: str

    sort_order: int


class TemplateResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: str

    name: str
    slug: str

    image: str
    template_text: str
    filename: str
    description: str

    price: float

    is_active: bool
    sort_order: int

    highlights: list[TemplateHighlightResponse]