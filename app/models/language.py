from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.id_generator import generate_id
from app.models.string_id_base import StringIDBaseModel


class Language(StringIDBaseModel):
    __tablename__ = "languages"

    id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
        index=True,
        default=lambda: generate_id("lang"),
    )

    resume_id: Mapped[str] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    proficiency: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    resume: Mapped["Resume"] = relationship(
        "Resume",
        back_populates="languages",
    )

    def __repr__(self) -> str:
        return (
            f"<Language(id='{self.id}', "
            f"name='{self.name}')>"
        )