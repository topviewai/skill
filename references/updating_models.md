# Updating Models & Features

**When to use this doc:** the user requests a model or capability that is **not** listed in the reference docs or in the scripts' model registries (`scripts/ai_image.py`, `scripts/video_gen.py`). Do **not** simply reply "not supported" — follow the procedure below.

## Procedure

### 1. Autonomously fetch the authoritative model list

Topview has **no "list models" API** — the supported-model tables live only in the docs. Fetch the Markdown source directly (append `.md` to the reference URL) and read the "Supported Models and Parameter Constraints" + "Credit Billing" tables.

| Domain | Docs URL (fetch the `.md`) |
|--------|----------------------------|
| Image (text2image / image_edit) | `https://docs.topview.ai/reference/text-to-image-image-edit-task-api-usage.md` |
| Video (image2video / text2video / omni_reference) | `https://docs.topview.ai/reference/image-to-video-v2-text-to-video-omni-reference-api-usage.md` |
| Full API index (to discover other endpoints/docs) | `https://docs.topview.ai/llms.txt` |

- Use the `WebFetch` tool on the `.md` URL; if it's unavailable, `curl -s <url>` also works.
- Match on the model **display name** — the `model` field is case-sensitive to the display name, not the code.

### 2. If the model exists in the docs → update the skill

- Add it to the relevant script's model registry **and** pricing table (`scripts/ai_image.py` or `scripts/video_gen.py`).
- Update its reference doc (`references/ai_image.md` / `references/video_gen.md`).
- Bump the **Last updated** date at the top of `SKILL.md`.

### 3. If the capability genuinely does not exist in the API

Fall back to suggesting the [topview.ai](https://www.topview.ai) web UI. Only do this after step 1 confirms the docs don't list it.
