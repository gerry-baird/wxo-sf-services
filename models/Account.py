from pydantic import BaseModel

class Account(BaseModel):
    name: str
    revenue: float

class AccountList(BaseModel):
    totalSize: int
    accounts: list[Account]
