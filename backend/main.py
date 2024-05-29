from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from services.config import get_settings
from api.routes import router
import uvicorn
from database.session import engine
from database.models import Base


settings = get_settings()

#Ensure that database is created
Base.metadata.create_all(engine)

app = FastAPI(
    title= settings.project_name,
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


origins = ["http://localhost:8080"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
   
