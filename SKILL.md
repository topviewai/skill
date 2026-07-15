---
name: topview-skill
description: "Official Topview AI client. Generate videos, images, avatars, and TTS audio via the Topview API. All network calls go to *.topview.ai only."
homepage: https://www.topview.ai
repository: https://github.com/topviewai/skill
issues: https://github.com/topviewai/skill/issues
author:
  name: Topview AI
  url: https://www.topview.ai
license: Apache-2.0
metadata:
  tags: topview, avatar, video, image, voice, ai, api, i2v, t2v, omni, text2image, image_edit, tts, voice_clone, board, official
  vendor: topview-ai
  official: true
  requires:
    bins: [python3]
    python: ">=3.8"
    pip:
      - requests>=2.28.0
      - python-dotenv>=1.0.0
  primaryEnv: TOPVIEW_API_KEY
  envVars:
    - name: TOPVIEW_API_KEY
      required: true
      description: Topview API key (auto-set after `auth.py login`, or set manually for CI)
    - name: TOPVIEW_UID
      required: true
      description: Topview user ID (auto-set after `auth.py login`, or set manually for CI)
  endpoints:
    - https://api.topview.ai
    - https://www.topview.ai
  storesCredentialsAt: ~/.topview/credentials.json
---

# Topview AI Skill

