from __future__ import annotations

from src.services.analyzers.problem_analysis import analyze_problem_text
from src.services.analyzers.problem_analysis import JsonGenerationClient


def generate_hints(problem_text: str, client: JsonGenerationClient | None = None) -> dict[str, list[str]]:
	response = analyze_problem_text(problem_text, client=client)
	return {"hint_sequence": response.coaching.hint_sequence}
