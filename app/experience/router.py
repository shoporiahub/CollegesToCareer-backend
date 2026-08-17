from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.experience.schemas import (
    ExperienceCreate,
    ExperienceResponse,
    ExperienceUpdate,
)
from app.experience.service import ExperienceService
from app.models.user import User


router = APIRouter(
    prefix="/experiences",
    tags=["Experiences"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=ExperienceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_experience(
    resume_id: str,
    request: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    experience = ExperienceService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return ExperienceResponse.model_validate(
        experience,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[ExperienceResponse],
)
def list_experiences(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    experiences = ExperienceService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        ExperienceResponse.model_validate(
            experience,
        )
        for experience in experiences
    ]


@router.put(
    "/{experience_id}",
    response_model=ExperienceResponse,
)
def update_experience(
    experience_id: str,
    request: ExperienceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    experience = ExperienceService.update(
        db=db,
        current_user=current_user,
        experience_id=experience_id,
        request=request,
    )

    return ExperienceResponse.model_validate(
        experience,
    )


@router.delete(
    "/{experience_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_experience(
    experience_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ExperienceService.delete(
        db=db,
        current_user=current_user,
        experience_id=experience_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )