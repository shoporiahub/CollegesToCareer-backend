from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.id_generator import generate_id
from app.models.string_id_base import StringIDBaseModel


class Experience(StringIDBaseModel):
    __tablename__ = "experiences"

    id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
        index=True,
        default=lambda: generate_id("exp"),
    )

    resume_id: Mapped[str] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    company: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    position: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
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

    is_current: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    resume: Mapped["Resume"] = relationship(
        "Resume",
        back_populates="experiences",
    )

    def __repr__(self) -> str:
        return (
            f"<Experience(id='{self.id}', "
            f"company='{self.company}', "
            f"position='{self.position}')>"
        )