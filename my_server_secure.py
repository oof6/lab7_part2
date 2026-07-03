"""my_server_secure.py — SECURED version of your MCP server."""

from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-server")

# use abs resolution directly at initialization
NOTES_DIR = (Path(__file__).parent / "notes").resolve()


@mcp.tool()
def list_notes() -> str:
    """List the note files available to read."""
    try:
        NOTES_DIR.mkdir(exist_ok=True)
        return "\n".join(sorted(p.name for p in NOTES_DIR.glob("*.txt"))) or "(no notes)"
    except Exception as e:
        return f"Error listing notes: {str(e)}"


@mcp.tool()
def read_note(name: str) -> str:
    """Read a note securely from the notes/ directory. Prevent path traversal."""
    # Resolve abs reference layers
    target_path = (NOTES_DIR / name).resolve()
    
    # Enforce sandbox
    if not target_path.is_relative_to(NOTES_DIR):
        return "Error: Access denied. Cannot read files outside the notes directory."

    try:
        if not target_path.exists() or not target_path.is_file():
            return f"Error: Note '{name}' not found."
        return target_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading note: {str(e)}"


if __name__ == "__main__":
    mcp.run()
