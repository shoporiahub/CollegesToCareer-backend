from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.language.schemas import (
    LanguageCreate,
    LanguageResponse,
    LanguageUpdate,
)
from app.language.service import LanguageService
from app.models.user import User


router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=LanguageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_language(
    resume_id: str,
    request: LanguageCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    language = LanguageService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return LanguageResponse.model_validate(
        language,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[LanguageResponse],
)
def list_languages(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    languages = LanguageService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        LanguageResponse.model_validate(
            language,
        )
        for language in languages
    ]


@router.put(
    "/{language_id}",
    response_model=LanguageResponse,
)
def update_language(
    language_id: str,
    request: LanguageUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    language = LanguageService.update(
        db=db,
        current_user=current_user,
        language_id=language_id,
        request=request,
    )

    return LanguageResponse.model_validate(
        language,
    )


@router.delete(
    "/{language_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_language(
    language_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    LanguageService.delete(
        db=db,
        current_user=current_user,
        language_id=language_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )