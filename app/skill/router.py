from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.skill.schemas import (
    SkillCreate,
    SkillResponse,
    SkillUpdate,
)
from app.skill.service import SkillService


router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_skill(
    resume_id: str,
    request: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    skill = SkillService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return SkillResponse.model_validate(
        skill,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[SkillResponse],
)
def list_skills(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    skills = SkillService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        SkillResponse.model_validate(
            skill,
        )
        for skill in skills
    ]


@router.put(
    "/{skill_id}",
    response_model=SkillResponse,
)
def update_skill(
    skill_id: str,
    request: SkillUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    skill = SkillService.update(
        db=db,
        current_user=current_user,
        skill_id=skill_id,
        request=request,
    )

    return SkillResponse.model_validate(
        skill,
    )


@router.delete(
    "/{skill_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_skill(
    skill_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    SkillService.delete(
        db=db,
        current_user=current_user,
        skill_id=skill_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )