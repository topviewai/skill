# Shopee MCP tool routing

Adapted from Marketing Studio skills (`shopee-market-analysis`, `shopee-product-analysis`, `shopee-shop-analysis`, `shopee-brand-analysis`, `shopee-keyword-analysis`).
Tool names are lowercase `queryshopee*` from the deferred Shopee catalog.

**Invoke via host MCP only** — unified server id `topview-mcp`.  
Do **not** use `scripts/mcp_call.py` or curl.

## Progressive invocation

| Field | Value |
|-------|--------|
| Server | `topview-mcp` |
| Domain | `shopee` |
| Entry (optional list / warm-up) | `use_shopee_data` |
| Schema | `get_tool_schema` |
| Execute | `call_tool` |

```text
1) tools/list → read use_shopee_data Tools catalog
   (optional: call use_shopee_data if catalog not loaded)
2) get_tool_schema { "name": "queryshopeecatdata", "domain": "shopee" }
3) call_tool {
     "name": "queryshopeecatdata",
     "domain": "shopee",
     "arguments": { ... }
   }
```

Host meta-tool ids: `mcp__topview-mcp__get_tool_schema` / `mcp__topview-mcp__call_tool`.  
Deferred `queryshopee*` names are `call_tool.name` values — not top-level tools/list entries.

Always pass required site (`tw`/`my`/`id`/`th`/`ph`/`sg`/`vn`/`br`) and date window when the schema requires it.

## Market analysis

- Category tree: `queryshopeelevel1categories`, `queryshopeelevel2categories`, `queryshopeelevel3categories`.
- Overview: `queryshopeesitedate`, `queryshopeecatdata`, `queryshopeesubcatdata`.
- Ranking/trend: `queryshopeecatranking`, `queryshopeecattrend`, `queryshopeecategorytrendoverview`.
- Structure: `queryshopeecatpricedistribute`.

## Product analysis

- Screening/ranking: `queryshopeeitemdata`, `queryshopeeitemranking`.
- Detail: `queryshopeeitemdetailbatch`.
- Trend: `queryshopeeitemtrend`, `queryshopeeitemtrenddetail`.
- Related demand: `queryshopeeitemhotword`.

## Shop analysis

- Screening/ranking: `queryshopeeshopdata`, `queryshopeeshopranking`.
- Detail: `queryshopeeshopdetailbatch`.
- Trend: `queryshopeeshoptrend`, `queryshopeeshoptrenddetail`.
- Assortment: `queryshopeeshopitemlist`, `queryshopeeshopitempricedistribute`, `queryshopeeshopcatdistribute`, `queryshopeeshopbrandanalysis`.

## Brand analysis

- Screening/ranking: `queryshopeebranddata`, `queryshopeebrandranking`.
- Detail: `queryshopeebranddetailbatch`.
- Trend: `queryshopeebrandtrend`, `queryshopeebrandtrenddetail`.
- Structure: `queryshopeebranditemlist`, `queryshopeebrandshoplist`, `queryshopeebrandpricedistribute`, `queryshopeebrandsitedistribute`, `queryshopeebrandcategorydistribute`.

## Keyword analysis

- Screening/ranking: `queryshopeeworddata`, `queryshopeewordranking`.
- Detail: `queryshopeeworddetailbatch`.
- Trend: `queryshopeewordtrend`.
- Related items: `queryshopeeworditemlist`.

## Boundaries

- Resolve category/item/shop/brand IDs via ranking/search before batch detail.
- Do not invent private shop ads, orders, inventory or profit.
- Do not use other domains (`amazon` / `tiktok` / `youtube_kol`) or their `use_*` entry tools for Shopee intents.
- Creative assets → chain `topview-generate` (direct `topview_*` / `ta_*` — not via `call_tool`).
