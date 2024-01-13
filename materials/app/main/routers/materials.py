from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from authentication.app.main.services.authentication import get_current_user

from materials.app.main.models.material import Material
from authentication.app.main.models import User, UserMaterial
from materials.app.main.schemas.material import MaterialCreate, MaterialResponse

router = APIRouter()


@router.get("/materials/{material_id}", response_model=MaterialResponse, responses={404: {"model": HTTPNotFoundError}})
async def get_material(material_id: int):
    material = await Material.get_or_none(id=material_id)
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return MaterialResponse.from_orm(material)


@router.post("/materials", response_model=MaterialResponse)
async def create_material(material_create: MaterialCreate, current_user: User = Depends(get_current_user)):
    material = await Material.create(**material_create.dict(exclude_unset=True))
    await UserMaterial.create(user=current_user, material=material)
    return MaterialResponse.from_orm(material)
