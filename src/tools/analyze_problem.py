from __future__ import annotations

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.services.analyzers.problem_analysis import JsonGenerationClient
from src.types.contracts import ToolResult


def analyze_problem(problem_text: str, client: JsonGenerationClient | None = None) -> dict:
	response = analyze_problem_text(problem_text, client=client)
	return ToolResult(
		result=response.coaching,
		cleaned_problem=response.cleaned_problem,
	).model_dump()
