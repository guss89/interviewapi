from fastapi import FastAPI
from app.database import engine, Base
from app.config import settings

#routes
from app.routers import store
from app.routers import waiter
from app.routers import interview
from app.routers import question
from app.routers import catAnswer
from app.routers import interviewQuestion
from app.routers import answer
from app.routers import hostess

# Crear las tablas en la base de datos (automáticamente)
Base.metadata.create_all(bind=engine)

# Instanciar la aplicación FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
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