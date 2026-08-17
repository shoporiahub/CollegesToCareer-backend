from io import BytesIO
from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape,
)
from sqlalchemy.orm import Session
from weasyprint import HTML

from app.models.user import User
from app.resumes.service import ResumeService


class RenderService:

    def __init__(self):

        self.templates_path = (
            Path(__file__).parent.parent
            / "templates"
        )

        self.base_path = (
            Path(__file__).parent.parent
        )

        self.environment = Environment(
            loader=FileSystemLoader(
                self.templates_path,
            ),
            autoescape=select_autoescape(
                ["html", "xml"],
            ),
        )

    def render_resume(
        self,
        db: Session,
        current_user: User,
        resume_id: str,
    ) -> str:
        """
        Render a resume as HTML using the filename
        configured for the selected template.
        """

        resume = ResumeService.get_resume_detail(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        # -----------------------------------------------------
        # Validate template
        # -----------------------------------------------------

        if not resume.template:
            raise ValueError(
                "Resume template not found."
            )

        if not resume.template.filename:
            raise ValueError(
                "Resume template filename is missing."
            )

        # -----------------------------------------------------
        # Get template filename from database
        #
        # Example:
        #
        # template1/index.html
        #
        # This is relative to:
        #
        # app/templates/
        # -----------------------------------------------------

        template_name = (
            resume.template.filename
        )

        # -----------------------------------------------------
        # Render Jinja template
        # -----------------------------------------------------

        template = self.environment.get_template(
            template_name,
        )

        html = template.render(
            resume=resume,
        )

        return html

    def render_resume_pdf(
        self,
        db: Session,
        current_user: User,
        resume_id: str,
    ) -> bytes:
        """
        Render a resume as PDF using the selected
        template.
        """

        html = self.render_resume(
            db=db,
            current_user=current_user,
            resume_id=resume_id,
        )

        pdf_buffer = BytesIO()

        HTML(
            string=html,
            base_url=str(self.base_path),
        ).write_pdf(
            target=pdf_buffer,
        )

        return pdf_buffer.getvalue()