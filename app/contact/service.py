from sqlalchemy.orm import Session

from app.contact.schemas import ContactCreate
from app.models.contact import Contact


class ContactService:

    @staticmethod
    def create_contact(
        db: Session,
        request: ContactCreate,
    ) -> Contact:

        contact = Contact(
            **request.model_dump(),
        )

        db.add(contact)
        db.commit()
        db.refresh(contact)

        return contact