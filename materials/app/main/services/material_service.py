from typing import List

from tortoise.exceptions import DoesNotExist
from materials.app.main.models.material import Material
from materials.app.main.schemas.material import MaterialCreate, MaterialResponse


async def create_material(material_create: MaterialCreate) -> MaterialResponse:
    material = await Material.create(**material_create.dict())
    return MaterialResponse.from_orm(material)


async def get_material(material_id: int) -> MaterialResponse:
    material = await Material.get_or_none(id=material_id)
    if not material:
        raise DoesNotExist(f"Material with id {material_id} not found")
    return MaterialResponse.from_orm(material)


async def get_materials() -> List[MaterialResponse]:
    materials = await Material.all()
    return [MaterialResponse.from_orm(material) for material in materials]


async def update_material(material_id: int, material_update: MaterialCreate) -> MaterialResponse:
    material = await Material.get_or_none(id=material_id)
    if not material:
        raise DoesNotExist(f"Material with id {material_id} not found")
    await material.update_from_dict(material_update.dict(exclude_unset=True))
    return MaterialResponse.from_orm(material)
