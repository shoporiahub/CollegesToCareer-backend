from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.achievement import Achievement
from app.models.certification import Certification
from app.models.education import Education
from app.models.experience import Experience
from app.models.id_generator import generate_id
from app.models.language import Language
from app.models.project import Project
from app.models.skill import Skill
from app.models.string_id_base import StringIDBaseModel
from app.models.template import Template
from app.models.user import User


class Resume(StringIDBaseModel):
    __tablename__ = "resumes"

    id: Mapped[str] = mapped_column(
        String(30),
        primary_key=True,
        index=True,
        default=lambda: generate_id("res"),
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    headline: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    city: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    state: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    country: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    pincode: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    portfolio_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    website_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    profile_photo: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    template_id: Mapped[str] = mapped_column(
        ForeignKey(
            "templates.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
        index=True,
    )

    theme: Mapped[str] = mapped_column(
        String(50),
        default="blue",
        nullable=False,
    )

    font: Mapped[str] = mapped_column(
        String(50),
        default="inter",
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="draft",
        nullable=False,
        index=True,
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True,
    )

    user: Mapped["User"] = relationship(
        "User",
        back_populates="resumes",
    )

    template: Mapped["Template"] = relationship(
        "Template",
    )

    educations: Mapped[list["Education"]] = relationship(
        "Education",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    experiences: Mapped[list["Experience"]] = relationship(
        "Experience",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    projects: Mapped[list["Project"]] = relationship(
        "Project",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    skills: Mapped[list["Skill"]] = relationship(
        "Skill",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    certifications: Mapped[list["Certification"]] = relationship(
        "Certification",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    languages: Mapped[list["Language"]] = relationship(
        "Language",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    achievements: Mapped[list["Achievement"]] = relationship(
        "Achievement",
        back_populates="resume",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return (
            f"<Resume("
            f"id='{self.id}', "
            f"title='{self.title}', "
            f"user_id='{self.user_id}', "
            f"template_id='{self.template_id}', "
            f"status='{self.status}')>"
        )