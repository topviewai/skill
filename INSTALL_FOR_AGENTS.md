# Install Topview Skills (for agents)

Paste this into your coding agent:

1. Clone or update `https://github.com/topviewai/skill.git`.
2. Run `./setup` from the repo root (or `npx skills add topviewai/skill`).
3. Ensure the host already has unified Topview MCP **`topview-mcp`** registered per `mcp.example.json` / `~/.cursor/mcp.json` (surface tools: `use_*_data` / `use_youtube_kol`, `get_tool_schema`, `call_tool`, `topview_*`, `ta_*`). If not, ask the user to add it and reload MCP — do **not** run `mcp_call.py`.
4. For `topview-generate`: call `topview_*` / `ta_*` hot tools directly on `topview-mcp`. If the server requires authentication, use Cursor OAuth or the host `mcp_auth` flow — do **not** ask the user to export `TOPVIEW_UID` / `TOPVIEW_API_KEY`, and do not run bundled REST scripts.
5. Pick the right skill by intent:
   - Media generation → `topview-generate` (direct MCP hot tools)
   - Amazon / TikTok Shop / Shopee / YouTube KOL → corresponding `topview-*-ops` skill + progressive disclosure on **`topview-mcp`** (`use_*` catalog → `get_tool_schema` → `call_tool`)
6. Call tools only through the host MCP interface (never `mcp_call.py`, never raw curl). Do not assume deferred data tool names appear as top-level tools/list entries.
