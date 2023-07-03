from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

schemas.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#########
# USERS #
#########

@app.post("/users/create", response_model=models.User)
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="A User with this Email already exists")
    return crud.create_user(db=db, user=user)

@app.get("/users/list", response_model=list[models.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=models.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @app.post("/users/{user_id}/articles/", response_model=schemas.Article)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)



############
# ARTICLES #
############

@app.post("/articles/create", response_model=models.Article)
def create_article(article: models.ArticleCreate, db: Session = Depends(get_db)):
    existing_article = crud.get_article_by_title(db, title=article.title)
    if existing_article:
        raise HTTPException(status_code=400, detail="An Article with this title already exists")
    return crud.create_article(db=db, article=article)

@app.get("/articles/list", response_model=list[models.Article])
def read_articles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=skip, limit=limit)
    return articles

@app.get("/articles/{article_id}", response_model=models.Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article



########
# TAGS #
########

@app.post("/tag/create", response_model=models.Tag)
def create_tag(tag: models.TagCreate, db: Session = Depends(get_db)):
    existing_tag = crud.get_tag_by_name(db, name=tag.name)
    if existing_tag:
        raise HTTPException(status_code=400, detail="A tag with this name already exists")
    return crud.create_tag(db=db, tag=tag)

@app.get("/tag/list", response_model=list[models.Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.get_tags(db, skip=skip, limit=limit)
    return tags

@app.get("/tag/{tag_id}", response_model=models.Tag)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = crud.get_tag(db, tag_id=tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag
