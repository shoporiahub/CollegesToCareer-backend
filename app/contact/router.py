from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.contact.schemas import (
    ContactCreate,
    ContactResponse,
)
from app.contact.service import ContactService
from app.core.database import get_db


router = APIRouter(
    prefix="/contact",
    tags=["Contact"],
)


@router.post(
    "",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_contact(
    request: ContactCreate,
    db: Session = Depends(get_db),
):
    return ContactService.create_contact(
        db=db,
        request=request,
    )