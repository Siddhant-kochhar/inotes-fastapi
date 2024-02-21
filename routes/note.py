from typing import Union
from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from config.db import conn
from fastapi.templating import Jinja2Templates
from schemas.note import noteEntity,notesEntity

note=APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/",response_class=HTMLResponse)
async def read_item(request:Request):
    docs=conn.notes.notes.find({})
    newDocs=[]
    
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title":doc.get("title", "not found"),
            "desc":doc.get("desc", "not found"),
            "important":doc.get("important", "not found")
        })
    print(newDocs)
    return templates.TemplateResponse("index.html",{"request": request, "newDocs":newDocs})



@note.post("/save-notes")
async def create_item(request:Request ):
    form = await request.form()
    formDict = dict(form)
    formDict["important"]=True if formDict.get("important")=="on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"success":True}

