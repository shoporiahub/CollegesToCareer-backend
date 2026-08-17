from sqlalchemy.orm import Session

from app.common.base_service import BaseResumeService
from app.language.schemas import (
    LanguageCreate,
    LanguageUpdate,
)
from app.models.language import Language
from app.models.user import User


class LanguageService(BaseResumeService):

    model = Language
    entity_name = "Language"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: LanguageCreate,
    ) -> Language:

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
    ) -> list[Language]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Language.created_at,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        language_id: str,
        request: LanguageUpdate,
    ) -> Language:

        language = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=language_id,
        )

        return cls.update_entity(
            db=db,
            entity=language,
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
        language_id: str,
    ) -> None:

        language = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=language_id,
        )

        cls.delete_entity(
            db=db,
            entity=language,
        )