# Topview AI Skill

Agent skill for [Topview AI](https://www.topview.ai) developer products. This skill follows the [Agent Skills specification](https://agentskills.io/specification) and can be used with any compatible AI coding assistant.

Generate, Edit, Collaborate — access all mainstream AI models in one toolkit. Simply describe your vision to create videos, images, and avatars.

## Installation

```bash
npx skills add topviewai/skill
```

## Available Modules

| Module | Script | Description |
|--------|--------|-------------|
| [Avatar4](references/avatar4.md) | `scripts/avatar4.py` | Talking avatar videos from a photo |
| [Video Gen](references/video_gen.md) | `scripts/video_gen.py` | Image-to-video, text-to-video, omni reference video generation |
| [AI Image](references/ai_image.md) | `scripts/ai_image.py` | Text-to-image and AI image editing (10+ models) |
| [Remove BG](references/remove_bg.md) | `scripts/remove_bg.py` | Remove image background |
| [Product Avatar](references/product_avatar.md) | `scripts/product_avatar.py` | Model showcase product image with avatar templates |
| [Text2Voice](references/text2voice.md) | `scripts/text2voice.py` | Text-to-speech audio generation |
| [Voice](references/voice.md) | `scripts/voice.py` | Voice list/search, voice cloning, delete custom voices |
| [Board](references/board.md) | `scripts/board.py` | Board management — organize and view results on web |
| [User](references/user.md) | `scripts/user.py` | Credit balance and usage history |

## Configuration

Requires Python 3.8+ and a Topview AI account. Authenticate via the device flow:

```bash
pip install -r scripts/requirements.txt
python scripts/auth.py login
```

This sets `TOPVIEW_UID` and `TOPVIEW_API_KEY` automatically. You can also set them manually:

```bash
export TOPVIEW_UID="your-uid"
export TOPVIEW_API_KEY="your-api-key"
```

## License

See [LICENSE.txt](LICENSE.txt).
