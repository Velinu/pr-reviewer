from fastapi import FastAPI
from app.api.review.review_controller import router as review_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="AI Pull Request Reviewer",
        version="1.0.0",
        description="API for automated PR review using Gemini + RAG",
    )

    # Rotas
    app.include_router(review_router, prefix="/review")

    return app


app = create_app()
