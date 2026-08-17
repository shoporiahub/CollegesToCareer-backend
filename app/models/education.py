from datetime import date

from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.id_generator import generate_id
from app.models.string_id_base import StringIDBaseModel


class Education(StringIDBaseModel):
    __tablename__ = "educations"

    id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
        index=True,
        default=lambda: generate_id("edu"),
    )

    resume_id: Mapped[str] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    institution: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    degree: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    field_of_study: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    grade: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resume: Mapped["Resume"] = relationship(
        "Resume",
        back_populates="educations",
    )

    def __repr__(self) -> str:
        return (
            f"<Education(id='{self.id}', "
            f"institution='{self.institution}', "
            f"degree='{self.degree}')>"
        )