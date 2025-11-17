from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.api.review.review_service import ReviewService

router = APIRouter()

class ReviewRequest(BaseModel):
    pr_url: str

@router.post("/")
async def review_pr(payload: ReviewRequest):
    try:
        review = await ReviewService().review_pull_request(payload.pr_url)
        return review
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
async def review_pr():
    try:
        """ review = await ReviewService().review_pull_request(payload.pr_url) """
        return "sdaf"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

