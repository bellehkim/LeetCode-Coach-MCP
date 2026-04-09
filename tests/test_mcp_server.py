from __future__ import annotations

import asyncio

from src import main as main_module


def test_mcp_server_registers_expected_tools() -> None:
	async def get_tool_names() -> list[str]:
		tools = await main_module.mcp.list_tools()
		return [tool.name for tool in tools]

	tool_names = asyncio.run(get_tool_names())

	assert main_module.mcp.name == "leetcode-coach-mcp"
	assert tool_names == [
		"analyze_problem_tool",
		"classify_patterns_tool",
		"generate_hints_tool",
		"generate_followups_tool",
	]


def test_main_uses_stdio_transport(monkeypatch) -> None:
	called: dict[str, str] = {}

	def fake_run(*, transport: str) -> None:
		called["transport"] = transport

	monkeypatch.setattr(main_module.mcp, "run", fake_run)

	main_module.main()

	assert called == {"transport": "stdio"}