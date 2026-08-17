from pydantic import ConfigDict, Field

from app.achievement.schemas import AchievementResponse
from app.certification.schemas import CertificationResponse
from app.education.schemas import EducationResponse
from app.experience.schemas import ExperienceResponse
from app.language.schemas import LanguageResponse
from app.project.schemas import ProjectResponse
from app.resumes.schemas import ResumeResponse
from app.skill.schemas import SkillResponse


class ResumeDetailResponse(ResumeResponse):

    model_config = ConfigDict(
        from_attributes=True,
    )

    educations: list[EducationResponse] = Field(
        default_factory=list,
    )

    experiences: list[ExperienceResponse] = Field(
        default_factory=list,
    )

    projects: list[ProjectResponse] = Field(
        default_factory=list,
    )

    skills: list[SkillResponse] = Field(
        default_factory=list,
    )

    certifications: list[CertificationResponse] = Field(
        default_factory=list,
    )

    languages: list[LanguageResponse] = Field(
        default_factory=list,
    )

    achievements: list[AchievementResponse] = Field(
        default_factory=list,
    )