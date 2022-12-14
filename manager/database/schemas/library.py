from pydantic import BaseModel

from manager.database.schemas.book import Book as BookSchema
from manager.database.schemas.users import Admin as AdminSchema, User as UserSchema


class Library(BaseModel):
    admins: list = []
    users: list = []

    borrowed_books: list = []
    books: list = []

    authors: list = []
