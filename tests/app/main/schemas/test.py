from pydantic import BaseModel
from typing import List


class TestCreate(BaseModel):
    question: str
    options: List[str]
    correct_option: str


class TestUpdate(BaseModel):
    question: str
    options: List[str]
    correct_option: str


class TestResponse(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_option: str

    class Config:
        orm_mode = True
