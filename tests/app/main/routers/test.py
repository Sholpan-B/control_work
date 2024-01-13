from typing import List

from fastapi import APIRouter, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

from tests.app.main.schemas.test import TestCreate, TestResponse
from tests.app.main.services.test_service import create_test, get_test, get_tests, update_test

router = APIRouter()


@router.post("/tests", response_model=TestResponse)
async def create_new_test(test_create: TestCreate):
    return await create_test(test_create)


@router.get("/tests/{test_id}", response_model=TestResponse, responses={404: {"model": HTTPNotFoundError}})
async def get_single_test(test_id: int):
    return await get_test(test_id)


@router.get("/tests", response_model=List[TestResponse])
async def get_all_tests():
    return await get_tests()


@router.put("/tests/{test_id}", response_model=TestResponse, responses={404: {"model": HTTPNotFoundError}})
async def update_existing_test(test_id: int, test_update: TestCreate):
    return await update_test(test_id, test_update)
