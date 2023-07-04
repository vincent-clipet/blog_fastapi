from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import pydantic

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

@app.post("/user/create", response_model=models.User)
def user_create(user: models.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.user_get_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="A User with this Email already exists")
    return crud.user_create(db=db, user=user)

@app.get("/user/list", response_model=list[models.User])
def user_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.user_get_all(db, skip=skip, limit=limit)
    return users

@app.get("/user/{user_id}", response_model=models.User)
def user_read(user_id: int, db: Session = Depends(get_db)):
    user = crud.user_get(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/user/{user_id}")
def user_delete(user_id: int, db: Session = Depends(get_db)):
    user = crud.user_get(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.user_delete(db=db, user=user)

@app.patch("/user/{user_id}", response_model=models.User)
def user_patch(user_id: int, body: models.UserPatch, db: Session = Depends(get_db)):
    user = crud.user_get(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.user_patch(db=db, user=user, body=body)



############
# ARTICLES #
############

@app.post("/article/create", response_model=models.Article)
def article_create(article: models.ArticleCreate, db: Session = Depends(get_db)):
    existing_article = crud.article_get_by_title(db, title=article.title)
    if existing_article:
        raise HTTPException(status_code=400, detail="An Article with this title already exists")
    return crud.article_create(db=db, article=article)

@app.get("/article/list", response_model=list[models.Article])
def article_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    articles = crud.article_get_all(db, skip=skip, limit=limit)
    return articles

@app.get("/article/{article_id}", response_model=models.Article)
def article_read(article_id: int, db: Session = Depends(get_db)):
    article = crud.article_get(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@app.delete("/article/{article_id}")
def article_delete(article_id: int, db: Session = Depends(get_db)):
    article = crud.article_get(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return crud.article_delete(db=db, article=article)

@app.patch("/article/{article_id}", response_model=models.Article)
def article_patch(article_id: int, body: models.ArticlePatch, db: Session = Depends(get_db)):
    article = crud.article_get(db, article_id=article_id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return crud.article_patch(db=db, article=article, body=body)



########
# TAGS #
########

@app.post("/tag/create", response_model=models.Tag)
def tag_create(tag: models.TagCreate, db: Session = Depends(get_db)):
    existing_tag = crud.tag_get_by_name(db, name=tag.name)
    if existing_tag:
        raise HTTPException(status_code=400, detail="A tag with this name already exists")
    return crud.tag_create(db=db, tag=tag)

@app.get("/tag/list", response_model=list[models.Tag])
def tag_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tags = crud.tag_get_all(db, skip=skip, limit=limit)
    return tags

@app.get("/tag/{tag_id}", response_model=models.Tag)
def tag_read(tag_id: int, db: Session = Depends(get_db)):
    tag = crud.tag_get(db, tag_id=tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@app.delete("/tag/{tag_id}")
def tag_delete(tag_id: int, db: Session = Depends(get_db)):
    tag = crud.tag_get(db, tag_id=tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return crud.tag_delete(db=db, tag=tag)

@app.patch("/tag/{tag_id}", response_model=models.Tag)
def article_patch(tag_id: int, body: models.TagPatch, db: Session = Depends(get_db)):
    tag = crud.tag_get(db, tag_id=tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return crud.tag_patch(db=db, tag=tag, body=body)
