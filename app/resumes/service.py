from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.resume import Resume
from app.models.template import Template
from app.models.user import User
from app.resumes.schemas import (
    ResumeCreate,
    ResumeUpdate,
)


class ResumeService:

    @staticmethod
    def create_resume(
        db: Session,
        current_user: User,
        request: ResumeCreate,
    ) -> Resume:

        # Check that the selected template exists
        template_result = db.execute(
            select(Template).where(
                Template.id == request.template_id,
                Template.is_active.is_(True),
            )
        )

        template = template_result.scalar_one_or_none()

        if template is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Template not found or inactive.",
            )

        resume = Resume(
            user_id=current_user.id,
            **request.model_dump(),
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def get_all_resumes(
        db: Session,
        current_user: User,
    ) -> list[Resume]:

        result = db.execute(
            select(Resume).where(
                Resume.user_id == current_user.id,
            )
        )

        return result.scalars().all()

    @staticmethod
    def get_resume(
        db: Session,
        resume_id: str,
        current_user: User,
    ) -> Resume:

        result = db.execute(
            select(Resume).where(
                Resume.id == resume_id,
                Resume.user_id == current_user.id,
            )
        )

        resume = result.scalar_one_or_none()

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found.",
            )

        return resume

    @staticmethod
    def get_resume_detail(
        db: Session,
        current_user: User,
        resume_id: str,
    ) -> Resume:

        result = db.execute(
            select(Resume)
            .options(
                selectinload(Resume.educations),
                selectinload(Resume.experiences),
                selectinload(Resume.projects),
                selectinload(Resume.skills),
                selectinload(Resume.certifications),
                selectinload(Resume.languages),
                selectinload(Resume.achievements),
            )
            .where(
                Resume.id == resume_id,
                Resume.user_id == current_user.id,
            )
        )

        resume = result.scalar_one_or_none()

        if resume is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resume not found.",
            )

        return resume

    @staticmethod
    def update_resume(
        db: Session,
        resume_id: str,
        current_user: User,
        request: ResumeUpdate,
    ) -> Resume:

        resume = ResumeService.get_resume(
            db=db,
            resume_id=resume_id,
            current_user=current_user,
        )

        update_data = request.model_dump(
            exclude_unset=True,
        )

        # If template_id is being changed,
        # make sure the new template exists and is active.
        if "template_id" in update_data:

            template_result = db.execute(
                select(Template).where(
                    Template.id == update_data["template_id"],
                    Template.is_active.is_(True),
                )
            )

            template = template_result.scalar_one_or_none()

            if template is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Template not found or inactive.",
                )

        for key, value in update_data.items():
            setattr(
                resume,
                key,
                value,
            )

        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def delete_resume(
        db: Session,
        resume_id: str,
        current_user: User,
    ) -> None:

        resume = ResumeService.get_resume(
            db=db,
            resume_id=resume_id,
            current_user=current_user,
        )

        db.delete(resume)
        db.commit()