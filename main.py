from fastapi import FastAPI, Query, Path, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from schemas.schema import BlogSchema
from models import blog_models
from database.database import SessionLocal, engine
from queries.blog_queries import BlogCrud
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder


app = FastAPI()


blog_models.Base.metadata.create_all(bind=engine)
# Dependency
def create_get_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@app.post("/create-blog", response_model = BlogSchema)
def create_blog(blog: BlogSchema, db: Session = Depends(create_get_session)):
    """Create a blog."""
    blog_crud = BlogCrud(db)
    response = blog_crud.create_blog(blog)
    if response:
        return JSONResponse(status_code=status.HTTP_201_CREATED)
    raise HTTPException(400, "something went wrong/ Bad request")


@app.get("/blogs", response_model=list[BlogSchema])
def list_blogs(db: Session = Depends(create_get_session)):
    blog_crud = BlogCrud(db)
    response = blog_crud.get_blogs()
    if response:
        response = jsonable_encoder(response)
        return JSONResponse(status_code=status.HTTP_200_OK, content=response)
    raise HTTPException(400, "something went wrong/ Bad request")


@app.get("/blogs/{blog_id}", response_model=BlogSchema)
def list_blog(blog_id: int, db: Session = Depends(create_get_session)):
    blog_crud = BlogCrud(db)
    response = blog_crud.get_blog(blog_id)
    if response:
        response = jsonable_encoder(response)
        return JSONResponse(status_code=status.HTTP_200_OK, content=response)
    raise HTTPException(400, "something went wrong/ Bad request")