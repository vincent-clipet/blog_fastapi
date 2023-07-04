from sqlalchemy.orm import Session

from . import models
from .schemas import User, Article, Tag



#############
# FUNCTIONS #
#############
def patch_entity(entity, new_values):
    for key, value in new_values.__dict__.items():
        setattr(entity, key, value)



########
# USER #
########

def user_get(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def user_get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def user_get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

def user_create(db: Session, user: models.UserCreate):
    db_user = User(
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def user_delete(db: Session, user: User):
    db.query(User).filter(User.id == user.id).delete(synchronize_session="fetch")

def user_patch(db: Session, user: models.User, body: models.UserPatch):
    patch_entity(user, body)
    db.commit()
    db.refresh(user)
    return user



############
# ARTICLES #
############

def article_get(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def article_get_by_title(db: Session, title: str):
    return db.query(Article).filter(Article.title == title).first()

def article_get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Article).offset(skip).limit(limit).all()

def article_create(db: Session, article: models.ArticleCreate):
    article = Article(
        title=article.title,
        content=article.content,
        author_id=article.author_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

def article_delete(db: Session, article: Article):
    db.query(Article).filter(Article.id == article.id).delete(synchronize_session="fetch")

def article_patch(db: Session, article: models.Article, body: models.ArticlePatch):
    patch_entity(article, body)
    db.commit()
    db.refresh(article)
    return article



########
# TAGS #
########

def tag_get(db: Session, tag_id: int):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def tag_get_by_name(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()

def tag_get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Tag).offset(skip).limit(limit).all()

def tag_create(db: Session, tag: models.TagCreate):
    db_tag = Tag(
        name=tag.name
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def tag_delete(db: Session, tag: Tag):
    db.query(Tag).filter(Tag.id == tag.id).delete(synchronize_session="fetch")

def tag_patch(db: Session, tag: models.Tag, body: models.TagPatch):
    patch_entity(tag, body)
    db.commit()
    db.refresh(tag)
    return tag
