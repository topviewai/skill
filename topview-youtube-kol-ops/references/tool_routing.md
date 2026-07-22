# YouTube KOL MCP tool routing

Adapted from Marketing Studio `youtube-kol-ops-assistant` agent definition.

**Invoke via host MCP only** — unified server id `topview-mcp`.  
Do **not** use `scripts/mcp_call.py` or curl.

## Progressive invocation

| Field | Value |
|-------|--------|
| Server | `topview-mcp` |
| Domain | `youtube_kol` |
| Entry (optional list) | `use_youtube_kol` |
| Schema | `get_tool_schema` |
| Execute | `call_tool` |

```text
1) tools/list → read use_youtube_kol Tools catalog
   (calling use_youtube_kol to list is optional)
2) get_tool_schema { "name": "youtube_kol_discover", "domain": "youtube_kol" }
3) call_tool {
     "name": "youtube_kol_discover",
     "domain": "youtube_kol",
     "arguments": { "req": { "keyword": "..." } }
   }
```

Host meta-tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Deferred `youtube_kol_*` names are `call_tool.name` values — not top-level tools/list entries.

Only use `youtube_kol_*` tools for this skill (domain `youtube_kol`). This is **not** Modash / `use_creator_discovery`.

## Tools

| Tool | Purpose |
|------|---------|
| `youtube_kol_discover` | Discover creators by keyword (YouTube search + pool cross-check) |
| `youtube_kol_search` / `youtube_kol_list` | Filter or browse creators already in the pool |
| `youtube_kol_channel_detail` | Detail by YouTube channel id (`UC...`) |
| `youtube_kol_channel_detail_by_id` | Detail by internal numeric id from search/list |
| `youtube_kol_channel_videos` | Recent videos for a creator (YouTube channel id) |
| `youtube_kol_competitor_list` | Competitor tags |
| `youtube_kol_competitor_videos` | Competitor videos |
| `youtube_kol_competitor_channels` | Reverse channel lookup |
| `youtube_kol_auto_quote` | **Generate** a new AI quote (writes to DB) |
| `youtube_kol_auto_quote_saved` | **Read** the latest saved quote (read-only) |
| `youtube_kol_stats` | Pool size / funnel overview |

## Request rules

- For POST-style tools, pass one root object `req` and put API body fields inside `req` (e.g. `{"req":{"keyword":"..."}}`). Confirm with `get_tool_schema` when unsure.
- Never invent creator metrics. If a tool fails or returns empty, say so and suggest narrowing filters.
- Use `youtube_kol_auto_quote` only when the user wants a **new** quote reference. Prefer `youtube_kol_auto_quote_saved` to inspect existing quotes. Calling the write tool via `call_tool(name="youtube_kol_auto_quote")` counts as a write.

## Boundaries

- Merchant/brand facing: prefer analysis and recommendations over CRM execution.
- Do not send emails, bulk-import channels, or change cooperation status.
- Do not use other domains (`amazon` / `shopee` / `tiktok` / `creator_discovery`) or their `use_*` entry tools for YouTube KOL pool intents.
- Creative production → `topview-generate` (direct `topview_*` / `ta_*` — not via `call_tool`).
