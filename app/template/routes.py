from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.template.schemas import (
    TemplateCreate,
    TemplateResponse,
    TemplateUpdate,
)
from app.template.service import TemplateService


router = APIRouter(
    prefix="/templates",
    tags=["Templates"],
)


@router.post(
    "",
    response_model=TemplateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_template(
    request: TemplateCreate,
    db: Session = Depends(get_db),
):
    return TemplateService.create_template(
        db,
        request,
    )


@router.get(
    "",
    response_model=list[TemplateResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_templates(
    db: Session = Depends(get_db),
):
    return TemplateService.get_all_templates(db)


@router.get(
    "/{template_id}",
    response_model=TemplateResponse,
    status_code=status.HTTP_200_OK,
)
def get_template(
    template_id: str,
    db: Session = Depends(get_db),
):
    template = TemplateService.get_template(
        db,
        template_id,
    )

    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found.",
        )

    return template


@router.put(
    "/{template_id}",
    response_model=TemplateResponse,
    status_code=status.HTTP_200_OK,
)
def update_template(
    template_id: str,
    request: TemplateUpdate,
    db: Session = Depends(get_db),
):
    template = TemplateService.get_template(
        db,
        template_id,
    )

    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found.",
        )

    return TemplateService.update_template(
        db,
        template,
        request,
    )


@router.delete(
    "/{template_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_template(
    template_id: str,
    db: Session = Depends(get_db),
):
    template = TemplateService.get_template(
        db,
        template_id,
    )

    if not template:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Template not found.",
        )

    TemplateService.delete_template(
        db,
        template,
    )

    return None