from fastapi import FastAPI
from app.database import engine, Base
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

#routes
from app.routers import store
from app.routers import waiter
from app.routers import interview
from app.routers import question
from app.routers import catAnswer
from app.routers import interviewQuestion
from app.routers import answer
from app.routers import hostess
from app.routers import client
from app.routers import comments

from app.routers import auth

#Bot para prueba
from app.routers import chatBot

# Crear las tablas en la base de datos (automáticamente)
Base.metadata.create_all(bind=engine)

# Instanciar la aplicación FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dev-xen.com",
        "https://interal-control.dev-xen.com",
        "http://127.0.0.1:5500"
        ],  # Solo tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # O restringe a ["POST"] si solo usas POST
    allow_headers=["*"],  # O define encabezados específicos si prefieres
)

# Incluir los routers
app.include_router(store.router)
app.include_router(waiter.router)
app.include_router(interview.router)
app.include_router(question.router)
app.include_router(catAnswer.router)
app.include_router(interviewQuestion.router)
app.include_router(answer.router)
app.include_router(hostess.router)
app.include_router(client.router)
app.include_router(comments.router)

app.include_router(auth.router)