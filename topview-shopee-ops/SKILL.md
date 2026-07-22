---
version: 0.2.0
name: topview-shopee-ops
description: |
  Shopee public market intelligence via unified host MCP `topview-mcp`
  (progressive disclosure: use_shopee_data → get_tool_schema → call_tool).
  Use when: Shopee site/category market analysis, item ranking/detail,
  shop/brand analysis, hot-search keyword research across Shopee sites
  (tw/my/id/th/ph/sg/vn/br).
  NOT for: Amazon, TikTok Shop, YouTube creators, or media generation
  (use topview-amazon-ops, topview-tiktok-shop-ops, topview-youtube-kol-ops,
  or topview-generate).
argument-hint: "[shopee research request] [--site] [--category|--item|--shop]"
metadata:
  tags: topview, shopee, ecommerce, mcp
  mcpServers:
    - topview-mcp
  endpoints:
    - https://mcp.topview.ai
---

# Topview Shopee Ops

Public Shopee intelligence via the host's unified **`topview-mcp`** server (progressive disclosure; domain `shopee`; deferred `queryshopee*` tools).

## Step 0 — Bootstrap

1. Confirm MCP server **`topview-mcp`** is connected (look for `use_shopee_data`, `get_tool_schema`, `call_tool`).
2. If missing, point the user to [`mcp.example.json`](../mcp.example.json) → `~/.cursor/mcp.json`, reload MCP.
3. **Do not** run `scripts/mcp_call.py`, open SSE yourself, or use curl/raw HTTP.

## Execution

Server: **`topview-mcp`** (unified). Never open SSE yourself.

Shopee data tools are **deferred**. Invoke via progressive disclosure:

1. Read the `use_shopee_data` description on `tools/list` (embedded Tools catalog). Calling `use_shopee_data` only to list tools is **optional**; call it once if the catalog says it is not loaded yet (Shopee proxy warm-up).
2. Pick a deferred `queryshopee*` name from the catalog or [references/tool_routing.md](references/tool_routing.md).
3. `get_tool_schema` with `{ "name": "<deferred>", "domain": "shopee" }`.
4. `call_tool` with `{ "name": "<deferred>", "domain": "shopee", "arguments": { ... } }`.

Typical host tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Resolve category/item/shop/brand IDs before batch detail. Always confirm site + date window when required.

## UX Rules

1. Be concise; lead with findings.
2. Ask for site / category / ids when missing.
3. Do not invent private shop ads/order/profit data.
4. Creative production → `topview-generate`.
5. Match the user's language.

## Source

Adapted from Marketing Studio Shopee expert skills (V060/V061).
