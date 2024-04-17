from pydantic import BaseModel

class Contact(BaseModel):
    name: str
    title: str
    email: str

class ContactList(BaseModel):
    totalSize: int
    records: list[Contact]