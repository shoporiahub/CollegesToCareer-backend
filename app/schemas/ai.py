from pydantic import BaseModel, Field


class AIRequest(BaseModel):

    question: str = Field(
        ...,
        min_length=1,
        max_length=2000,
    )


class AIResponse(BaseModel):

    answer: str