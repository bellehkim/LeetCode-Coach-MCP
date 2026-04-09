from __future__ import annotations

from mcp.server.fastmcp import FastMCP

from src.config import get_settings
from src.services.analyzers.problem_analysis import JsonGenerationClient
from src.tools.analyze_problem import analyze_problem
from src.tools.classify_patterns import classify_patterns
from src.tools.generate_followups import generate_followups
from src.tools.generate_hints import generate_hints


def build_mcp_server(*, client: JsonGenerationClient | None = None) -> FastMCP:
	settings = get_settings()
	instructions = (
		"LeetCode Coach MCP helps candidates reason through coding interview problems. "
		"It focuses on patterns, brute force to optimal thinking, hints, and interviewer-style follow-ups."
	)

	mcp = FastMCP(name=settings.mcp_server_name, instructions=instructions)

	@mcp.tool(description="Analyze a LeetCode-style problem and return full interview coaching output.")
	def analyze_problem_tool(problem_text: str) -> dict:
		return analyze_problem(problem_text, client=client)

	@mcp.tool(description="Return the most relevant algorithm patterns for a LeetCode-style problem.")
	def classify_patterns_tool(problem_text: str) -> dict[str, object]:
		return classify_patterns(problem_text, client=client)

	@mcp.tool(description="Return progressive hints for a LeetCode-style problem.")
	def generate_hints_tool(problem_text: str) -> dict[str, list[str]]:
		return generate_hints(problem_text, client=client)

	@mcp.tool(description="Return likely interviewer follow-ups, hints, and common mistakes.")
	def generate_followups_tool(problem_text: str) -> dict[str, object]:
		return generate_followups(problem_text, client=client)

	return mcp