---
version: 0.2.0
name: topview-youtube-kol-ops
description: |
  YouTube creator discovery and evaluation via unified host MCP `topview-mcp`
  (progressive disclosure: use_youtube_kol → get_tool_schema → call_tool;
  deferred youtube_kol_* tools from Topview's owned youtubeagent pool).
  Use when: find YouTube creators, channel detail, competitor creators,
  collaboration quote references from Topview's owned pool.
  NOT for: Amazon/Shopee/TikTok Shop data, Modash Instagram/YouTube
  creator-discovery MCP, or media generation (use other topview-*-ops
  or topview-generate).
argument-hint: "[youtube creator research] [--keyword] [--channelId]"
metadata:
  tags: topview, youtube, creator, kol, mcp
  mcpServers:
    - topview-mcp
  endpoints:
    - https://mcp.topview.ai
---

# Topview YouTube KOL Ops

Merchant-facing YouTube creator research via the host's unified **`topview-mcp`** server (progressive disclosure; domain `youtube_kol`).

## Step 0 — Bootstrap

1. Confirm MCP server **`topview-mcp`** is connected (look for `use_youtube_kol`, `get_tool_schema`, `call_tool`).
2. If missing, point the user to [`mcp.example.json`](../mcp.example.json) → `~/.cursor/mcp.json`, reload MCP.
3. **Do not** run `scripts/mcp_call.py`, open SSE yourself, or use curl/raw HTTP.

## Execution

Server: **`topview-mcp`** (unified). Never open SSE yourself.

YouTube KOL tools are **deferred**. Invoke via progressive disclosure:

1. Read the `use_youtube_kol` description on `tools/list` (embedded Tools catalog). Calling `use_youtube_kol` only to list tools is **optional**.
2. Pick a deferred `youtube_kol_*` name from the catalog or [references/tool_routing.md](references/tool_routing.md).
3. `get_tool_schema` with `{ "name": "<youtube_kol_*>", "domain": "youtube_kol" }`.
4. `call_tool` with `{ "name": "<youtube_kol_*>", "domain": "youtube_kol", "arguments": { "req": { ... } } }` (confirm shape with schema).

Typical host tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Prefer `youtube_kol_auto_quote_saved` over write tool `youtube_kol_auto_quote` unless the user explicitly wants a new saved quote.

## UX Rules

1. Prefer analysis and shortlists over CRM execution.
2. Never invent subscriber/metrics; report empty/failed tool results honestly.
3. Creative production → `topview-generate`.
4. Match the user's language.

## Source

Adapted from Marketing Studio `youtube-kol-ops-assistant` (V049).
