from pydantic import BaseModel
from github import Github
import re
from app.config import Config

class PullRequestData(BaseModel):
    title: str
    description: str
    diffs: str
    files: list[str]
    author: str

class GitHubService:

    def __init__(self):
        self.client = Github(Config.GITHUB_TOKEN)

    def fetch_pull_request(self, pr_url: str) -> PullRequestData:
        # Extrair owner/repo/numero
        match = re.search(r"github\.com/(.*)/(.*)/pull/(\d+)", pr_url)
        if not match:
            raise Exception("Invalid PR URL")

        owner, repo, number = match.groups()

        repository = self.client.get_repo(f"{owner}/{repo}")
        pr = repository.get_pull(int(number))

        diffs = ""
        files = []

        for f in pr.get_files():
            diffs += f.patch or ""
            files.append(f.filename)

        return PullRequestData(
            title=pr.title,
            description=pr.body or "",
            diffs=diffs,
            files=files,
            author=pr.user.login,
        )
