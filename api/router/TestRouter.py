from fastapi import APIRouter
from api.model.UserModel import UserModel

from api.model.ResponseModel import SimpleResponse, BaseResponse
from api.model.Entity import User

router = APIRouter()


@router.get("/user")
def get_user():
    user_model = UserModel(
        name="Asif",
        age="25"
    )
    return user_model


# @router.post("/add", response_model=SimpleResponse)
# def add_user(name: str, age: str):
#     user_model = UserModel(
#         name=name,
#         age=age
#     )
#     users_collection.insert_one(user_model.dict())
#     return SimpleResponse


@router.get("/all", response_model=BaseResponse)
async def get_all_users():

    users = await User.find_all().to_list()
    base_response = BaseResponse(
        data=users
    )
    return base_response
