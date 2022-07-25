from fastapi import APIRouter, status, HTTPException, Depends, Request
from fastapi.templating import Jinja2Templates

from Schemas import ArticleSchemaIn, ArticleSchema, UserSchema
from db import Article, database
from typing import List
from Token import get_current_user  # do zabezpieczenie routów

router = APIRouter(
    tags=["Articles"]
)

templates = Jinja2Templates(directory='templates')

@router.post('/articles/', status_code=status.HTTP_201_CREATED, response_model=ArticleSchema)
async def insert_article(article: ArticleSchemaIn, current_user:UserSchema = Depends(get_current_user)):
    query = Article.insert().values(title=article.title, description=article.description)
    last_record_id = await database.execute(query)
    return {**article.dict(), "id": last_record_id}


@router.get('/articles/', response_model=List[ArticleSchema])  # List bo otrzymuje wszystkie artykułu
async def get_articles(request:Request):
    query = Article.select()
    articles_set = await database.fetch_all(query=query)
    return templates.TemplateResponse("index.html", {"request": request, "articles": articles_set})


@router.get('/articles/{id}/', response_model=ArticleSchema)
async def get_details(id: int, current_user:UserSchema = Depends(get_current_user)):
    query = Article.select().where(id == Article.c.id)
    myarticle = await database.fetch_one(query=query)

    if not myarticle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=article)
    return {**myarticle}


@router.put('/articles{id}/', response_model=ArticleSchema)
async def update_article(id: int, article: ArticleSchemaIn, current_user:UserSchema = Depends(get_current_user)):
    query = Article.update().where(Article.c.id == id).values(title=article.title, description=article.description)
    last_record_id = await database.execute(query)
    return {**article.dict(), "id": last_record_id}


@router.delete('/articles{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_article(id: int, current_user:UserSchema = Depends(get_current_user)):
    query = Article.delete().where(Article.c.id == id)
    await database.execute(query)
    return {"message": "Article deleted"}
