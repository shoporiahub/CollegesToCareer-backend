from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.project.schemas import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from app.project.service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_project(
    resume_id: str,
    request: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = ProjectService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return ProjectResponse.model_validate(
        project,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[ProjectResponse],
)
def list_projects(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    projects = ProjectService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        ProjectResponse.model_validate(
            project,
        )
        for project in projects
    ]


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
)
def update_project(
    project_id: str,
    request: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    project = ProjectService.update(
        db=db,
        current_user=current_user,
        project_id=project_id,
        request=request,
    )

    return ProjectResponse.model_validate(
        project,
    )


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_project(
    project_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ProjectService.delete(
        db=db,
        current_user=current_user,
        project_id=project_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )