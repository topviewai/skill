# Product Avatar

Place a product into a digital-human or model scene.

## Recommended Workflow

1. Call `topview_list_product_avatar_categories`.
2. Call `topview_list_product_avatars` with useful filters.
3. Upload the product and call `topview_remove_background`.
4. Poll `remove_background` and retain `bgRemovedImageFileId`.
5. Call `topview_product_avatar` with that file ID and the selected
   `avatarId`, or upload a custom template and use `templateImageFileId`.
6. Poll `product_avatar` to completion.

If the product already has a valid background-removed Topview file ID, skip
steps 3–4.

## Template Discovery

Categories:

```json
{
  "req": {}
}
```

Avatars:

```json
{
  "req": {
    "gender": "female",
    "categoryIds": "category_1,category_2",
    "ethnicityIds": "ethnicity_1",
    "sortingType": "Popularity",
    "pageNo": 1,
    "pageSize": 20
  }
}
```

`sortingType` supports `Popularity` and `Newest`. Treat filters as optional and
follow the live host schema for array-versus-comma-separated representations.
Show preview images when available so the user can choose.

## Automatic Placement

Preserve the model pose:

```json
{
  "req": {
    "avatarId": "avatar_123",
    "productImageWithoutBackgroundFileId": "file_product_nobg",
    "generateImageMode": "auto",
    "keepTarget": "model",
    "boardId": "board_123"
  }
}
```

Use `"keepTarget": "product"` when preserving product appearance matters more
than preserving the model.

## Custom Template or Manual Placement

```json
{
  "req": {
    "templateImageFileId": "file_template",
    "productImageWithoutBackgroundFileId": "file_product_nobg",
    "generateImageMode": "manual",
    "version": "v4",
    "location": [[10.5, 20.0], [30.5, 40.0]],
    "imageEditPrompt": "Keep the product label sharp and readable",
    "boardId": "board_123"
  }
}
```

Manual mode requires `location` and is intended for V4 coordinate-based
placement.

## Polling

```json
{
  "req": {
    "taskType": "product_avatar",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Follow [the common workflow](../SKILL.md#common-agent-workflow) for uploads,
boards, and timeout recovery.

## Parameter Guidance

| Field | Meaning |
|---|---|
| `avatarId` / `templateImageFileId` | Public/private avatar or uploaded template; provide one |
| `productImageWithoutBackgroundFileId` | Required background-removed product |
| `generateImageMode` | `auto` or `manual` |
| `keepTarget` | `model` or `product` in auto mode |
| `location` | Product coordinate matrix in manual mode |
| `version` | `v3` or `v4`; manual placement uses `v4` |
| `userFaceImageFileId` | Optional uploaded face replacement |
| `imageEditPrompt` | Optional placement/edit instruction |
| `productSize` | Optional supported product-size enum |

Historical pricing is **0.5 credits per task**, with failed tasks refunded.
Verify current pricing when the live response or account policy provides it.
