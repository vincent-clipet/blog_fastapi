from sqlalchemy.orm import Session

from . import models, schemas



########
# USER #
########

def get_user(db: Session, user_id: int):
    return db.query(schemas.User).filter(schemas.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(schemas.User).filter(schemas.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: models.UserCreate):
    db_user = schemas.User(
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



############
# ARTICLES #
############

def get_article(db: Session, article_id: int):
    return db.query(schemas.Article).filter(schemas.Article.id == article_id).first()

def get_article_by_title(db: Session, title: str):
    return db.query(schemas.Article).filter(schemas.Article.title == title).first()

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: models.ArticleCreate):
    article = schemas.Article(
        title=article.title,
        content=article.content,
        author_id=article.author_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item



########
# TAGS #
########

def get_tag(db: Session, tag_id: int):
    return db.query(schemas.Tag).filter(schemas.Tag.id == tag_id).first()

def get_tag_by_name(db: Session, name: str):
    return db.query(schemas.Tag).filter(schemas.Tag.name == name).first()

def get_tags(db: Session, skip: int = 0, limit: int = 100):
    return db.query(schemas.Tag).offset(skip).limit(limit).all()

def create_tag(db: Session, tag: models.TagCreate):
    db_tag = schemas.Tag(
        name=tag.name
    )
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag
