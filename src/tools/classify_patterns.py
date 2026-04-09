from __future__ import annotations

from src.services.analyzers.pattern_analysis import classify_patterns as classify_patterns_service
from src.services.analyzers.problem_analysis import JsonGenerationClient


def classify_patterns(problem_text: str, client: JsonGenerationClient | None = None) -> dict[str, object]:
	return classify_patterns_service(problem_text, client=client)
