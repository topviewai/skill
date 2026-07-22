---
version: 0.2.0
name: topview-amazon-ops
description: |
  Amazon public market intelligence via unified host MCP `topview-mcp`
  (progressive disclosure: use_amazon_data → get_tool_schema → call_tool).
  Use when: Amazon market/category research, ASIN/product screening,
  competitor lookup, listing/keyword/traffic analysis, review VOC,
  trend or trademark risk checks, SellerSprite-style public Amazon data.
  NOT for: TikTok Shop, Shopee, YouTube creator pool, or video/image/avatar
  generation (use topview-tiktok-shop-ops, topview-shopee-ops,
  topview-youtube-kol-ops, or topview-generate).
argument-hint: "[amazon research request] [--marketplace] [--asin|--keyword]"
metadata:
  tags: topview, amazon, ecommerce, mcp, market-research
  mcpServers:
    - topview-mcp
  endpoints:
    - https://mcp.topview.ai
---

# Topview Amazon Ops

Public Amazon market / ASIN / keyword intelligence through the host's unified **`topview-mcp`** server (progressive disclosure; domain `amazon`).

## Step 0 — Bootstrap

1. Confirm the host already has MCP server **`topview-mcp`** connected (look for `use_amazon_data`, `get_tool_schema`, `call_tool`).
2. If tools are missing, tell the user to add the server from repo [`mcp.example.json`](../mcp.example.json) into `~/.cursor/mcp.json`, reload MCP — then retry.
3. **Do not** run `scripts/mcp_call.py`, open SSE yourself, or use curl/raw HTTP.

## Execution

Server: **`topview-mcp`** (unified). Never open SSE yourself.

Amazon data tools are **deferred** — they do not appear as top-level `tools/list` entries. Invoke via progressive disclosure:

1. Read the `use_amazon_data` description on `tools/list` (embedded Tools catalog). Calling `use_amazon_data` only to list tools is **optional**; call it once if the catalog says it is not loaded yet (Amazon proxy warm-up).
2. Pick a deferred tool name from the catalog or [references/tool_routing.md](references/tool_routing.md).
3. `get_tool_schema` with `{ "name": "<deferred>", "domain": "amazon" }`.
4. `call_tool` with `{ "name": "<deferred>", "domain": "amazon", "arguments": { ... } }`.

Typical host tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool` (Cursor may prefix `user-`).  
Do **not** assume deferred names like `market_research` are direct top-level tools. Creative tools (`topview_*` / `ta_*`) are on the same server but belong to `topview-generate` — call those directly, never via `call_tool`.

## UX Rules

1. Be concise; lead with findings, not RPC noise.
2. Ask for marketplace / category / ASIN / keyword when required by the tool schema.
3. Never invent private Seller Central Ads/order/profit numbers.
4. Match the user's language.
5. After analysis, if the user wants creatives, chain to `topview-generate`.

## Source

Routing adapted from Marketing Studio Amazon expert skills (V032).
