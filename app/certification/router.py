from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.certification.schemas import (
    CertificationCreate,
    CertificationResponse,
    CertificationUpdate,
)
from app.certification.service import CertificationService
from app.core.database import get_db
from app.models.user import User


router = APIRouter(
    prefix="/certifications",
    tags=["Certifications"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=CertificationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_certification(
    resume_id: str,
    request: CertificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    certification = CertificationService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return CertificationResponse.model_validate(
        certification,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[CertificationResponse],
)
def list_certifications(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    certifications = CertificationService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        CertificationResponse.model_validate(
            certification,
        )
        for certification in certifications
    ]


@router.put(
    "/{certification_id}",
    response_model=CertificationResponse,
)
def update_certification(
    certification_id: str,
    request: CertificationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    certification = CertificationService.update(
        db=db,
        current_user=current_user,
        certification_id=certification_id,
        request=request,
    )

    return CertificationResponse.model_validate(
        certification,
    )


@router.delete(
    "/{certification_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_certification(
    certification_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    CertificationService.delete(
        db=db,
        current_user=current_user,
        certification_id=certification_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )