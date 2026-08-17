from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse, Response
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.core.database import get_db
from app.models.user import User
from app.render.service import RenderService


router = APIRouter(
    prefix="/render",
    tags=["Render"],
)


render_service = RenderService()


@router.get(
    "/resume/{resume_id}",
    response_class=HTMLResponse,
)
def render_resume(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    html = render_service.render_resume(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return HTMLResponse(
        content=html,
    )


@router.get(
    "/resume/{resume_id}/pdf",
)
def download_resume_pdf(
    resume_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    pdf = render_service.render_resume_pdf(
        db=db,
        current_user=current_user,
        resume_id=resume_id,
    )

    return Response(
        content=pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition": (
                f'attachment; filename="resume_{resume_id}.pdf"'
            ),
        },
    )