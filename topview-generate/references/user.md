# Credits and Usage

Use Topview credit tools to check affordability before generation and explain
historical charges afterward.

## Current Balance

Call `topview_get_credit`:

```json
{
  "req": {}
}
```

Present the available balance in plain language. Do not expose unrelated
account metadata unless the user asks.

## Credit History

Call `topview_list_credit_logs`:

```json
{
  "req": {
    "pageNo": 1,
    "pageSize": 50,
    "taskType": "common_task_image2video",
    "startTime": "2026-07-01 00:00:00",
    "endTime": "2026-07-21 23:59:59"
  }
}
```

`taskType`, `startTime`, and `endTime` are optional filters. Times are UTC in
`yyyy-MM-dd HH:mm:ss` form unless the live schema says otherwise.

Common historical task types include:

| Value | Meaning |
|---|---|
| `m2v` | Marketing video |
| `common_task_image2video` | Image to video |
| `video_avatar` | Video avatar |
| `product_avatar_image2video` | Product avatar |
| `voice_clone` | Voice clone |
| `product_anyfit` | Product AnyShoot |

For pre-generation confirmation and cost communication, follow
[Cost and Confirmation Guidance](../SKILL.md#cost-and-confirmation-guidance).
