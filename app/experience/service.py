from sqlalchemy.orm import Session

from app.common.base_service import BaseResumeService
from app.experience.schemas import (
    ExperienceCreate,
    ExperienceUpdate,
)
from app.models.experience import Experience
from app.models.user import User


class ExperienceService(BaseResumeService):

    model = Experience
    entity_name = "Experience"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: ExperienceCreate,
    ) -> Experience:

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
    ) -> list[Experience]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Experience.start_date,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        experience_id: str,
        request: ExperienceUpdate,
    ) -> Experience:

        experience = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=experience_id,
        )

        return cls.update_entity(
            db=db,
            entity=experience,
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
        experience_id: str,
    ) -> None:

        experience = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=experience_id,
        )

        cls.delete_entity(
            db=db,
            entity=experience,
        )