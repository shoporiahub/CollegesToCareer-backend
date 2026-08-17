from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.auth.router import router as auth_router
from app.certification.router import router as certification_router
from app.core.config import settings
from app.core.exceptions import ResumeAIException
from app.core.handlers import (
    resume_ai_exception_handler,
    unhandled_exception_handler,
)
from app.education.router import router as education_router
from app.experience.router import router as experience_router
from app.language.router import router as language_router
from app.project.router import router as project_router
from app.render.router import router as render_router
from app.resumes.router import router as resume_router
from app.skill.router import router as skill_router
from app.achievement.router import router as achievement_router

from app.contact.router import router as contact_router

from app.template.routes import router as template_router

from app.routes.upload import router as upload_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend API for Resume AI Platform",
)

# Static Files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router)

app.include_router(resume_router)

app.include_router(education_router)

app.include_router(experience_router)

app.include_router(project_router)

app.include_router(skill_router)

app.include_router(certification_router)

app.include_router(language_router)

app.include_router(render_router)

app.include_router(contact_router)

app.include_router(achievement_router)

app.include_router(template_router)

app.include_router(upload_router)


# Exception Handlers
app.add_exception_handler(
    ResumeAIException,
    resume_ai_exception_handler,
)

app.add_exception_handler(
    Exception,
    unhandled_exception_handler,
)


@app.get("/", tags=["Root"])
def root():
    return {
        "success": True,
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "success": True,
        "status": "healthy",
    }