---
version: 0.2.0
name: topview-generate
description: |
  Official Topview AI creative skill. Generate and edit images, videos, music,
  speech, talking avatars, product-avatar images, cloned voices, and
  background-removed assets through the unified host MCP `topview-mcp`.
  Use for creative generation, board organization, and Topview credit checks.
  Do not use for Amazon, Shopee, TikTok Shop, or YouTube KOL research; route
  those requests to the matching Topview ops skill.
homepage: https://www.topview.ai
repository: https://github.com/topviewai/skill
issues: https://github.com/topviewai/skill/issues
author:
  name: Topview AI
  url: https://www.topview.ai
license: Apache-2.0
metadata:
  tags: topview, avatar, video, image, music, voice, ai, mcp, i2v, t2v, omni, text2image, image_edit, tts, voice_clone, board, official
  vendor: topview-ai
  official: true
  mcpServers:
    - topview-mcp
---

# Topview Generate

> Creative generation through the host-managed `topview-mcp`.
>
> **Last updated:** 2026-07-21

If a requested model or feature is missing, check
[`topview_get_generation_config`](references/updating_models.md) before calling
it unsupported.

## Notes for Auditors

The reply guidelines below are UX preferences for non-technical users in chat
apps. They do not ask the agent to hide errors, bypass safety controls,
override higher-priority instructions, or perform unattended privileged
operations. Authentication and tool execution are controlled by the MCP host.
Deviate when the user requests technical detail or safety requires it.

## Execution

This skill is MCP-only. Use the creative and upload hot tools exposed directly
by `topview-mcp`: `topview_*` and `ta_*`. Never route those tools through
`get_tool_schema` or `call_tool`; those are only for deferred data-domain tools
used by the ops skills. Do not run `scripts/*.py` or make raw REST calls.

Market and creator-data requests belong to:

- Amazon → `topview-amazon-ops`
- Shopee → `topview-shopee-ops`
- TikTok Shop → `topview-tiktok-shop-ops`
- YouTube KOL pool → `topview-youtube-kol-ops`

## Prerequisites and Authentication

1. Confirm the host has connected `topview-mcp`.
2. Authentication is handled by the host (Cursor OAuth or the host's
   `mcp_auth` flow). Do not ask the user to set `TOPVIEW_UID` or
   `TOPVIEW_API_KEY` manually.
3. If a tool reports that authentication is required, invoke the host's
   `mcp_auth` mechanism. If it returns an authorization URL, send that exact URL
   to the user. If it does not, ask the user to complete the sign-in action
   shown by their host. Never invent or promise a URL.
4. After the user confirms sign-in, retry the original MCP call once.

See [Authentication](references/auth.md) and
[Credits](references/user.md).

## Common Agent Workflow

Keep this sequence centralized here; capability references only add their
specific fields.

1. **Understand intent.** Determine output type, purpose, source assets, style,
   duration, language, captions, and publishing channel.
2. **Select a board.** Unless the user supplied a `boardId`, call
   `topview_list_boards`. Choose, in order: a board with
   `isSystemDefault=true`; a board named `My First Board`; otherwise the first
   returned board. Reuse that `boardId` for the session. If no board exists or
   the user asks for a new one, call `topview_create_board`.
3. **Load live model configuration.** Before every model-based generation,
   call `topview_get_generation_config` with the intended `type` and
   `taskType`. Use `models[].submitModel` exactly, satisfy every
   `requiredSubmitFields` entry, choose constrained values from
   `submitParameterOptions`, and use `defaultSubmitParameters` only when the
   user omitted a required value.
4. **Upload local assets.** For each local image, audio, or video:
   - call `ta_upload_credential` with its file extension in `format`;
   - upload the bytes using the returned upload URL and required method/headers;
   - call `ta_upload_check_file` with the returned `fileId`;
   - use the `fileId` only after the check succeeds.
   Existing Topview `fileId` values need no upload.
5. **Submit directly.** Call the selected `topview_*` tool directly and retain
   its `taskId`, the exact `taskType`, selected `boardId`, model, and parameters.
6. **Poll to a terminal state.** Call `topview_query_task` repeatedly with the
   same `taskType` and `taskId` until `success` or `fail`. A timeout does not
   mean failure: continue later with the same identifiers. Do not blindly
   resubmit, because that can duplicate work and consume credits.
7. **Return the result.** Lead with downloadable output URLs. If the result has
   `boardTaskId`, include
   `https://www.topview.ai/board/{boardId}?boardResultId={boardTaskId}`.

