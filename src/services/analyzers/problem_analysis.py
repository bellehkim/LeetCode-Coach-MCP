from __future__ import annotations

from typing import Protocol

from src.services.cleaners.problem_cleaner import clean_problem_text
from src.services.llm.claude_client import ClaudeClient
from src.services.llm.prompts import build_problem_analysis_prompt
from src.types.contracts import AnalysisRequest, AnalysisResponse, CoachingOutput


class JsonGenerationClient(Protocol):
    def generate_json(self, prompt: str) -> dict: ...


class ProblemAnalysisService:
    def __init__(self, client: JsonGenerationClient | None = None) -> None:
        self.client = client or ClaudeClient()

    def analyze(self, request: AnalysisRequest) -> AnalysisResponse:
        cleaned_problem = clean_problem_text(request.problem_text)
        prompt = build_problem_analysis_prompt(cleaned_problem)
        raw_payload = self.client.generate_json(prompt)
        coaching = CoachingOutput.model_validate(raw_payload)
        return AnalysisResponse(
            coaching=coaching,
            cleaned_problem=cleaned_problem,
            raw_response=raw_payload,
        )


def analyze_problem_text(problem_text: str, client: JsonGenerationClient | None = None) -> AnalysisResponse:
    service = ProblemAnalysisService(client=client)
    return service.analyze(AnalysisRequest(problem_text=problem_text))