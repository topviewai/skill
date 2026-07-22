# Authentication

Topview authentication is owned by the host that connects `topview-mcp`, not
by this skill.

## Host Configuration

The host authenticates via OAuth (Cursor) or its `mcp_auth` flow. Credential
storage, refresh, logout, and protection are host concerns. Do not ask the user
to export `TOPVIEW_UID` / `TOPVIEW_API_KEY`, and do not claim that this skill
writes or manages a credential file.

## Authentication Recovery

When a Topview MCP tool reports an authentication or authorization error:

1. Invoke the host-provided `mcp_auth` action for `topview-mcp`.
2. If `mcp_auth` returns an authorization URL, send that exact URL to the user.
3. If it returns host instructions instead, ask the user to complete that
   host-provided sign-in action.
4. Never invent a URL or promise that one will be returned.
5. Wait for the user to confirm sign-in, then retry the original tool call once.
6. If authentication is still denied, report the blocker and stop.

## User-Facing Guidance

- Keep the message short: “Please sign in to Topview, then reply ‘done’.”
- Match the user's language.
- Do not refer to an invisible popup, terminal, or another machine.
- Do not ask the user to choose among authentication methods unless the host
  itself requires a choice.
- If the host displays the sign-in action only in its own UI, tell the user
  where the host says to complete it; do not substitute an unrelated link.

The common MCP workflow remains in [SKILL.md](../SKILL.md#common-agent-workflow).
