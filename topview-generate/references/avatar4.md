# Talking Avatar

Create a talking-head video from a portrait with `topview_avatar_video`.

## Caption Discovery

Call `topview_list_captions` before generation when the user wants captions:

```json
{
  "req": {}
}
```

Show useful caption thumbnails and pass the selected `captionId` to the avatar
request.

## Text-Driven Avatar

Upload a local portrait first, or use an existing `fileId`. Find a voice with
`topview_list_voices` when needed.

```json
{
  "req": {
    "templateImageFileId": "file_portrait",
    "mode": "avatar4",
    "scriptMode": "text",
    "ttsText": "Welcome to Topview.",
    "voiceId": "voice_123",
    "voiceModel": "elevenlabs-v2.5",
    "captionId": "caption_123",
    "customMotion": "Natural eye contact and subtle hand gestures",
    "boardId": "board_123"
  }
}
```

An existing reusable avatar may be supplied as `avatarId` instead of
`templateImageFileId`.

## Audio-Driven Avatar

Upload both portrait and audio first:

```json
{
  "req": {
    "templateImageFileId": "file_portrait",
    "mode": "avatar4Fast",
    "scriptMode": "audio",
    "audioFileId": "file_audio",
    "boardId": "board_123"
  }
}
```

## Polling

```json
{
  "req": {
    "taskType": "avatar_video",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Follow [the common workflow](../SKILL.md#common-agent-workflow) for upload,
board selection, and timeout recovery.

## Parameters

| Field | Meaning |
|---|---|
| `avatarId` / `templateImageFileId` | Existing avatar or uploaded portrait; provide one |
| `mode` | `avatar4` for quality or `avatar4Fast` for speed |
| `scriptMode` | `text` or `audio` |
| `ttsText` + `voiceId` | Required together for text mode |
| `audioFileId` | Required for audio mode |
| `voiceModel` | Optional supported TTS model |
| `voiceSettings` | Optional stability, volume, similarity, and style controls |
| `captionId` | Optional caption style |
| `customMotion` | Motion prompt, maximum 600 characters |
| `offPeak` | Optional off-peak execution |

## Duration and Segmentation

Both `avatar4` and `avatar4Fast` support up to 120 seconds per segment.
`avatar4` prioritizes quality; `avatar4Fast` prioritizes speed.

For scripts over 120 seconds:

1. Split at natural sentence boundaries, usually around 60–120 seconds.
2. Keep portrait/avatar, voice, mode, voice settings, caption, and motion
   consistent.
3. Submit independent segments in parallel when appropriate.
4. Poll every segment with its own task ID.
5. Return results in script order and label each segment.
