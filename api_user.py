import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from uuid import UUID

import jinja2
from fastapi import FastAPI, HTTPException, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from utils_hashlib import get_password_hash

import config
import dao
from api_router.api_users import api_router_users
from database import User, session

app = FastAPI()

templates = Jinja2Templates(directory="templates")

SessionLocal = sessionmaker(
    bind=config.engine, class_=AsyncSession, expire_on_commit=False
)


def create_user(name: str, email: str, password: str, surname: str = "") -> User:
    user = User(
        name=name,
        surname=surname,
        email=email,
        hashed_password=get_password_hash(password),
    )
    session.add(user)
    session.commit()
    return user


def get_user_by_email(email: str) -> User | None:
    user = session.query(User).filter(User.email == email).first()
    return user


def get_user_by_uuid(user_uuid: str) -> User | None:
    user = session.query(User).filter(User.user_uuid == user_uuid).first()
    return user


@api_router_users.get("/verify/{user_uuid}")
def verify_user_account(user_uuid: UUID):
    maybe_user = dao.get_user_by_uuid(user_uuid)
    if not maybe_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong data")


def activate_user_account(user: User) -> User:
    if not user:
        raise HTTPException(status_code=400, detail="Log in!")

    def send_email(
        recipients: list[str],
        *,
        mail_body: str,
        mail_subject: str,
        attachment: str = None,
    ) -> None:
        TOKEN_API = config.TOKEN_API
        USER = config.USER
        SMTP_SERVER = config.SMTP_SERVER

        msg = MIMEMultipart("alternative")
        msg["Subject"] = mail_subject
        msg["From"] = f"{USER} sent this email"
        msg["To"] = ", ".join(recipients)
        msg["Reply-To"] = USER
        msg["Return-Path"] = USER
        msg["X-Mailer"] = "decorator"

        if attachment:
            is_file_exists = os.path.exists(attachment)
            if not is_file_exists:
                print(f"File {attachment} doesn't exist")
                raise ValueError(f"File {attachment} doesn't exist")
            else:
                basename = os.path.basename(attachment)
                filesize = os.path.getsize(attachment)
                file = MIMEBase("application", f"octet-stream; name={basename}")
                file.set_payload(open(attachment, "rb").read())
                file.add_header("Content-Description", attachment)
                file.add_header(
                    "Content-Disposition",
                    f"attachment; filename={basename}; size={filesize}",
                )
                encoders.encode_base64(file)
                msg.attach(file)

        text_to_send = MIMEText(mail_body, "html")
        msg.attach(text_to_send)

        mail = smtplib.SMTP_SSL(SMTP_SERVER)
        mail.login(USER, TOKEN_API)
        mail.sendmail(USER, recipients, msg.as_string())
        mail.quit()

    def create_welcome_letter(params: dict) -> str:
        template_loader = jinja2.FileSystemLoader(searchpath="./")
        template_env = jinja2.Environment(loader=template_loader)
        template_file = "templates/welcome_letter.html"
        template = template_env.get_template(template_file)
        output = template.render(params)
        return output

    if user.is_verified:
        raise HTTPException(status_code=400, detail="Already verified")
    user.is_verified = True
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