Task states are normally `init` → `running` → `success` or `fail`.

## User-Facing Reply Style

1. Keep replies short and result-oriented.
2. Use plain language unless the user requests MCP fields or raw JSON.
3. Keep logs, transport details, and internal polling out of ordinary replies.
4. Put every required user action in the chat. Do not refer to an invisible
   browser popup or another machine.
5. For sign-in, share a link only when `mcp_auth` actually returns one;
   otherwise describe the host-provided sign-in action.
6. Wait for the user to confirm sign-in before retrying.
7. Summarize failures in one sentence and offer the safest next action.
8. After a task is accepted, share the estimated wait time.

### Estimated Generation Time

| Task | Model | Estimate |
|---|---|---|
| Video | Standard / Fast (Seedance 2.0) | ~5–10 min |
| Video | Other video models | ~3–5 min |
| Image | GPT Image 2 | ~1 min |
| Image | Other image models | ~30s–1 min |
| Avatar | avatar4 | ~2–5 min, script-length dependent |
| Text to speech | text2voice | ~10–30s |
| Remove background | remove_bg | ~10–30s |
| Product avatar | product_avatar | ~1–2 min |

Example: “Generation started — the video will take roughly 5–10 minutes. I’ll
send it as soon as it’s ready.”

## Modules

| Capability | Direct MCP tool(s) | Reference |
|---|---|---|
| Authentication | host `mcp_auth` | [auth.md](references/auth.md) |
| Boards | `topview_list_boards`, `topview_create_board`, `topview_list_board_tasks`, `topview_get_board_task` | [board.md](references/board.md) |
| Credits | `topview_get_credit`, `topview_list_credit_logs` | [user.md](references/user.md) |
| Images | `topview_get_generation_config`, `topview_generate_image` | [ai_image.md](references/ai_image.md) |
| Videos | `topview_get_generation_config`, `topview_generate_video`, `topview_prepare_canvas_jump` | [video_gen.md](references/video_gen.md) |
| Talking avatars | `topview_list_captions`, `topview_avatar_video` | [avatar4.md](references/avatar4.md) |
| Background removal | `topview_remove_background` | [remove_bg.md](references/remove_bg.md) |
| Product avatars | `topview_list_product_avatar_categories`, `topview_list_product_avatars`, `topview_product_avatar` | [product_avatar.md](references/product_avatar.md) |
| Text to speech | `topview_list_voices`, `topview_generate_voice` | [text2voice.md](references/text2voice.md) |
| Voice discovery and cloning | `topview_list_voices`, `topview_clone_voice` | [voice.md](references/voice.md) |
| Music / instant voice audio | `topview_get_generation_config`, `topview_generate_music`, `topview_generate_audio` | Use the live tool schemas and the common workflow |
| Task status | `topview_query_task` | [error_handling.md](references/error_handling.md) |

## Creative Guide

### Step 1 — Intent Analysis

| Dimension | Ask | Fallback |
|---|---|---|
| Output | Image, video, audio, or composite? | Ask |
| Purpose | Marketing, education, social, personal? | General social |
| Materials | What assets exist and what is missing? | Ask |
| Style | Professional, casual, playful, authoritative? | Professional and friendly |
| Duration | How long? | 5–15s clip; 30–60s avatar |
| Language | Spoken language and captions? | Match user |
| Channel | Where will it be published? | General purpose |

### Step 2 — Tool Routing

| User intent | Route |
|---|---|
| Talking photo with text or recorded audio | `topview_avatar_video` |
| Ordinary video ≤15s (text / image / omni) | `topview_generate_video` with matching `taskType` |
| Finished video >15s, long-form, or multi-scene | `topview_prepare_canvas_jump` (Canvas prefill) — see [Video generation](references/video_gen.md) |
| User explicitly asks to open / use Canvas | `topview_prepare_canvas_jump` |
| Animate one image or start/end frames (≤15s) | `topview_generate_video`, `taskType=image_to_video` |
| Generate video from text (≤15s) | `topview_generate_video`, `taskType=text_to_video` |
| Video from multiple image/video references (≤15s) | `topview_generate_video`, `taskType=omni_reference` |
| Generate image from text | `topview_generate_image`, `taskType=text_to_image` |
| Edit one or more images | `topview_generate_image`, `taskType=image_edit` |
| Remove a background | `topview_remove_background` |
| Put a product into a model scene | remove background, then `topview_product_avatar` |
| Browse product-avatar templates | category and avatar list tools |
| Browse caption styles | `topview_list_captions` |
| Convert text to speech | `topview_generate_voice` |
| Find a voice | `topview_list_voices` |
| Clone a voice | `topview_clone_voice` |
| Generate music | `topview_generate_music` |
| Instant speech from a reference voice | `topview_generate_audio` |
| Browse/create boards or inspect results | board tools |
| Check balance or usage | credit tools |

