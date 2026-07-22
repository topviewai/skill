# Background Removal

Remove an image background with `topview_remove_background`. This is commonly
the first step in the Product Avatar workflow.

## Request

Upload a local product image first, then call:

```json
{
  "req": {
    "productImageFileId": "file_product"
  }
}
```

If the user supplies a hand-painted mask, upload it and include:

```json
{
  "req": {
    "productImageFileId": "file_product",
    "productImageMaskFileId": "file_mask"
  }
}
```

## Polling

```json
{
  "req": {
    "taskType": "remove_background",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Keep polling the same task until terminal status. Follow
[the common workflow](../SKILL.md#common-agent-workflow) for upload and timeout
recovery.

## Result Fields

| Field | Use |
|---|---|
| `bgRemovedImageFileId` | Background-removed Topview file ID |
| `bgRemovedImagePath` | Downloadable result URL |
| `bgRemovedImageWidth` / `bgRemovedImageHeight` | Result dimensions |
| `maskImageFileId` / `maskImagePath` | Generated mask |
| `costCredit` | Credits consumed |

## Product Avatar Chaining

Pass `bgRemovedImageFileId` directly as
`productImageWithoutBackgroundFileId` in `topview_product_avatar`. Do not
download and upload the intermediate image again unless the returned file ID is
unusable.

See [Product Avatar](product_avatar.md) for template discovery and placement.
