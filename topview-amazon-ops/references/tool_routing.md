# Amazon MCP tool routing

Adapted from Marketing Studio skills (`amazon-market-analysis`, `amazon-product-analysis`, `amazon-listing-optimization`, `amazon-keyword-traffic-analysis`, `amazon-review-optimization`, `amazon-trend-risk-monitor`).

**Invoke via host MCP only** — unified server id `topview-mcp` (see `~/.cursor/mcp.json` / repo `mcp.example.json`).  
Do **not** use `scripts/mcp_call.py` or curl.

## Progressive invocation

| Field | Value |
|-------|--------|
| Server | `topview-mcp` |
| Domain | `amazon` |
| Entry (optional list / warm-up) | `use_amazon_data` |
| Schema | `get_tool_schema` |
| Execute | `call_tool` |

```text
1) tools/list → read use_amazon_data Tools catalog
   (optional: call use_amazon_data if catalog not loaded)
2) get_tool_schema { "name": "market_research", "domain": "amazon" }
3) call_tool {
     "name": "market_research",
     "domain": "amazon",
     "arguments": { "request": { ... } }
   }
```

Host meta-tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Deferred names below are `call_tool.name` values — they are **not** top-level tools/list entries. Amazon arguments often wrap the body in `request` (confirm with `get_tool_schema`).

## Market analysis

- Start with `market_research` for market overview, demand, maturity and opportunity framing.
- Use `market_research_statistics` for category node statistics and top-N summaries.
- Concentration: `market_product_concentration`, `market_brand_concentration`, `market_seller_concentration`, `market_seller_type_concentration`, `market_seller_country_distribution`.
- Distribution: `market_price_distribution`, `market_rating_distribution`, `market_ratings_count_distribution`, `market_listing_date_distribution`, `market_listing_trend_distribution`, `market_ebc_distribution`.
- Trends only when asked: `market_product_demand_trend`, `keyword_research_trends`, `google_trend`.
- If keyword-only search returns empty, resolve browse node with `product_node` then retry with `nodeIdPath`.

## Product analysis

- `product_research` — conditional product search / screening.
- `competitor_lookup` — competitor / brand / seller / keyword / ASIN comparison.
- `asin_detail_with_coupon_trend`, `asin_sales_trend`, `keepa_info`, `product_node`.
- Forecast only when asked: `asin_prediction`, `bsr_prediction`.

## Listing optimization

- `traffic_keyword`, `traffic_listing`, `traffic_listing_stat`, `traffic_source`.
- `keyword_research`, `keyword_miner`, `keyword_research_trends`.
- `review`, `market_ebc_distribution`.

## Keyword / traffic

- `keyword_research`, `keyword_miner`, `keyword_research_trends`.
- ABA: `aba_research_weekly`, `aba_research_monthly`, `aba_research_trend`, `google_trend`.
- Traffic: `traffic_keyword`, `traffic_keyword_stat`, `traffic_listing`, `traffic_listing_stat`, `traffic_source`, `traffic_extend`, `keyword_order`.

## Review / risk

- `review` for VOC / rating distribution / pain points.
- `trademark_list`, `trademark_detail` for claim / infringement screening (not legal advice).

## Trend / risk monitor

- `market_product_demand_trend`, `keyword_research_trends`, `google_trend`.
- `asin_prediction`, `bsr_prediction`, `asin_sales_trend`.
- `trademark_list`, `trademark_detail`.

## Boundaries

- Do not invent private Seller Central revenue, inventory, Ads or profit. Ask for uploaded reports.
- If marketplace, category node, keyword or ASIN is missing, ask before calling tools.
- Do not use other domains (`tiktok` / `shopee` / `youtube_kol`) or their `use_*` entry tools for Amazon intents.
- For creative assets after analysis, chain to `topview-generate` (direct `topview_*` / `ta_*` on the same server — not via `call_tool`).
