from typing import Any, Type

from sqlalchemy.orm import Session

from app.common.service import CommonService
from app.models.resume import Resume
from app.models.user import User


class BaseResumeService:
    """
    Base service for all entities that belong to a resume.
    """

    model: Type = None
    entity_name: str = "Entity"

    @classmethod
    def get_resume(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
    ) -> Resume:
        """
        Get a resume owned by the current user.
        """
        return CommonService.get_user_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

    @classmethod
    def get_entity(
        cls,
        db: Session,
        current_user: User,
        entity_id: str,
    ):
        """
        Get an entity owned by the current user.
        """
        return CommonService.get_owned_entity(
            db=db,
            model=cls.model,
            entity_id=entity_id,
            current_user=current_user,
            entity_name=cls.entity_name,
        )

    @classmethod
    def request_data(
        cls,
        request,
        *,
        exclude_unset: bool = False,
    ) -> dict[str, Any]:
        """
        Convert a Pydantic request model into a dictionary.
        """
        return request.model_dump(
            exclude_unset=exclude_unset,
        )

    @classmethod
    def create_entity(
        cls,
        db: Session,
        resume: Resume,
        data: dict[str, Any],
    ):
        """
        Create a new entity.
        """
        entity = cls.model(
            resume_id=resume.id,
            **data,
        )

        db.add(entity)
        db.commit()
        db.refresh(entity)

        return entity

    @classmethod
    def list_entities(
        cls,
        db: Session,
        resume: Resume,
        order_column,
    ):
        """
        List all entities belonging to a resume.
        """
        return (
            db.query(cls.model)
            .filter(
                cls.model.resume_id == resume.id,
            )
            .order_by(
                order_column.desc(),
            )
            .all()
        )

    @classmethod
    def update_entity(
        cls,
        db: Session,
        entity,
        data: dict[str, Any],
    ):
        """
        Update an existing entity.
        """
        for key, value in data.items():
            setattr(
                entity,
                key,
                value,
            )

        db.commit()
        db.refresh(entity)

        return entity

    @classmethod
    def delete_entity(
        cls,
        db: Session,
        entity,
    ) -> None:
        """
        Delete an entity.
        """
        db.delete(entity)
        db.commit()