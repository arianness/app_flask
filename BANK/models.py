from BANK.ext.database import db
from sqlalchemy import ForeignKey, String, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from sqlalchemy_serializer import SerializerMixin


# Create Roles Table
class Roles(db.Model, SerializerMixin):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"Roles(id={self.id!r})"

    def __init__(self, description):
        self.description = description


# TCreate Users Table
class Users(db.Model, SerializerMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r})"

    def __init__(self, name, email, password, role_id):
        self.name = name
        self.email = email
        self.password = password
        self.role_id = role_id

