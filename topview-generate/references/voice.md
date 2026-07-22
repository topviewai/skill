# Voices and Voice Cloning

Use `topview_list_voices` to discover voices and `topview_clone_voice` to create
a custom voice from a consented audio sample.

## List Voices

```json
{
  "req": {
    "language": "en",
    "gender": "female",
    "age": "Young",
    "style": "UGC",
    "accent": "American",
    "isCustom": false,
    "pageNo": 1,
    "pageSize": 20
  }
}
```

All filters are optional. `isCustom=true` lists custom cloned voices. Present
`voiceId`, name, language, gender, age, style, accent, and demo audio when
available.

Common language codes include `en`, `zh-CN`, `zh-Hant`, `ja`, `ko`, `fr`,
`de`, `es`, `pt`, `ar`, `hi`, `id`, `th`, `tr`, `uk`, and `vi`.

Common accents include American, British, Australian, Chinese, Indian,
Japanese, Korean, French, German, Spanish, Brazilian, and Vietnamese.

## Clone a Voice

Confirm the user has the right to use the voice. Upload the audio sample, then
call:

```json
{
  "req": {
    "originVoiceFileId": "file_voice_sample",
    "name": "My Brand Voice",
    "voiceText": "Welcome to Topview.",
    "voiceSpeed": 1.0
  }
}
```

`voiceText` should match the sample transcript when provided; accurate
reference text can improve quality.

## Audio Requirements

- MP3 or WAV
- 10 seconds to 5 minutes
- Under 10 MB
- Clear single-speaker speech with minimal noise and music

## Polling

```json
{
  "req": {
    "taskType": "voice_clone",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Poll until success or failure. On success, return the custom `voiceId`, voice
name, and demo audio URL. Follow
[the common workflow](../SKILL.md#common-agent-workflow) for uploads and timeout
recovery.

## Unavailable Operation

Voice deletion is not available through the current MCP surface. State that
limitation directly; do not teach or suggest a non-MCP fallback.