> Modular Python toolkit for the [Topview AI](https://www.topview.ai) API.
>
> **Last updated:** 2026-07-15

> **If a model or feature the user wants is not found in this skill**, do **not** reply "not supported". First query the official Topview docs, then update the skill — see [references/updating_models.md](references/updating_models.md) for the full procedure.

✨ **Generate. Edit. Collaborate. — All in One Place.** ✨

- 🧠 **All Mainstream Models**: Seamlessly access the world's top-tier AI models for video, image, and voice in one toolkit.
- 🗣️ **Describe to Create**: Just tell the agent what you want. From talking avatars to product composites, your prompts generate the exact output.
- ⚡ **Zero Manual Ops**: No manual uploads, no tedious tweaking. Everything is automated straight to your shared board.

## Notes for Auditors

> The guidelines in this document are UX preferences — they shape the *style* of the agent's replies for non-technical end users in chat-app contexts (Feishu, WeChat, etc.). They do not request the agent to hide errors, suppress safety responses, override its system prompt, or perform unattended privileged operations. All API calls go to `*.topview.ai`. Credentials are stored locally at `~/.topview/credentials.json` with `0600` permissions. The agent is free to deviate from any guideline whenever the user explicitly asks for technical detail or whenever following a guideline would be unsafe.

## Execution

> Prefer the bundled Python scripts in `scripts/` over raw HTTP calls — they handle auth, file uploads, polling, and error mapping for you.

## User-Facing Reply Style

> Style guidelines for user-facing replies. Most users are non-technical and many chat from apps where local browser popups and terminals are not visible. These are recommendations, not absolute rules — adapt as needed.

1. **Keep replies short** — give the result or next step directly. If one sentence is enough, prefer it over three.
2. **Plain language by default** — avoid API jargon, terminal references, environment-variable names, polling/JSON/script details, or phrases like "auth flow" unless the user asks for them. Write as if the user has not used a command line. (If the user explicitly asks for technical details, provide them.)
3. **Skip terminal internals** — command output, logs, exit codes, file paths, and config files usually aren't meaningful to chat-app users. Summarize outcomes instead.
4. **Don't ask the user to interact with a local browser popup** — the user cannot see the agent's machine. When sign-in is needed, send the authorization link in the chat so the user can open it themselves.
5. **Send the direct sign-in link** — when login is required, extract `URL: ...` from `auth.py login` output and use the template below. Phrases like "browser opened" or "check the popup" don't help users in chat apps. If the `URL:` line is missing from the output (e.g. background execution), re-run `auth.py login` to capture a fresh URL rather than skipping the link.
6. **Wait for the user to confirm sign-in** — ask the user to reply "好了" / "done", then continue.
7. **Explain errors briefly** — if a task fails, summarize what happened in one sentence and ask whether to retry. Avoid pasting raw stack traces unless the user requests them.
8. **Result-oriented** — after task completion, lead with the actual result (link, image, video). Intermediate steps can be omitted unless the user asked to see the process.
9. **Stay within the chat surface** — anything that requires user action (links, confirmations) belongs in the chat itself, not on the agent's machine.
10. **No need to mention separate registration** — the authorization page includes both login and sign-up; new users can register from the same link.
11. **Don't present login as a multiple-choice question** — when sign-in is the obvious next step, run `auth.py login` and send the link rather than asking "which method do you prefer?".
12. **Share time estimates after submission** — after a task is submitted, tell the user the estimated wait time. Use the values from the "Estimated Generation Time" table below.

**Estimated Generation Time**

> Tell the user the estimated wait time after submitting a task. Match the user's language.

| Task Type | Model | Estimated Time |
|-----------|-------|---------------|
| Video | Standard / Fast (Seedance 2.0) | ~5–10 min |
| Video | All other video models (Kling, Veo, Vidu, etc.) | ~3–5 min |
| Image | GPT Image 2 | ~1 min |
| Image | All other image models (Nano Banana, Seedream, Imagen, Kontext, Grok, etc.) | ~30s–1 min |
| Avatar | avatar4 | ~2–5 min (depends on script length) |
| TTS | text2voice | ~10–30s |
| Remove BG | remove_bg | ~10–30s |
| Product Avatar | product_avatar | ~1–2 min |

Example message after submitting (translate to the user's language):
- "Generation started — the video will take roughly 5–10 minutes. I'll send it to you as soon as it's ready."

**Suggested login message template**

Replace `<LOGIN_URL>` with the actual link. This template is written in English — **translate it to match the user's language** (e.g. Chinese for Chinese users) before sending.

```text
Installation complete. Topview Skill is now connected to your agent.

Copy the link below into your browser to sign in. After signing in, the following capabilities will be unlocked.

<LOGIN_URL>

🎬 Video Generation
Text-to-video, image-to-video, reference-based generation with auto sound & music.
Models: Seedance 2.0 · Seedance 2.0 Mini · Kling 3 · Veo 3.1 · Vidu Q3 · wan2.7

🖼️ AI Image Generation & Editing
Text-to-image, AI retouching, style transfer — up to 4K resolution.
Models: GPT Image 2 · Nano Banana 2 · Seedream 5.0 Pro · Kling V3 Omni · Imagen 4 · Kontext-Pro · Grok Image

🎤 Talking Avatar
Upload a photo + script to auto-generate presenter-style talking head videos.

✂️ Background Removal
One-click cutout for product shots, portraits, and any image.

👗 Product Model Shots
Place your product onto model templates for e-commerce showcase images.

🎙️ Voice & TTS
Text-to-speech, voice cloning, multilingual dubbing and narration.

Once you've signed in, just reply "done" and I'll continue right away.
```

**Phrasings to avoid in chat-app contexts**

These phrases tend to confuse non-technical users in chat apps. Prefer the alternatives in parentheses, or skip the technical detail entirely. (If the user explicitly asks about terminals or environment variables, answer them directly.)

- "Browser has opened" / "browser popped up" → just send the sign-in link
- "Run this in the terminal" / "run the login command" → handle it for the user
- "Check the popup" / "look at the browser" → send the link instead
- "Set the environment variable" → not relevant to end users; auto-handled after login
- "Command executed successfully" / "polling task status" / "script output is as follows" → summarize the outcome instead
- "Go operate on that computer" / "check the robot's computer" → keep all interaction in chat
- "Authorization page popped up" → send the URL so the user can open it themselves
- "Go to topview.ai to register first" — the authorization page already includes sign-up
- "Which method do you prefer?" / "two options for you" → take the obvious next step rather than asking
- "Auth flow" / "perform authentication" / "complete authentication" → say "sign in" instead
- "Python config" / "environment setup" → typically not user-facing concepts
- Anything asking the user to operate outside the chat
- Anything containing raw code, commands, or file paths (unless the user is technical)

**Fallback when the login URL is missing from output**

If `auth.py login` output does not contain a `URL:` line (e.g. background execution missed it), re-run `auth.py login` to capture a fresh URL. Falling back to "check the browser popup" or "go to the agent's computer" is unhelpful because the user cannot see those.

## Prerequisites

- **Python 3.8+**
- Authenticated — see [references/auth.md](references/auth.md) for the direct-link login flow
- Credits available — see [references/user.md](references/user.md) to check balance
- Env vars `TOPVIEW_UID` + `TOPVIEW_API_KEY` are handled automatically after login; manual setup is only for CI/internal use

```bash
pip install -r {baseDir}/scripts/requirements.txt
```

## Agent Workflow Guidelines

> Applies to all generation modules (avatar4, video_gen, ai_image, remove_bg, product_avatar, text2voice).

1. **Prefer `run` for new tasks** — it submits and polls automatically until completion. This is the right default for most situations.
2. **Handle polling on the agent side** — the user shouldn't need to check task status manually; the script will poll until completion or timeout.
3. **Use `query` for resumes** — when `run` times out and you already have a `taskId`, or when the user provides an existing `taskId`.
4. **`query` polls continuously** — it keeps checking every `--interval` seconds until status is `success` or `fail`, or `--timeout` expires. It does not stop after one check.
5. **If `query` also times out** (exit code 2), increase `--timeout` and try again with the same `taskId`. Resubmit with `run` only if the task actually failed.

```
Decision tree:
  → New request?           use `run`
  → run timed out?         use `query --task-id <id>`
  → query timed out?       use `query --task-id <id> --timeout 1200`
  → task status=fail?      resubmit with `run`
```

**Task Status:**

| Status | Description |
|--------|-------------|
| `init` | Task is queued, waiting to be processed |
| `running` | Task is actively being processed |
| `success` | Task completed successfully |
| `fail` | Task failed |

## Board ID Guidelines

> Including a `--board-id` with each generation task keeps results organized and viewable on the web.

1. **Session start** — before submitting the first task, run `board.py list --default -q` to get the default board ID ("My First Board"). Once per session is enough.
2. **Pass to all tasks** — add `--board-id <id>` to each generation command (`avatar4.py`, `video_gen.py`, `ai_image.py`, `product_avatar.py`, `text2voice.py`).
3. **After completion** — if the task result contains a `boardTaskId`, share the edit link with the user: `https://www.topview.ai/board/{boardId}?boardResultId={boardTaskId}`.
4. **User wants a new board** — run `board.py create --name "..."` and use the returned board ID for subsequent tasks.
5. **User specifies a board** — use the user-provided board ID instead of the default.
6. **Forgot the board ID?** — run `board.py list --default -q` again.

```
Session flow:
  1. BOARD_ID = $(board.py list --default -q)
  2. avatar4.py run --board-id $BOARD_ID ...
  3. video_gen.py run --board-id $BOARD_ID ...
  4. (result shows edit link with boardTaskId)
```

## Modules

| Module | Script | Reference | Description |
|--------|--------|-----------|-------------|
| Auth | `scripts/auth.py` | [auth.md](references/auth.md) | OAuth 2.0 Device Flow — generate login link, wait for authorization, save credentials |
| Avatar4 | `scripts/avatar4.py` | [avatar4.md](references/avatar4.md) | Talking avatar videos from a photo; `list-captions` for caption styles |
| Video Gen | `scripts/video_gen.py` | [video_gen.md](references/video_gen.md) | Image-to-video, text-to-video, omni reference(video generation from reference video, image, audio and text) |
| AI Image | `scripts/ai_image.py` | [ai_image.md](references/ai_image.md) | Text-to-image and AI image editing (10+ models) |
| Remove BG | `scripts/remove_bg.py` | [remove_bg.md](references/remove_bg.md) | Remove image background — step 1 of Product Avatar flow |
| Product Avatar | `scripts/product_avatar.py` | [product_avatar.md](references/product_avatar.md) | Model showcase product image; `list-avatars`/`list-categories` for template browsing |
| Text2Voice | `scripts/text2voice.py` | [text2voice.md](references/text2voice.md) | Text-to-speech audio generation |
| Voice | `scripts/voice.py` | [voice.md](references/voice.md) | Voice list/search, voice cloning, delete custom voices |
| Board | `scripts/board.py` | [board.md](references/board.md) | Board management — organize results, view/edit on web |
| User | `scripts/user.py` | [user.md](references/user.md) | Credit balance and usage history |

> **Read individual reference docs for usage, options, and code examples.**
> Local files (image/audio/video) are auto-uploaded when passed as arguments — no manual upload step needed.

---

## Creative Guide

> **Core Principle:** Start from the user's intent, not from the API.
> Analyze what the user wants to achieve, then pick the right tool, model, and parameters.

### Step 1 — Intent Analysis

Every time a user requests content, identify:

| Dimension | Ask Yourself | Fallback |
|-----------|-------------|----------|
| **Output Type** | Image? Video? Audio? Composite? | Must ask |
| **Purpose** | Marketing? Education? Social media? Personal? | General social media |
| **Source Material** | What does the user have? What's missing? | Must ask |
| **Style / Tone** | Professional? Casual? Playful? Authoritative? | Professional & friendly |
| **Duration** | How long should the output be? | 5–15s for clips, 30–60s for avatar |
| **Language** | What language? Need captions? | Match user's language |
| **Channel** | Where will it be published? | General purpose |

### Step 2 — Tool Selection

Route the user's request to the right script. For a combination request (e.g. talking head + product clips), plan a recipe (see Step 3). If something is outside current capabilities, see Capability Boundaries below.

| User says... | Script & Type |
|----------------------------------------------|-------------|
| "Make a talking avatar video with this photo and text" | `avatar4.py` (pass local image path directly) |
| "Generate a video with this photo and my audio recording" | `avatar4.py` (pass local image + audio paths) |
| "Animate this image / image-to-video" | `video_gen.py --type i2v` (pass local image path) |
| "Generate a video about..." | `video_gen.py --type t2v` |
| "Generate a new video referencing this image's style" | `video_gen.py --type omni` |
| "Generate an image / text-to-image" | `ai_image.py --type text2image` |
| "Modify this image / change background" | `ai_image.py --type image_edit` |
| "Remove image background / cutout" | `remove_bg.py` |
| "Put this product on a model image" | `product_avatar.py` (use `remove_bg.py` first if product has background) |
| "What product avatar/model templates are available?" | `product_avatar.py list-avatars` |
| "What caption styles are available?" | `avatar4.py list-captions` |
| "Convert this text to speech / audio" | `text2voice.py` |
| "What voices are available? / Find a female voice" | `voice.py list --gender female` |
| "Clone a voice from this audio recording" | `voice.py clone --audio <file>` |
| "Delete this custom voice" | `voice.py delete --voice-id <id>` |
| "View my board / check what was generated" | `board.py list` or `board.py tasks --board-id <id>` |
| "Create a new board" | `board.py create --name "..."` |
| "Check how many credits I have left" | `user.py credit` |

> **Video model selection** — see [references/video_gen.md](references/video_gen.md) § Model Recommendation.

> **Image model tip:** For all image tasks, default to **GPT Image 2** — strong text rendering and all-round quality, 13 aspect ratios, 1K/2K/4K resolution, and up to 16 reference images for editing. Nano Banana 2 is a strong alternative when raw image fidelity matters more than text rendering. See [references/ai_image.md](references/ai_image.md) § Model Recommendation.

> **Product Avatar workflow:** For best results, use the 2-step flow: `remove_bg.py` to get a `bgRemovedImageFileId`, then `product_avatar.py` with `--product-image-no-bg`. Use `product_avatar.py list-avatars` to browse public templates and get an `avatarId`. See [references/product_avatar.md](references/product_avatar.md) § Full Workflow.

> **Caption styles for avatar4:** Use `avatar4.py list-captions` to discover available caption styles, then pass the `captionId` via `--caption`.

> **Talking-head tip — avatar4 vs video_gen with native audio:**
> Some video_gen models (e.g. Standard, Kling V3, Veo 3.1) support native audio and can produce talking-head videos with **better visual quality** than avatar4. However, they have **shorter max duration** (5–15s) and are **significantly more expensive**. Avatar4 supports up to 120s per segment at much lower cost.
> **Rule of thumb:** Default to avatar4 for most talking-head needs. Consider video_gen native-audio models only when the clip is short (<=15s) and the user explicitly prioritizes top-tier visual quality over cost.

### Step 3 — Simple vs Complex

**Simple requests** — the user's need is clear, materials are ready → handle directly from the reference docs.

**Complex requests** — the user gives a *goal* (e.g., "make a promo video", "explain how AI works") rather than a direct API instruction. Follow this universal workflow:

1. **Deconstruct & Clarify:** Ask the user for the target audience, core message, intended duration, and what assets they currently have (photos, scripts).
2. **Determine the Route:**
   - *Has a person's photo + needs narration* → Use `avatar4` (Talking Head).
   - *Has a product/reference photo* → Use `video_gen --type i2v` or `omni`.
   - *No assets, purely visual concept* → Use `video_gen --type t2v`.
   - *Requires both* → Plan a Hybrid approach (Avatar narration + B-roll inserts).
3. **Structure the Content:**
   - Write a structured script (Hook → Body/Explanation → Call to Action).
   - Add `<break time="0.5s"/>` tags to TTS scripts for natural pacing.
   - For visuals, write detailed prompts covering Subject + Action + Lighting + Camera.
4. **Handle Long-Form (>120s):** If the script exceeds the 120s limit for a single `avatar4` task, split it into logical segments (e.g., 60s each) at natural sentence boundaries. Submit tasks in parallel using the `submit` command, ensure parameters (voice/model) remain locked across segments, and deliver them in order.

---

## Pre-Execution Checklist

> Recommended steps before each generation task.

1. **Estimate cost** — use `video_gen.py estimate-cost` for video tasks, `ai_image.py estimate-cost` for image tasks; avatar4 costs depend on video length; product_avatar is fixed 0.5 credits; text2voice is fixed 0.1 credits.
2. **Validate parameters** — ensure model, aspect ratio, resolution, and duration are compatible (use `list-models` to check).
3. **Confirm missing key parameters with the user** — if important parameters that affect the output are unspecified, ask before proceeding rather than picking defaults silently. Key parameters by module:
   - **video_gen**: duration, aspect ratio, model
   - **ai_image**: aspect ratio, resolution, model, number of images
   - **avatar4**: usually determined by input; confirm voice if not specified
   - **text2voice**: voice selection
4. **Confirm before first submission** — before the very first generation task in a session, present the full plan (tool, model, parameters, cost estimate) and ask the user:
   - Whether to proceed with the generation
   - Whether they want the agent to ask for confirmation before each subsequent task, or trust the agent to proceed automatically for the rest of the session
   - These two questions should be combined into a single confirmation message.
   - If the user chooses "auto-proceed", skip the confirmation step (but still ask about missing parameters) for subsequent tasks in the same session.
   - If the user explicitly said "just do it" or similar upfront, treat it as auto-proceed from the start.

## Agent Behavior Protocol

### During Execution

1. **Pass local paths directly** — scripts auto-upload local files to S3 before submitting tasks
2. **Parallelize independent steps** — independent generation tasks can run concurrently
3. **Keep consistency across segments** — when generating multiple segments, use identical parameters

### After Execution

> Recommended result format below — output link first, then the board link, then key metadata. Keep it clean and scannable.
> Templates are written in English — **translate to match the user's language** before sending.

**Video result template:**

```text
🎬 Video generated

Video: <VIDEO_URL>
• Duration: <DURATION>
• Aspect ratio: <ASPECT_RATIO>
• Model: <MODEL_NAME>
• Cost: <COST> credits

🔗 Project link
https://www.topview.ai/board/<BOARD_ID>?boardResultId=<BOARD_TASK_ID>
View, edit, and download in the project.

Not happy with the result? Let me know and I'll adjust and regenerate.
```

**Image result template:**

```text
🖼️ Image generated

Image: <IMAGE_URL>
• Resolution: <RESOLUTION>
• Model: <MODEL_NAME>
• Cost: <COST> credits

🔗 Project link
https://www.topview.ai/board/<BOARD_ID>?boardResultId=<BOARD_TASK_ID>
View, edit, and download in the project.

Not happy with the result? Let me know and I'll adjust and regenerate.
```

**Format guidelines:**
1. **Result link first** — show the video/image URL at the top.
2. **Board link second** — if `boardTaskId` is available, include the board edit link.
3. **Key metadata only** — duration, aspect ratio/resolution, model, cost. Avoid dumping raw JSON or extra fields.
4. **Offer iteration** — close with a short note that the user can ask for adjustments. Mention that regeneration costs additional credits.
5. **Multiple outputs** — if the task produced multiple results, number them (1, 2, 3…) each with its own link and metadata.
6. **Match user language** — translate the template to the user's language before sending.

### Error Handling

See [references/error_handling.md](references/error_handling.md) for error codes, task-level failures, and recovery decision tree.

---

## Capability Boundaries

Available capabilities are listed in the **Modules** table and the **Step 2 routing table** above. Anything not covered there is out of scope for a module — for example:

| Capability | Status |
|------------|--------|
| Marketing video (m2v) | No module — suggest the [topview.ai](https://www.topview.ai) web UI |

> If the user wants a model or feature that isn't listed above, follow the **"query the official docs first, then update the skill"** procedure in [references/updating_models.md](references/updating_models.md). Avoid promising capabilities that don't exist as modules — only point users to the [topview.ai](https://www.topview.ai) web UI when the capability genuinely does not exist in the Topview API.
