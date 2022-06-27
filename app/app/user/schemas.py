from pydantic import BaseModel

class UserSignUpRequest(BaseModel):
    username: str