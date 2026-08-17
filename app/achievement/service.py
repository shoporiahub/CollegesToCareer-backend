from sqlalchemy.orm import Session

from app.achievement.schemas import (
    AchievementCreate,
    AchievementUpdate,
)
from app.common.base_service import BaseResumeService
from app.models.achievement import Achievement
from app.models.user import User


class AchievementService(BaseResumeService):

    model = Achievement
    entity_name = "Achievement"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: AchievementCreate,
    ) -> Achievement:

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
    ) -> list[Achievement]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Achievement.achievement_date,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        achievement_id: str,
        request: AchievementUpdate,
    ) -> Achievement:

        achievement = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=achievement_id,
        )

        return cls.update_entity(
            db=db,
            entity=achievement,
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
        achievement_id: str,
    ) -> None:

        achievement = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=achievement_id,
        )

        cls.delete_entity(
            db=db,
            entity=achievement,
        )