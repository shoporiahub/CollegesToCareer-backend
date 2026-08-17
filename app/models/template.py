import secrets
import string

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


def generate_template_id() -> str:
    characters = string.ascii_letters + string.digits

    random_part = "".join(
        secrets.choice(characters)
        for _ in range(6)
    )

    return f"tpl_{random_part}"


class Template(BaseModel):
    __tablename__ = "templates"

    id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
        default=generate_template_id,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )

    image: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    template_text: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    filename: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    price: Mapped[float] = mapped_column(
        nullable=False,
        default=0,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        index=True,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    highlights: Mapped[list["TemplateHighlight"]] = relationship(
        "TemplateHighlight",
        back_populates="template",
        cascade="all, delete-orphan",
        order_by="TemplateHighlight.sort_order",
    )

    def __repr__(self) -> str:
        return (
            f"<Template("
            f"id='{self.id}', "
            f"slug='{self.slug}', "
            f"name='{self.name}')>"
        )


class TemplateHighlight(BaseModel):
    __tablename__ = "template_highlights"

    id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
        default=lambda: (
            "th_"
            + "".join(
                secrets.choice(
                    string.ascii_letters + string.digits
                )
                for _ in range(6)
            )
        ),
    )

    template_id: Mapped[str] = mapped_column(
        ForeignKey(
            "templates.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    highlight: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    sort_order: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    template: Mapped["Template"] = relationship(
        "Template",
        back_populates="highlights",
    )

    def __repr__(self) -> str:
        return (
            f"<TemplateHighlight("
            f"id='{self.id}', "
            f"template_id='{self.template_id}', "
            f"highlight='{self.highlight}')>"
        )