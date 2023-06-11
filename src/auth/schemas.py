from pydantic import BaseModel


class User(BaseModel):
    id: int
    UUID: str

    class Config:
        orm_mode = True
