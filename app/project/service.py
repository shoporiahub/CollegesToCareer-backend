from sqlalchemy.orm import Session

from app.common.base_service import BaseResumeService
from app.models.project import Project
from app.models.user import User
from app.project.schemas import (
    ProjectCreate,
    ProjectUpdate,
)


class ProjectService(BaseResumeService):

    model = Project
    entity_name = "Project"

    @classmethod
    def create(
        cls,
        db: Session,
        current_user: User,
        resume_id: str,
        request: ProjectCreate,
    ) -> Project:

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
    ) -> list[Project]:

        resume = cls.get_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        return cls.list_entities(
            db=db,
            resume=resume,
            order_column=Project.start_date,
        )

    @classmethod
    def update(
        cls,
        db: Session,
        current_user: User,
        project_id: str,
        request: ProjectUpdate,
    ) -> Project:

        project = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=project_id,
        )

        return cls.update_entity(
            db=db,
            entity=project,
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
        project_id: str,
    ) -> None:

        project = cls.get_entity(
            db=db,
            current_user=current_user,
            entity_id=project_id,
        )

        cls.delete_entity(
            db=db,
            entity=project,
        )