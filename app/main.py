from fastapi import FastAPI
from app.api.v1.endpoints import app_route,admin_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_route.router)
app.include_router(admin_routes.router)

