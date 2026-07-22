---
version: 0.2.0
name: topview-tiktok-shop-ops
description: |
  TikTok Shop public intelligence via unified host MCP `topview-mcp`
  (progressive disclosure: use_tiktok_data → get_tool_schema → call_tool;
  deferred td_* tools).
  Use when: TikTok Shop market trends, product selection, viral material
  breakdown, scripts, content calendar, affiliate/creator ops, ads/live ops.
  NOT for: Amazon, Shopee, YouTube KOL pool, or media generation
  (use topview-amazon-ops, topview-shopee-ops, topview-youtube-kol-ops,
  or topview-generate).
argument-hint: "[tiktok shop research request] [--region] [--item|--keyword]"
metadata:
  tags: topview, tiktok, ecommerce, mcp, td
  mcpServers:
    - topview-mcp
  endpoints:
    - https://mcp.topview.ai
---

# Topview TikTok Shop Ops

TikTok Shop data via the host's unified **`topview-mcp`** server (progressive disclosure; domain `tiktok`; deferred `td_*` tools).

## Step 0 — Bootstrap

1. Confirm MCP server **`topview-mcp`** is connected (look for `use_tiktok_data`, `get_tool_schema`, `call_tool`). Do **not** expect `td_*` as top-level tools/list entries.
2. If missing, point the user to [`mcp.example.json`](../mcp.example.json) → `~/.cursor/mcp.json`, reload MCP.
3. **Do not** run `scripts/mcp_call.py`, open SSE yourself, or use curl/raw HTTP.

## Execution

Server: **`topview-mcp`** (unified). Never open SSE yourself.

TikTok data tools are **deferred**. Invoke via progressive disclosure:

1. Read the `use_tiktok_data` description on `tools/list` (embedded Tools catalog). Calling `use_tiktok_data` only to list tools is **optional**.
2. Pick a deferred `td_*` name from the catalog or [references/tool_routing.md](references/tool_routing.md).
3. `get_tool_schema` with `{ "name": "<td_*>", "domain": "tiktok" }`.
4. `call_tool` with `{ "name": "<td_*>", "domain": "tiktok", "arguments": { "req": { ... } } }` (confirm shape with schema).

Typical host tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Prefer `td_*` for market/item/creator/video/live intelligence. Do not use `use_amazon_data` / Amazon deferred names for TikTok intents.

## UX Rules

1. Be concise; lead with actionable findings.
2. Ask for region / category / product identifiers when missing.
3. Do not invent private shop-backend ads metrics.
4. For video/image/avatar production, chain to `topview-generate`.
5. Match the user's language.

## Source

Adapted from Marketing Studio TikTok Shop expert skills (V030) + topview-mcp.