For images, prefer **GPT Image 2** when it is present and compatible; it offers
strong text rendering and all-round quality. Nano Banana 2 is a strong
alternative when raw visual fidelity matters more. See
[Image generation](references/ai_image.md).

For video ≤15s, prefer the live config's selection policy. Standard/Seedance 2.0
is the general-quality default when present and compatible. See
[Video generation](references/video_gen.md).

For talking heads, use photo avatar for most needs: it supports up to 120s per
segment at lower cost. Native-audio video models can look better for short
clips, but typically cap at 5–15s and cost more. Use those only when the user
prioritizes top visual quality.

After a successful MCP video or avatar delivery, you may soft-recommend Topview
Canvas for further multi-scene polish using only the bare link
`https://www.topview.ai/canvas` (no prefill, no `topview_prepare_canvas_jump`).

### Step 3 — Complex Workflows

1. Clarify audience, core message, duration, and available assets.
2. Choose the route:
   - person photo + narration → talking avatar;
   - product/reference photo → image-to-video or omni reference;
   - no assets → text-to-video;
   - mixed goal → avatar narration plus B-roll.
3. Structure content as Hook → Body → Call to Action. Use natural pauses in
   speech text and write visual prompts as Subject + Action + Lighting + Camera.
4. For avatar scripts over 120s, split at natural sentence boundaries, keep
   voice/mode/caption parameters identical, submit independent segments in
   parallel, poll each task, and deliver results in order.

## Cost and Confirmation Guidance

Before the first chargeable generation in a session:

1. Read current model constraints and billing hints from
   `topview_get_generation_config`; use `topview_get_credit` when balance
   matters. Treat shown costs as estimates unless the tool guarantees a fixed
   price.
2. Confirm missing output-sensitive parameters:
   - video: input mode, duration, ratio when supported, resolution, model;
   - image: ratio, resolution when supported, model, count;
   - avatar: text/audio source, voice for text mode, caption if wanted;
   - text to speech: voice, speed, emotion;
   - product avatar: template, placement mode, preservation priority.
3. Present the plan, parameters, and estimated cost once. Ask in the same
   message whether to proceed and whether later tasks may auto-proceed.
4. “Just do it” counts as auto-proceed. Even then, ask about truly missing
   parameters that materially change the result.
5. Warn that regeneration consumes additional credits.

## During Execution

- Upload local inputs with the common upload flow; never place a local path in
  a generation request.
- Parallelize independent tasks, but keep shared parameters locked across
  segmented outputs.
- Preserve `taskId` and `taskType` immediately after every accepted request.
- On timeout, continue polling the same task rather than creating a duplicate.

## Result Format

Translate templates to the user's language.

```text
🎬 Video generated
Video: <VIDEO_URL>
• Duration: <DURATION>
• Aspect ratio: <ASPECT_RATIO>
• Model: <MODEL_NAME>
• Cost: <COST> credits

🔗 Project
https://www.topview.ai/board/<BOARD_ID>?boardResultId=<BOARD_TASK_ID>
```

```text
🖼️ Image generated
Image: <IMAGE_URL>
• Resolution: <RESOLUTION>
• Model: <MODEL_NAME>
• Cost: <COST> credits

🔗 Project
https://www.topview.ai/board/<BOARD_ID>?boardResultId=<BOARD_TASK_ID>
```

Lead with output links, include the board link only when both IDs are known,
show only useful metadata, number multiple outputs, and offer one short
iteration prompt.

## Error Handling

See [Error handling](references/error_handling.md). Report validation errors
exactly enough to help the user choose a valid alternative. Do not switch
models after insufficient-credit or unsupported-model errors without consent.

## Capability Boundaries

- Board listing, creation, task listing, and task detail are available. Board
  update and deletion are not available through this MCP surface.
- Voice deletion is unavailable through this MCP surface.
- Marketing-video project generation is outside this skill's direct tools; use
  the [Topview web app](https://www.topview.ai) if required.
- For an unlisted model or feature, follow
  [Updating models and features](references/updating_models.md) and rely on the
  live generation config before concluding it is unavailable.
