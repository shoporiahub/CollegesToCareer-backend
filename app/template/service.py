from sqlalchemy.orm import Session

from app.models.template import Template, TemplateHighlight
from app.template.schemas import TemplateCreate, TemplateUpdate


class TemplateService:

    @staticmethod
    def create_template(
        db: Session,
        request: TemplateCreate,
    ) -> Template:

        template = Template(
            name=request.name,
            slug=request.slug,
            image=request.image,
            template_text=request.template_text,
            filename=request.filename,
            description=request.description,
            price=request.price,
            is_active=request.is_active,
            sort_order=request.sort_order,
        )

        db.add(template)
        db.flush()

        for index, highlight in enumerate(
            request.highlights
        ):
            template_highlight = TemplateHighlight(
                template_id=template.id,
                highlight=highlight,
                sort_order=index,
            )

            db.add(template_highlight)

        db.commit()
        db.refresh(template)

        return template

    @staticmethod
    def get_all_templates(
        db: Session,
    ) -> list[Template]:

        return (
            db.query(Template)
            .filter(
                Template.is_active.is_(True),
            )
            .order_by(
                Template.sort_order.asc(),
            )
            .all()
        )

    @staticmethod
    def get_template(
        db: Session,
        template_id: str,
    ) -> Template | None:

        return (
            db.query(Template)
            .filter(
                Template.id == template_id,
                Template.is_active.is_(True),
            )
            .first()
        )

    @staticmethod
    def update_template(
        db: Session,
        template: Template,
        request: TemplateUpdate,
    ) -> Template:

        update_data = request.model_dump(
            exclude_unset=True,
            exclude={"highlights"},
        )

        for field, value in update_data.items():
            setattr(template, field, value)

        if request.highlights is not None:

            template.highlights.clear()

            for index, highlight in enumerate(
                request.highlights
            ):
                template_highlight = TemplateHighlight(
                    template_id=template.id,
                    highlight=highlight,
                    sort_order=index,
                )

                template.highlights.append(
                    template_highlight,
                )

        db.commit()
        db.refresh(template)

        return template

    @staticmethod
    def delete_template(
        db: Session,
        template: Template,
    ) -> None:

        db.delete(template)
        db.commit()