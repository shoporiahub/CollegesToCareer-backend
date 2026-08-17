from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.models.user import User

from fastapi.security import OAuth2PasswordRequestForm

from app.auth.schemas import (
    AuthResponse,
    LoginRequest,
    OAuthTokenResponse,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from app.auth.service import AuthService
from app.core.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    user, token = AuthService.register(
        db=db,
        request=request,
    )

    return AuthResponse(
        user=UserResponse.model_validate(user),
        token=TokenResponse(
            access_token=token,
        ),
    )

@router.post(
    "/token",
    response_model=OAuthTokenResponse,
)
def token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):

    request = LoginRequest(
        email=form_data.username,
        password=form_data.password,
    )

    user, token = AuthService.login(
        db=db,
        request=request,
    )

    return OAuthTokenResponse(
        access_token=token,
    )

@router.post(
    "/login",
    response_model=AuthResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    user, token = AuthService.login(
        db=db,
        request=request,
    )

    return AuthResponse(
        user=UserResponse.model_validate(user),
        token=TokenResponse(
            access_token=token,
        ),
    )

@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user