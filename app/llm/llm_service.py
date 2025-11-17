from ..api.review.models.pullrequest import PullRequestData
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import Config

class LLMService:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=Config.GEMINI_API_KEY
        )

        with open("app/prompts/review_prompt.md", "r") as f:
            self.base_prompt = f.read()

    def review_code(self, pr: PullRequestData, context: str):
        filled_prompt = self.base_prompt\
            .replace("{{context}}", context)\
            .replace("{{diff}}", pr.diffs)\
            .replace("{{title}}", pr.title)\
            .replace("{{description}}", pr.description)\

        response = self.llm.invoke(filled_prompt)
        return response.content
