# MCP Error Handling

Diagnose the error, preserve task identity, and give the user a short,
actionable explanation.

## Connection and Authentication

| Situation | Action |
|---|---|
| `topview-mcp` is disconnected | Ask the user to enable/reconnect it in the host; do not switch execution paths |
| Authentication required | Invoke host `mcp_auth`; share a URL only if returned |
| Authentication still denied after one retry | Report the access blocker and stop |
| Direct creative tool is missing | Ask the user to refresh/update the MCP connection; do not route it through deferred-tool wrappers |

## Service Error Codes

| Code | Meaning | Action |
|---|---|---|
| `4100` | Insufficient credit | Show balance with `topview_get_credit` and suggest recharging at [Topview](https://www.topview.ai/dashboard/home) |
| `4007` | An unfinished task already exists | Preserve the known task ID when available, wait, and check status; do not create duplicates |
| `4000` / `4001` / `4003` | Invalid parameter or model | Re-read live generation config, correct the request, and confirm material changes |
| `DURATION_EXCEEDS_MCP_LIMIT` | Video `duration` above MCP single-clip limit (~15s) | Do not retry the same submit. Call `topview_prepare_canvas_jump` (or ask whether to shorten duration for MCP). Explain Canvas has more features for long / multi-scene work; MCP remains available if they want a shorter clip |
| `5003` | Service busy | Retry the same safe call after 10–30 seconds; if persistent, ask before changing models |
| `5000` / `5001` | Internal service error | Retry once; if persistent, report temporary unavailability |
| `6001` | Safety or security rejection | Explain briefly and offer a compliant prompt revision |

Do not switch models after code `4000` or `4100` without user consent.

## Task Polling

Every status check must reuse the task type and ID returned when the task was
accepted:

```json
{
  "req": {
    "taskType": "text_to_video",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

| Situation | Action |
|---|---|
| `init` or `running` | Wait and call `topview_query_task` again |
| Polling timeout | Retain identifiers and continue later; timeout is not failure |
| `success` | Return output URLs and board link |
| `fail` | Read `errorMsg`; revise prompt/model only with user consent when material |
| Partial success | Return successful outputs and offer to retry only failed outputs |

Never blindly resubmit after a timeout. A new request can duplicate work and
consume credits. Resubmit only after a terminal failure or clear evidence that
the original request was never accepted.

## Upload Errors

1. Confirm the file format and size are supported.
2. Obtain a fresh upload credential if the URL expired.
3. Upload the bytes exactly as the returned credential specifies.
4. Call `ta_upload_check_file` for the same `fileId`.
5. Retry once; if verification still fails, report the upload blocker.

Typical accepted media include PNG, JPG/JPEG, BMP, WebP, MP3, WAV, M4A, MP4,
AVI, and MOV, but the live credential/tool validation is authoritative.

## User Reply

Lead with what happened and the next safe action. Do not paste transport traces
or raw payloads unless the user requests technical detail.
