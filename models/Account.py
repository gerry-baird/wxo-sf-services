from pydantic import BaseModel

class Account(BaseModel):
    id: str
    name: str
    revenue: float

class AccountList(BaseModel):
    totalSize: int
    records: list[Account]
