from fastapi import APIRouter

from .models import User
from .schemas import UserSignUpRequest

router = APIRouter(
    prefix="/user",
    tags = ['user'],
    responses={404: {"description": "Not found"}}
)

@router.get('/')
async def user_index() -> dict:
    return {"data": "u reached user"} 

@router.post('/sign_up')
async def user_sign_up(user_data: UserSignUpRequest) -> dict:
    await User.create(nickname=user_data.username)
    return

@router.get('/get/all')
async def user_get_all() -> dict:
    return await User.query.gino.all()