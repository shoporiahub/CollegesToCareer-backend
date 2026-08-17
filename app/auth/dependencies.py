from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session

from app.auth.security import (
    decode_access_token,
    oauth2_scheme,
)
from app.core.database import get_db
from app.models.user import User


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:

    print("\n========== AUTH DEBUG ==========")
    print("TOKEN RECEIVED:", token[:30], "...")

    try:
        payload = decode_access_token(token)

        print("JWT PAYLOAD:", payload)

        user_id = payload.get("sub")

        print("SUB:", user_id)
        print("SUB TYPE:", type(user_id))

        if user_id is None:
            print("ERROR: sub is missing")
            raise HTTPException(
                status_code=401,
                detail="JWT sub is missing",
            )

    except JWTError as error:

        print("JWT DECODE ERROR:", repr(error))

        raise HTTPException(
            status_code=401,
            detail=f"JWT decode failed: {error}",
        )

    user = (
        db.query(User)
        .filter(User.id == str(user_id))
        .first()
    )

    print("USER FOUND:", user)

    if user is None:
        print("ERROR: User does not exist:", user_id)

        raise HTTPException(
            status_code=401,
            detail="User from JWT does not exist",
        )

    print("AUTH SUCCESS:", user.email)
    print("================================\n")

    return user