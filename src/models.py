# from __future__ import annotations
from typing import ForwardRef
from pydantic import BaseModel



# Python class loading sucks - part 1
Article = ForwardRef('Article')
User = ForwardRef('User')
Tag = ForwardRef('Tag')



# USER
class UserBase(BaseModel):
    email: str
class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int
    articles: list[Article] = []
    class Config:
        orm_mode = True



# ARTICLE
class ArticleBase(BaseModel): # Create or read
    title: str
    content: str | None = None
class ArticleCreate(ArticleBase): # Create
    author_id: int
class Article(ArticleBase): # Read
    id: int
    author_id: int
    tags: list[Tag] = []
    class Config:
        orm_mode = True



# TAG
class TagBase(BaseModel):
    name: str
class TagCreate(TagBase):
    pass
class Tag(TagBase):
    id: int
    articles: list[Article] = []
    class Config:
        orm_mode = True



# Python class loading sucks - part 2
Tag.update_forward_refs()
User.update_forward_refs()
Article.update_forward_refs()
