from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.auth.schemas import LoginRequest, RegisterRequest
from app.auth.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User


class AuthService:

    @staticmethod
    def register(
        db: Session,
        request: RegisterRequest,
    ) -> tuple[User, str]:

        existing_user = (
            db.query(User)
            .filter(User.email == request.email)
            .first()
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered.",
            )

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email=request.email,
            hashed_password=hash_password(
                request.password,
            ),
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return user, token


    @staticmethod
    def login(
        db: Session,
        request: LoginRequest,
    ) -> tuple[User, str]:

        user = (
            db.query(User)
            .filter(User.email == request.email)
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not verify_password(
            request.password,
            user.hashed_password,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        token = create_access_token(
            {
                "sub": str(user.id),
            }
        )

        return user, token