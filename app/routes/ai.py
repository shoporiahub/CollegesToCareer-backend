from fastapi import APIRouter, HTTPException

from app.schemas.ai import (
    AIRequest,
    AIResponse,
)

from app.services.ai_service import ask_ai


router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


@router.post(
    "/ask",
    response_model=AIResponse,
)
async def ask_ai_question(
    request: AIRequest,
):

    try:

        answer = await ask_ai(
            request.question,
        )

        return AIResponse(
            answer=answer,
        )

    except Exception as error:

        print(
            "AI request failed:",
            error,
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to process AI request.",
        )