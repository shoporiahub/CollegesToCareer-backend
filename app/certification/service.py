from sqlalchemy.orm import Session

from app.certification.schemas import (
    CertificationCreate,
    CertificationUpdate,
)
from app.common.base_service import BaseResumeService
from app.models.certification import Certification
from app.models.user import User


class CertificationService(BaseResumeService):

    model = Certification
    entity_name = "Certification"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: CertificationCreate,
    ) -> Certification:

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
    ) -> list[Certification]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Certification.issue_date,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        certification_id: str,
        request: CertificationUpdate,
    ) -> Certification:

        certification = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=certification_id,
        )

        return cls.update_entity(
            db=db,
            entity=certification,
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
        certification_id: str,
    ) -> None:

        certification = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=certification_id,
        )

        cls.delete_entity(
            db=db,
            entity=certification,
        )