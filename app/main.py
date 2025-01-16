from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import OPENAPI_URL
from app.routes import general

# tags for openapi docs
tags_metadata = [
    {
        "name": "General",
        "description": "General endpoints",
    },
]

app = FastAPI(openapi_url=OPENAPI_URL, openapi_tags=tags_metadata)

# Configure CORS
# CORS allow from all
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(general.router, tags=["General"])
# app.include_router(otherroute.router, tags=["Other route"])
# app.include_router(anotherroute.router, tags=["Another route"])
