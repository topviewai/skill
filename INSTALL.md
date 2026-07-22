# Install Topview Skills

## 1. Install skill packages

```bash
npx skills add topviewai/skill
# or
./setup
```

## 2. Register MCP server

All skills share one host-registered MCP. Merge [`mcp.example.json`](./mcp.example.json) into:

- Cursor: `~/.cursor/mcp.json`
- Codex / Claude: the host's MCP config path

Reload MCP, then verify `topview-mcp` exposes:

- Domain entry: `use_amazon_data`, `use_shopee_data`, `use_tiktok_data`, `use_youtube_kol`
- Meta: `get_tool_schema`, `call_tool`
- Creative hot tools: `topview_*`, `ta_*`

Production URL: `https://mcp.topview.ai`.

## Verify

Ask the agent (with MCP connected):

> Use topview-amazon-ops and research the US wireless earbuds market opportunity.

The agent should use host MCP meta-tools (`get_tool_schema` / `call_tool` with deferred name `market_research`, domain `amazon`), not `mcp_call.py` or a separate amazon-mcp server.

For generation, the agent should call `topview_*` / `ta_*` directly on `topview-mcp`; it should not use the data-domain meta-tools or bundled REST scripts.
