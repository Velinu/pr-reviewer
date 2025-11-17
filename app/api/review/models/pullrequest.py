from pydantic import BaseModel

class PullRequestData(BaseModel):
    title: str
    description: str
    diffs: str
    files: list[str]
    author: str
