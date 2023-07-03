from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .database import Base

#######################
# RELATIONSHIP TABLES #
#######################

table_article_tags = Table(
    "articles_tags",
    Base.metadata,
    Column("article_id", ForeignKey("articles.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)



##########
# MODELS #
##########

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    articles: Mapped[list['Article']] = relationship("Article", back_populates="author")



class Article(Base):
    __tablename__ = "articles"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped[User] = relationship("User", back_populates="articles")

    tags: Mapped[list['Tag']] = relationship(secondary=table_article_tags, back_populates="articles")


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    articles: Mapped[list['Article']] = relationship(secondary=table_article_tags, back_populates="tags")



