# TikTok Shop (topview MCP) tool routing

Adapted from Marketing Studio TikTok Shop skills and unified `topview-mcp` deferred `td_*` data tools.

**Invoke via host MCP only** — unified server id `topview-mcp`.  
Do **not** use `scripts/mcp_call.py` or curl.

## Progressive invocation

| Field | Value |
|-------|--------|
| Server | `topview-mcp` |
| Domain | `tiktok` |
| Entry (optional list) | `use_tiktok_data` |
| Schema | `get_tool_schema` |
| Execute | `call_tool` |

```text
1) tools/list → read use_tiktok_data Tools catalog
   (calling use_tiktok_data to list is optional)
2) get_tool_schema { "name": "td_item_v2_search", "domain": "tiktok" }
3) call_tool {
     "name": "td_item_v2_search",
     "domain": "tiktok",
     "arguments": { "req": { ... } }
   }
```

Host meta-tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Deferred `td_*` names are `call_tool.name` values — not top-level tools/list entries. Arguments commonly wrap the body in `req` (confirm with `get_tool_schema`).

Prefer `td_*` tools for public TikTok Shop intelligence.

## Market trend analysis

- Region / category / item ranking, item search, seller search and trend via `td_*` tools.
- Evaluate markets by GMV, sales, growth, creator participation, content intensity and category momentum.

## Product selection

- Score products by visual strength, pain point clarity, scene repeatability, commission, creator fit, sales growth, content supply and live/ad expansion potential.
- Prefer item search / ranking / detail / trend tools first (e.g. `td_item_v2_search` and related ranking/detail tools when available).

## Material breakdown

- Use item video, video statistics, video trend and AI insight `td_*` tools when available.
- Break down hook, first 3 seconds, scene, pain point, demonstration, proof, subtitle, CTA, creator style and fatigue risk.

## Script creation

- Generate bounded batches of hooks, UGC scripts, creator briefs, ad variants and live talk tracks from product evidence.
- For actual video/image/audio generation, chain to `topview-generate`.

## Content production

- Plan content by product, audience, angle, creator type, format, date and KPI.
- Delegate media generation to `topview-generate`.

## Affiliate ops

- Use creator and item-creator `td_*` tools when available.
- Build creator shortlist, outreach angle, sample plan, commission suggestion, tracking fields, ROI thresholds and follow-up cadence.

## Ads / live ops

- Use item, video, live, seller tools plus any uploaded ad/live reports as evidence.
- Separate organic content, paid ads and live room decisions.

## Boundaries

- Ask for region / category / product identifiers before calling tools when missing.
- Do not invent private seller ads or shop-backend metrics; ask for uploads.
- Do not use other domains (`amazon` / `shopee` / `youtube_kol`) or their `use_*` entry tools for TikTok Shop intents (e.g. do not `call_tool` `market_research` with `domain: amazon`).
- Creative production → `topview-generate`. Amazon/Shopee/YouTube KOL pool → their dedicated skills.
