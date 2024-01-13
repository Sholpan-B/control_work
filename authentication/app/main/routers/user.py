from typing import List

from fastapi import APIRouter, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

from materials.app.main.schemas.material import MaterialResponse
from authentication.app.main.services.authentication import get_current_user
from authentication.app.main.schemas.user import UserResponse
from tests.app.main.schemas.test import TestResponse

router = APIRouter()


@router.get("/users/me", response_model=UserResponse)
async def read_user_me(current_user: User = Depends(get_current_user)):
    return UserResponse.from_orm(current_user)


@router.get("/users/{user_id}", response_model=UserResponse, responses={404: {"model": HTTPNotFoundError}})
async def read_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPNotFoundError(detail="User not found")
    return UserResponse.from_orm(user)


@router.get("/users/me/materials", response_model=List[MaterialResponse])
async def get_user_materials(current_user: User = Depends(get_current_user)):
    materials = await UserMaterial.filter(user=current_user).prefetch_related("material")
    return [MaterialResponse.from_orm(um.material) for um in materials]


@router.get("/users/me/tests", response_model=List[TestResponse])
async def get_user_tests(current_user: User = Depends(get_current_user)):
    tests = await UserTest.filter(user=current_user).prefetch_related("test")
    return [TestResponse.from_orm(ut.test) for ut in tests]
