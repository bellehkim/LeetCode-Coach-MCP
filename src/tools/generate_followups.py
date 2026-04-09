from __future__ import annotations

from src.services.analyzers.followup_analysis import generate_followups as generate_followups_service
from src.services.analyzers.problem_analysis import JsonGenerationClient


def generate_followups(problem_text: str, client: JsonGenerationClient | None = None) -> dict[str, object]:
	return generate_followups_service(problem_text, client=client)
