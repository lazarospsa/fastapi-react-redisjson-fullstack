import os
from urllib.request import Request
from webbrowser import get
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from typing import Optional
from starlette.requests import Request
# import fastapi_jwt_auth
# import uvicorn


load_dotenv()

HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=[
                   'http://localhost:3000'], allow_methods=['*'], allow_headers=['*'])
redis_db = get_redis_connection(
    host=HOST_DB, port=PORT_DB, password=PASSWORD_DB, decode_responses=True)


class Task(HashModel):
    name: str
    completed: Optional[bool] = 0

    class Meta:
        database = redis_db


@app.get('/tasks')
async def all():
    return [format(pk) for pk in Task.all_pks()]


def format(pk: str):
    task = Task.get(pk)

    return {
        'id': task.pk,
        'name': task.name,
        'complete': task.completed,
    }

@app.post('/tasks')
async def create(task: Task):
    return task.save()

@app.put('/tasks/{pk}')
async def update(pk: str, request: Request):
    task = Task.get(pk)
    body = await request.json()
    task.completed = int(body['complete'])
    return task.save()


@app.delete('/tasks/{pk}')
async def deletefunc(pk: str):
    task = Task.get(pk)
    return task.delete(pk)