from ..github.github_service import GitHubService
from ...llm.rag_service import RAGService
from ...llm.llm_service import LLMService

class ReviewService:

    async def review_pull_request(self, pr_url: str):
        # 1. Buscar PR no GitHub
        github = GitHubService()
        pr_data = github.fetch_pull_request(pr_url)

        # 2. Buscar contexto RAG
        rag = RAGService()
        context = rag.get_context(pr_data.diffs)

        # 3. Obter análise do Gemini
        llm = LLMService()
        review_result = llm.review_code(pr_data, context)

        return {
            "pull_request": pr_url,
            "review": review_result
        }
