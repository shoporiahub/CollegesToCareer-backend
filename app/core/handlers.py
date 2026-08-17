from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import ResumeAIException
from app.core.logger import logger


async def resume_ai_exception_handler(
    request: Request,
    exc: ResumeAIException,
):

    logger.error(
        "%s %s -> %s",
        request.method,
        request.url.path,
        exc.message,
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
        },
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception,
):

    logger.exception(exc)

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error.",
        },
    )