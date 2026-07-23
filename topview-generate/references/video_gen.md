# Video Generation

Generate short clips with `topview_generate_video`. For longer finished videos,
prefer Canvas via `topview_prepare_canvas_jump`.

## Duration and Canvas Routing

| Intent | Default action |
|---|---|
| Ordinary video ≤15s (within the selected model's duration options) | `topview_generate_video` |
| Talking-head / digital-human narration | `topview_avatar_video` |
| >15s, long-form, or multi-scene finished video | Do **not** blind-call `topview_generate_video`. Call `topview_prepare_canvas_jump`, give the user `canvasUrl`, and explain they can still use topview-mcp (e.g. shorten to a supported duration and call `topview_generate_video`), but **Canvas has more features and usually better finished results** (storyboard, multi-scene, asset organization, iterative edit). If they then insist on MCP, follow MCP. |
| User explicitly asks for Canvas | `topview_prepare_canvas_jump` even when ≤15s |

### After MCP success (soft recommend, no prefill)

When delivering a successful `topview_generate_video` or `topview_avatar_video`
result, you may briefly suggest continuing in Topview Canvas for multi-scene
polish. Use **only** the bare link `https://www.topview.ai/canvas`. Do **not**
call `topview_prepare_canvas_jump` and do **not** invent `?prompt=` / `?sid=`
URLs for this soft recommend.

### Prefill jump (`topview_prepare_canvas_jump`)

Aligns with Marketing Studio Canvas prefill. Required `prompt`; optional
`aspectRatio`, `duration`, `templateId`, `source` (defaults to
`topview-generate`), and optional `images` / `videos` with Canvas agent-bucket
`s3Path` assets (max 8 images, 4 videos, 10 total). Public material URLs belong
inside `prompt` as `Reference Video URL：...` / `Products / Other Materials：...`.

```json
{
  "req": {
    "prompt": "30s vertical product ad ...",
    "aspectRatio": "9:16",
    "duration": 30,
    "source": "topview-generate"
  }
}
```

Return the tool's `canvasUrl` (`https://www.topview.ai/canvas?sid=...`) to the
user. Canvas only accepts `sid` prefill — never hand-build `?prompt=` links.

## Input-Mode Selection

Choose `taskType` from actual inputs before selecting a model:

| Inputs | `taskType` | Key fields |
|---|---|---|
| Text only | `text_to_video` | `prompt` |
| One image or start/end frames | `image_to_video` | `firstFrameFileId`, optional `endFrameFileId` |
| Multiple image references | `image_to_video` when config supports multi-image | `referenceImageFileIds` |
| Named image/video references | `omni_reference` | `prompt`, `inputImages`, `inputVideos` |
| Motion-control prompt/assets | `motion_control` | live-schema fields |
| Source avatar video | `video_avatar` | `videoFileId` |

Do not infer an input mode from a model's display name. Select a model whose
live capabilities match the supplied media.

## MCP Sequence

Read compatible models first:

```json
{
  "req": {
    "type": "video",
    "taskType": "image_to_video"
  }
}
```

Use `models[].submitModel` exactly and satisfy the selected model's
`requiredSubmitFields`.

Image-to-video:

```json
{
  "req": {
    "taskType": "image_to_video",
    "model": "<submitModel>",
    "prompt": "A product slowly rotating on a clean white background",
    "firstFrameFileId": "file_start",
    "endFrameFileId": "file_end",
    "resolution": 1080,
    "duration": 5,
    "boardId": "board_123"
  }
}
```

Text-to-video:

```json
{
  "req": {
    "taskType": "text_to_video",
    "model": "<submitModel>",
    "prompt": "A futuristic city at night with neon reflections on wet streets",
    "aspectRatio": "16:9",
    "resolution": 1080,
    "duration": 5,
    "generatingCount": 1,
    "boardId": "board_123"
  }
}
```

Omni reference:

```json
{
  "req": {
    "taskType": "omni_reference",
    "model": "<submitModel>",
    "prompt": "Apply the color style from <<<Image1>>> to the motion in <<<Video1>>>",
    "inputImages": [
      {"fileId": "file_style", "name": "Image1"}
    ],
    "inputVideos": [
      {"fileId": "file_motion", "name": "Video1"}
    ],
    "aspectRatio": "9:16",
    "resolution": 720,
    "boardId": "board_123"
  }
}
```

Poll with the same task type:

```json
{
  "req": {
    "taskType": "image_to_video",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Upload all local inputs first. Follow
[the common workflow](../SKILL.md#common-agent-workflow) for boards, uploads,
polling, and timeout recovery.

## Parameter Semantics

- `model`: live `submitModel`, not necessarily `displayName`.
- `aspectRatio`: pass only when the selected model supports it; image-to-video
  often derives ratio from the input.
- `resolution` and `duration`: exact values from live options.
- `generatingCount`: 1–4, default 1.
- `firstFrameFileId` / `endFrameFileId`: start/end frame mode.
- `referenceImageFileIds`: multi-image mode, often requiring at least two.
- `inputImages` / `inputVideos`: named omni references used as
  `<<<Image1>>>` and `<<<Video1>>>` in the prompt.
- Native audio and internet-search controls are model-specific. Include them
  only if the current tool schema and selected model config expose them.

## Model Recommendation

Live config is authoritative. Respect a compatible user-selected model; when
none is specified, use `modelSelectionPolicy.preferredSubmitModel`, or prefer
Standard/Seedance 2.0 when present.

| Priority | Guidance |
|---|---|
| Best quality | Standard, Kling O3, Veo 3.1 |
| Fast turnaround | Fast, Seedance 1.0 Pro Fast, Veo 3.1 Fast |
| Long clips (still ≤ model max, typically ≤15s) | Standard/Fast, Kling V3/O3, Vidu Q3 Pro |
| Longer than ~15s / multi-scene finished video | `topview_prepare_canvas_jump` → Topview Canvas |
| 4K | Veo 3.1 family when live config offers 2160p |
| Budget | Compare current config billing before confirmation |
| Native audio | Standard/Fast, Kling O3/V3, Veo 3.1, Vidu Q3 Pro when enabled |

Historically:

- Standard and Fast provide Seedance 2.0-level quality, native audio, and up to
  15s across text, image, and omni modes.
- Seedance 2.0 Mini supports 480/720p, 4–15s, and native audio.
- Gemini Omni Flash replaced `Topview Omni`; the deprecated name must not be
  sent.
- Happy Horse 1.1 supports image/text generation at 720/1080p and 3–15s.

Channel defaults: `9:16` for TikTok/Reels, `16:9` for YouTube, and `3:4` or
`1:1` for Instagram.

## Prompt Tips

Use Subject + Action + Environment + Style + Camera. Helpful camera language
includes “static shot,” “slow pan,” “dolly forward,” “tracking shot,” “orbit,”
“zoom in,” “crane shot,” and “shallow depth of field.”
