# Boards

Boards organize generated images, videos, and audio. Use only the four direct
board tools exposed by `topview-mcp`.

## Available Operations

| Tool | Purpose |
|---|---|
| `topview_list_boards` | List boards with pagination |
| `topview_create_board` | Create a named board |
| `topview_list_board_tasks` | List generated tasks in a board |
| `topview_get_board_task` | Read one board task |

Board rename/update and deletion are unavailable through this MCP surface.

## Request Examples

List boards:

```json
{
  "req": {
    "pageNo": 1,
    "pageSize": 20
  }
}
```

Create a board:

```json
{
  "req": {
    "name": "Campaign Q3"
  }
}
```

List recent video tasks:

```json
{
  "req": {
    "boardId": "board_123",
    "mediaType": "video",
    "sortField": "gmtCreate",
    "sortOrder": "desc",
    "pageNo": 1,
    "pageSize": 50
  }
}
```

Get one board task:

```json
{
  "req": {
    "taskId": "task_abc123"
  }
}
```

Optional task-list filters may include `mediaType` (`image` or `video`),
`rating` (0–3), `toolCategory`, and `toolType`. Follow the host-exposed schema
if it differs from an optional example field.

## Board Selection

Unless the user supplied a board:

1. Call `topview_list_boards`.
2. Prefer `isSystemDefault=true`.
3. Otherwise prefer the exact name `My First Board`.
4. Otherwise use the first board.
5. If none exists, create one.
6. Pass the selected `boardId` to every compatible generation request in the
   session.

## Web Links

Board:

```text
https://www.topview.ai/board/{boardId}
```

Specific generated result:

```text
https://www.topview.ai/board/{boardId}?boardResultId={boardTaskId}
```

Use `boardTaskId`, not the generation `taskId`, in `boardResultId`.

For upload, generation, and polling behavior, follow
[the common workflow](../SKILL.md#common-agent-workflow).
