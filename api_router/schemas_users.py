from pydantic import BaseModel, EmailStr, Field


class BaseUserInfo(BaseModel):
    name: str = Field(
        max_length=100,
        min_length=1,
        examples=["Vincent"],
        description="Name of the new user",
    )
    surname: str = Field(
        max_length=100,
        min_length=1,
        examples=["Bridge"],
        description="Surname of the new user",
    )
    email: EmailStr = Field(
        examples=["test_hillel_api_mailing@ukr.net"], description="EMAIL of the user"
    )


class UserPasswordField(BaseModel):
    password: str = Field(
        description="your password", examples=["vince66578"], min_length=8
    )


class RegisterUserRequest(BaseUserInfo, UserPasswordField):
    pass
