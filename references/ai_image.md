# AI Image Module

Generate images from text prompts or edit existing images with AI-powered models.

## Supported Task Types

| Type | Description | Required Params |
|------|-------------|-----------------|
| `text2image` | **Text-to-Image** — generate images from a text prompt | `--model`, `--prompt`, `--aspect-ratio` |
| `image_edit` | **Image Edit** — edit images with prompt + reference images | `--model`, `--prompt`, `--aspect-ratio`, `--input-images` |

## Subcommands

| Subcommand | When to use | Polls? |
|------------|-------------|--------|
| `run` | **Default.** New request, start to finish | Yes — waits until done |
| `submit` | Batch: fire multiple tasks without waiting | No — exits immediately |
| `query` | Recovery: resume polling a known `taskId` | Yes — waits until done |
| `list-models` | Check models, constraints, and supported ratios | No |
| `estimate-cost` | Estimate credit cost before running | No |

## Usage

```bash
python {baseDir}/scripts/ai_image.py <subcommand> --type <text2image|image_edit> [options]
```

## Examples

### List Models

```bash
python {baseDir}/scripts/ai_image.py list-models --type text2image
python {baseDir}/scripts/ai_image.py list-models --type image_edit --json
```

### Text-to-Image

Default base model — GPT Image 2:

```bash
python {baseDir}/scripts/ai_image.py run \
  --type text2image \
  --model "GPT Image 2" \
  --prompt "A futuristic city skyline at dusk, neon lights reflected on wet streets" \
  --aspect-ratio "16:9" \
  --resolution "2K" \
  --count 2
```

Fixed-price model (no resolution):

```bash
python {baseDir}/scripts/ai_image.py run \
  --type text2image \
  --model "GPT Image 1.5" \
  --prompt "A watercolor painting of a cat" \
  --aspect-ratio "1:1"
```

Strong alternative — Nano Banana 2 (best raw image fidelity):

```bash
python {baseDir}/scripts/ai_image.py run \
  --type text2image \
  --model "Nano Banana 2" \
  --prompt "A clean launch poster for a new AI image product with crisp readable text" \
  --aspect-ratio "16:9" \
  --resolution "2K"
```

### Image Edit

```bash
python {baseDir}/scripts/ai_image.py run \
  --type image_edit \
  --model "GPT Image 2" \
  --prompt "Change the background to a snowy mountain landscape" \
  --aspect-ratio "16:9" \
  --resolution "2K" \
  --input-images photo.jpg
```

Multi-image reference:

```bash
python {baseDir}/scripts/ai_image.py run \
  --type image_edit \
  --model "GPT Image 2" \
  --prompt "Blend the style of both images" \
  --aspect-ratio "1:1" \
  --resolution "2K" \
  --input-images style.jpg content.jpg \
  --count 2
```

### Cost Estimation

```bash
python {baseDir}/scripts/ai_image.py estimate-cost \
  --type text2image --model "GPT Image 2" --resolution "2K" --count 2
```

### Download Results

```bash
python {baseDir}/scripts/ai_image.py run \
  --type text2image --model "GPT Image 2" \
  --prompt "Northern lights" --aspect-ratio "16:9" --resolution "2K" \
  --output-dir ./results
```

## Options

| Option | Description |
|--------|-------------|
| `--type` | `text2image` or `image_edit` (required) |
| `--model` | Model **display name** (required) |
| `--prompt` | Text prompt (required) |
| `--aspect-ratio` | Aspect ratio (required), e.g. `"16:9"`, `"1:1"`, `"auto"` |
| `--resolution` | `"512p"`, `"1K"`, `"2K"`, `"4K"` — model-dependent |
| `--count` | Number of images (1-4, default: 1) |
| `--board-id` | Board ID |
| `--input-images` | Reference image fileIds or local paths, space-separated (image_edit only). E.g. `--input-images photo.jpg` or `--input-images style.jpg content.jpg` |
| `--timeout` | Max polling time (default: 300) |
| `--interval` | Polling interval (default: 3) |
| `--output-dir` | Download results to directory |
| `--json` | Full JSON response (not used by default; only when the user explicitly requests raw JSON output) |
| `-q, --quiet` | Suppress status messages |

## Model Recommendation

> **GPT Image 2 is the default base model for image generation.**
> Strong text rendering, 13 aspect ratios, 1K/2K/4K resolution, and up to 16 reference images for editing — a solid all-round default for both text2image and image_edit.

| Use Case | Recommended Models | Why |
|----------|--------------------|-----|
| **Best overall (default)** | **GPT Image 2** | Default base model — strong text & all-round quality, 13 ratios, 1K/2K/4K |
| **Strong alternative** | Nano Banana 2 | Best raw image fidelity, 14 ratios, up to 4K, 14 reference images |
| **Budget** | Seedream 4.0 (0.15/img), Grok Image (0.15/img) | Lowest cost |
| **No-resolution simplicity** | GPT Image 1.5, Kontext-Pro | No resolution param needed |
| **Auto aspect ratio** | Seedream 5.0, Seedream 4.5 | `auto` ratio |

**Defaults:**
- text2image → `GPT Image 2`
- image_edit → `GPT Image 2`

## Key Notes

- `aspectRatio` is always required; image_edit models additionally support `"auto"`
- `resolution` is required for some models, forbidden for others — check via `list-models`
- `GPT Image 2` must be called exactly by TopView display name `"GPT Image 2"`; do not pass a provider code name or alias
- `GPT Image 2` supports aspect ratios `9:16`, `3:4`, `1:1`, `4:3`, `16:9`, `2:3`, `3:2`, `5:4`, `4:5`, `21:9`, `9:21`, `1:2`, and `2:1`
- `GPT Image 2` requires `--resolution "1K"`, `"2K"`, or `"4K"`
- `GPT Image 2` image editing accepts up to 16 input images
- **Imagen 4** is only available for text2image, not image_edit
