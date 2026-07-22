# AI Image Generation

Generate images from text or edit existing images with
`topview_generate_image`.

## Task Types

| `taskType` | Use | Core inputs |
|---|---|---|
| `text_to_image` | Create from a prompt | `model`, `prompt` |
| `image_edit` | Edit or remix references | `model`, `prompt`, `inputImageFileIds` |
| `storyboard` | Create storyboard keyframes | `model`, `story`, `resolution` |

## MCP Sequence

First call `topview_get_generation_config` for the intended task:

```json
{
  "req": {
    "type": "image",
    "taskType": "text_to_image"
  }
}
```

Select `models[].submitModel` exactly. Live
`requiredSubmitFields`, `submitParameterOptions`, and
`defaultSubmitParameters` override static examples below.

Text-to-image request:

```json
{
  "req": {
    "taskType": "text_to_image",
    "model": "<submitModel>",
    "prompt": "A futuristic city skyline at dusk, neon lights reflected on wet streets",
    "aspectRatio": "16:9",
    "resolution": "2K",
    "generateCount": 2,
    "boardId": "board_123"
  }
}
```

Image-edit request after uploading local references:

```json
{
  "req": {
    "taskType": "image_edit",
    "model": "<submitModel>",
    "prompt": "Change the background to a snowy mountain landscape",
    "aspectRatio": "16:9",
    "resolution": "2K",
    "inputImageFileIds": ["file_photo"],
    "generateCount": 1,
    "boardId": "board_123"
  }
}
```

Poll the returned task with `topview_query_task`:

```json
{
  "req": {
    "taskType": "text_to_image",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Use the exact task type from the generation request. The common upload, board,
and timeout behavior is in
[SKILL.md](../SKILL.md#common-agent-workflow).

## Parameter Semantics

- `model`: machine submit value from live config, not necessarily the display
  name.
- `prompt`: required for text generation and editing.
- `aspectRatio`: use a supported config value such as `16:9`, `1:1`, or `auto`.
- `resolution`: model-dependent; include it only when supported or required.
- `quality`: include only when listed by the selected model.
- `generateCount`: 1–4, default 1.
- `inputImageFileIds`: uploaded Topview file IDs for editing.
- `boardId`: selected session board.

## Model Recommendation

Prefer the live config's selection policy. When compatible and the user did not
specify a model, **GPT Image 2** is the default: strong text rendering,
all-round quality, many aspect ratios, 1K/2K/4K output, and multi-image editing.

| Use case | Model guidance |
|---|---|
| Best overall / text rendering | GPT Image 2 |
| Raw image fidelity | Nano Banana 2 |
| Lower-cost fidelity | Nano Banana 2 Lite |
| High detail | Seedream 5.0 Pro |
| Budget high resolution | Seedream 5.0 Lite |
| Multi-image editing plus 4K | Kling V3 Omni |
| Quality-tier control | GPT Image 2 or Reve Image family |
| No-resolution simplicity | Kontext-Pro or Imagen 4 |

Historical constraints, to be verified against live config:

- GPT Image 2: `1K`, `2K`, or `4K`; up to 16 edit inputs; optional
  `low`/`medium`/`high` quality.
- Nano Banana 2 Lite: fixed `1K`.
- Seedream 5.0 Pro: `1K`/`2K`, `auto` ratio, up to 14 edit inputs.
- Seedream 5.0 Lite: fixed `2K`; `Seedream 5.0` may be a compatibility alias.
- Kling V3 Omni: `1K`/`2K`/`4K`, up to 10 edit inputs.
- Reve Image Remix: editing only, up to 6 references, optional quality.
- Imagen 4: text-to-image only.

Do not pass unsupported fields. If Topview rejects the model or parameters,
report the validation message and offer compatible values from the same live
config.
