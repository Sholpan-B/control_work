from typing import List

from tortoise.exceptions import DoesNotExist

from tests.app.main.schemas.test import TestCreate, TestResponse

from tests.app.main.models.test import Test


async def create_test(test_create: TestCreate) -> TestResponse:
    test = await Test.create(**test_create.dict())
    return TestResponse.from_orm(test)


async def get_test(test_id: int) -> TestResponse:
    test = await Test.get_or_none(id=test_id)
    if not test:
        raise DoesNotExist(f"Test with id {test_id} not found")
    return TestResponse.from_orm(test)


async def get_tests() -> List[TestResponse]:
    tests = await Test.all()
    return [TestResponse.from_orm(test) for test in tests]


async def update_test(test_id: int, test_update: TestCreate) -> TestResponse:
    test = await Test.get_or_none(id=test_id)
    if not test:
        raise DoesNotExist(f"Test with id {test_id} not found")
    await test.update_from_dict(test_update.dict(exclude_unset=True))
    return TestResponse.from_orm(test)
