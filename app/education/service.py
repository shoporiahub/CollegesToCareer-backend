from sqlalchemy.orm import Session

from app.common.base_service import BaseResumeService
from app.education.schemas import (
    EducationCreate,
    EducationUpdate,
)
from app.models.education import Education
from app.models.user import User


class EducationService(BaseResumeService):

    model = Education
    entity_name = "Education"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: EducationCreate,
    ) -> Education:

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
    ) -> list[Education]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Education.start_date,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        education_id: str,
        request: EducationUpdate,
    ) -> Education:

        education = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=education_id,
        )

        return cls.update_entity(
            db=db,
            entity=education,
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
        education_id: str,
    ) -> None:

        education = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=education_id,
        )

        cls.delete_entity(
            db=db,
            entity=education,
        )