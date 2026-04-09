from __future__ import annotations

from src.server import build_mcp_server

mcp = build_mcp_server()


def main() -> None:
	mcp.run(transport="stdio")


if __name__ == "__main__":
	main()
