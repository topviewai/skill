# Topview AI Skills

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](./LICENSE.txt)
[![Version](https://img.shields.io/badge/version-0.2.0-green.svg)](./VERSION)

Agent skills for [Topview AI](https://www.topview.ai): media generation plus ecommerce / KOL research. Layout follows the [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills) multi-skill collection pattern.

**Skills call the unified host MCP `topview-mcp`** (Cursor / Codex / Claude Code). They do **not** open their own MCP SSE sessions via Python.

- **Ops (data):** progressive disclosure — read `use_*` catalog → `get_tool_schema` → `call_tool`.
- **Generate (creative):** call `topview_*` / `ta_*` hot tools **directly** through `topview-mcp`; there is no non-MCP fallback.

## Install skills

```bash
npx skills add topviewai/skill
# or
git clone https://github.com/topviewai/skill.git && cd skill && ./setup
```

## Register MCP server (required)

Copy [`mcp.example.json`](./mcp.example.json) into `~/.cursor/mcp.json` (or the host equivalent). Sign in with Cursor OAuth (or the host's `mcp_auth` flow).

| Skill | MCP server id |
|-------|---------------|
| `topview-generate` | `topview-mcp` |
| `topview-tiktok-shop-ops` | `topview-mcp` |
| `topview-amazon-ops` | `topview-mcp` |
| `topview-shopee-ops` | `topview-mcp` |
| `topview-youtube-kol-ops` | `topview-mcp` |

Reload MCP, then confirm surface tools appear: `use_amazon_data` / `use_shopee_data` / `use_tiktok_data` / `use_youtube_kol`, `get_tool_schema`, `call_tool`, and `topview_*` / `ta_*`. Deferred data tools (`market_research`, `td_*`, `queryshopee*`, `youtube_kol_*`) are invoked via `call_tool`, not as top-level listings.

Production URL: `https://mcp.topview.ai`.

## Skills

| Skill | Description |
|-------|-------------|
| [`topview-generate`](./topview-generate) | Videos, images, avatars, TTS, voices, and boards via direct MCP `topview_*` / `ta_*` tools |
| [`topview-amazon-ops`](./topview-amazon-ops) | Amazon intelligence via `topview-mcp` (`use_amazon_data` → `call_tool`) |
| [`topview-tiktok-shop-ops`](./topview-tiktok-shop-ops) | TikTok Shop via `topview-mcp` (`use_tiktok_data` → `call_tool`) |
| [`topview-shopee-ops`](./topview-shopee-ops) | Shopee via `topview-mcp` (`use_shopee_data` → `call_tool`) |
| [`topview-youtube-kol-ops`](./topview-youtube-kol-ops) | YouTube KOL pool via `topview-mcp` (`use_youtube_kol` → `call_tool`) |

## Quick Reference

| What you want | Skill |
|---------------|-------|
| Generate image / video / avatar / TTS | `topview-generate` |
| Amazon market / ASIN / keywords / reviews | `topview-amazon-ops` |
| TikTok Shop product / trend / affiliate | `topview-tiktok-shop-ops` |
| Shopee category / shop / brand / keywords | `topview-shopee-ops` |
| YouTube creators from Topview pool | `topview-youtube-kol-ops` |

## Auth

Credentials are managed by the host MCP connection. Cursor uses OAuth;
other hosts should use their `mcp_auth` flow when sign-in is required.

## License

Apache-2.0 — see [LICENSE.txt](./LICENSE.txt).
