from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi.security import OAuth2PasswordRequestForm


from authentication.app.main.models import User
from authentication.app.main.schemas.user import UserCreate, UserResponse
from authentication.app.main.services.authentication import authenticate_user, create_access_token

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", response_model=UserResponse)
async def register_user(user_create: UserCreate):
    existing_user = await User.get_or_none(username=user_create.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    user = await User.create(username=user_create.username, email=user_create.email, password=user_create.password)
    return UserResponse.from_orm(user)
