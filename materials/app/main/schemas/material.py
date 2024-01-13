from pydantic import BaseModel


class MaterialBase(BaseModel):
    title: str
    content: str


class MaterialCreate(MaterialBase):
    pass


class MaterialResponse(MaterialBase):
    id: int

    class Config:
        orm_mode = True
