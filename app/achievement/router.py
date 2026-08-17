from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.achievement.schemas import (
    AchievementCreate,
    AchievementResponse,
    AchievementUpdate,
)
from app.achievement.service import AchievementService
from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User


router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"],
)


@router.post(
    "/resume/{resume_id}",
    response_model=AchievementResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_achievement(
    resume_id: str,
    request: AchievementCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    achievement = AchievementService.create(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
        request=request,
    )

    return AchievementResponse.model_validate(
        achievement,
    )


@router.get(
    "/resume/{resume_id}",
    response_model=list[AchievementResponse],
)
def list_achievements(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    achievements = AchievementService.list(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return [
        AchievementResponse.model_validate(
            achievement,
        )
        for achievement in achievements
    ]


@router.put(
    "/{achievement_id}",
    response_model=AchievementResponse,
)
def update_achievement(
    achievement_id: str,
    request: AchievementUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    achievement = AchievementService.update(
        db=db,
        current_user=current_user,
        achievement_id=achievement_id,
        request=request,
    )

    return AchievementResponse.model_validate(
        achievement,
    )


@router.delete(
    "/{achievement_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_achievement(
    achievement_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    AchievementService.delete(
        db=db,
        current_user=current_user,
        achievement_id=achievement_id,
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )