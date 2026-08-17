from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.id_generator import generate_id
from app.models.string_id_base import StringIDBaseModel


class Achievement(StringIDBaseModel):
    __tablename__ = "achievements"

    id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
        index=True,
        default=lambda: generate_id("ach"),
    )

    resume_id: Mapped[str] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    issuer: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    achievement_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resume: Mapped["Resume"] = relationship(
        "Resume",
        back_populates="achievements",
    )

    def __repr__(self) -> str:
        return (
            f"<Achievement(id='{self.id}', "
            f"title='{self.title}')>"
        )