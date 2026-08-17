from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.models.user import User


class CommonService:

    @staticmethod
    def get_user_resume(
        db: Session,
        current_user: User,
        resume_id: str,
    ) -> Resume:

        resume = (
            db.query(Resume)
            .filter(
                Resume.id == resume_id,
                Resume.user_id == current_user.id,
            )
            .first()
        )

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found.",
            )

        return resume

    @staticmethod
    def get_owned_entity(
        db: Session,
        model,
        entity_id: str,
        current_user: User,
        entity_name: str,
    ):
        entity = (
            db.query(model)
            .join(Resume)
            .filter(
                model.id == entity_id,
                Resume.user_id == current_user.id,
            )
            .first()
        )

        if entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{entity_name} not found.",
            )

        return entity