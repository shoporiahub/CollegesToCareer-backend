from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.sql import func

from app.models.base import Base


class AIConversation(Base):

    __tablename__ = "ai_conversations"

    id = Column(
        # use your existing ID type here
        ...
    )

    user_id = Column(
        ...,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    resume_id = Column(
        ...,
        ForeignKey("resumes.id"),
        nullable=True,
        index=True,
    )

    prompt = Column(
        Text,
        nullable=False,
    )

    answer = Column(
        Text,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )