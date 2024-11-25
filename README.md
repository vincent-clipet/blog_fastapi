# blog_fastapi

Basic demo API for a blog. Using :
- Python
- FastAPI
- SQLite

<br>
<br>



Install :
```bash
conda create --name fastapi
conda activate fastapi
conda install python=3.10 pip
pip install uvicorn fastapi
pip install SQLAlchemy
```

Run : [http://localhost:8000/](http://localhost:8000/)
```bash
conda activate fastapi
uvicorn src.main:app --reload
```

Import DB :
```bash
cat script.sql | sqlite3 app.db
```
