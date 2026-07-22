# Contributing

## Branching

- Base branch: `main`
- Do not commit feature work directly on `main`
- Use feature branches, e.g. `feat/multi-skill-mcp-ops`

## Ops skills vs generate

- All skills share unified host MCP **`topview-mcp`** (`mcp.example.json` / `~/.cursor/mcp.json`).
- Ops skills are **prompt + routing** with progressive disclosure (`use_*` → `get_tool_schema` → `call_tool`). Edit `SKILL.md` / `references/tool_routing.md`.
- `topview-generate` uses direct MCP `topview_*` / `ta_*` hot tools. Its legacy REST scripts remain in the repository but are not an agent execution path.

## Adding an ops skill

1. Create `topview-<name>/SKILL.md` + `references/tool_routing.md` (domain id, progressive invocation, deferred tool names)
2. Keep `mcp.example.json` on the single `topview-mcp` entry; add the skill to `./setup` skill list
3. Update root `README.md` / `INSTALL.md` / `VERSION`

## Do not commit

Local API dumps (`*API.md`, PDFs) and `topview-skill-workspace/` unless intentionally part of the change.
