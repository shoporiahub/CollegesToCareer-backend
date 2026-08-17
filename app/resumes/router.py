from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.resumes.detail_schema import ResumeDetailResponse
from app.resumes.schemas import (
    ResumeCreate,
    ResumeResponse,
    ResumeUpdate,
)
from app.resumes.service import ResumeService


router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.post(
    "",
    response_model=ResumeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_resume(
    request: ResumeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ResumeService.create_resume(
        db=db,
        current_user=current_user,
        request=request,
    )


@router.get(
    "",
    response_model=list[ResumeResponse],
)
def get_all_resumes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ResumeService.get_all_resumes(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{resume_id}",
    response_model=ResumeResponse,
)
def get_resume(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ResumeService.get_resume(
        db=db,
        resume_id=resume_id,
        current_user=current_user,
    )


@router.get(
    "/{resume_id}/full",
    response_model=ResumeDetailResponse,
)
def get_resume_detail(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    resume = ResumeService.get_resume_detail(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return ResumeDetailResponse.model_validate(
        resume,
    )


@router.put(
    "/{resume_id}",
    response_model=ResumeResponse,
)
def update_resume(
    resume_id: str,
    request: ResumeUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ResumeService.update_resume(
        db=db,
        resume_id=resume_id,
        current_user=current_user,
        request=request,
    )


@router.delete(
    "/{resume_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_resume(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ResumeService.delete_resume(
        db=db,
        resume_id=resume_id,
        current_user=current_user,
    )