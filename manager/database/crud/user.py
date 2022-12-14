from sqlalchemy import select
from sqlalchemy.orm import Session

from manager.database.models import User as UserModel
from manager.database.models import BorrowedBook as BorrowedBookModel
from manager.database.schemas.users import UserCreate
from manager.security import Password


def create_user(db: Session, user: UserCreate) -> UserModel:
    """Creates a User and adds User to User Table Database."""
    db_user = UserModel(**user.dict())

    db_user.password = Password.hash(user.password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session) -> list[UserModel] | list:
    """Returns all users who are not admins."""
    return db.scalars(select(UserModel).where(UserModel.is_admin == False)).all()


def get_admins(db: Session) -> list[UserModel] | list:
    """Returns all users who are admins. Functionality only for admins."""
    return db.scalars(select(UserModel).where(UserModel.is_admin == True)).all()


def get_user_by_id(db: Session, user_id: int) -> UserModel | None:
    """Gets a user with a specific id."""
    return db.get(UserModel, user_id)


def get_user_by_username(db: Session, username: str) -> UserModel | None:
    """Returns a user with a specific Username; since usernames are unique."""
    return db.scalar(select(UserModel).where(UserModel.username == username))
