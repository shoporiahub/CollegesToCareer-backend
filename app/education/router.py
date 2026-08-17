from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.education.schemas import (
    EducationCreate,
    EducationResponse,
    EducationUpdate,
)
from app.education.service import EducationService
from app.models.user import User


router = APIRouter(
    prefix="/educations",
    tags=["Educations"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=EducationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_education(
    resume_id: str,
    request: EducationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    education = EducationService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return EducationResponse.model_validate(
        education,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[EducationResponse],
)
def list_educations(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    educations = EducationService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        EducationResponse.model_validate(
            education,
        )
        for education in educations
    ]


@router.put(
    "/{education_id}",
    response_model=EducationResponse,
)
def update_education(
    education_id: str,
    request: EducationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    education = EducationService.update(
        db=db,
        current_user=current_user,
        education_id=education_id,
        request=request,
    )

    return EducationResponse.model_validate(
        education,
    )


@router.delete(
    "/{education_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_education(
    education_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    EducationService.delete(
        db=db,
        current_user=current_user,
        education_id=education_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )