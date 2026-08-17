from sqlalchemy.orm import Session

from app.common.base_service import BaseResumeService
from app.models.skill import Skill
from app.models.user import User
from app.skill.schemas import (
    SkillCreate,
    SkillUpdate,
)


class SkillService(BaseResumeService):

    model = Skill
    entity_name = "Skill"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: SkillCreate,
    ) -> Skill:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.create_entity(
            db=db,
            resume=resume,
            data=cls.request_data(request),
        )

    @classmethod
    def list(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
    ) -> list[Skill]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Skill.created_at,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        skill_id: str,
        request: SkillUpdate,
    ) -> Skill:

        skill = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=skill_id,
        )

        return cls.update_entity(
            db=db,
            entity=skill,
            data=cls.request_data(
                request,
                exclude_unset=True,
            ),
        )

    @classmethod
    def delete(
        cls,
        db: Session,
        current_user: User,
        skill_id: str,
    ) -> None:

        skill = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=skill_id,
        )

        cls.delete_entity(
            db=db,
            entity=skill,
        )