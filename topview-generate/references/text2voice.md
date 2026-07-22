# Text to Speech

Convert text into speech with `topview_generate_voice`.

## Choose a Voice

Call `topview_list_voices` when the user has not supplied a voice:

```json
{
  "req": {
    "language": "zh-CN",
    "gender": "female",
    "style": "Advertisement",
    "pageNo": 1,
    "pageSize": 20
  }
}
```

Show a short, relevant list with voice name, language, gender, accent, style,
and demo URL when available.

## Generate Speech

```json
{
  "req": {
    "voiceText": "你好，欢迎使用文本转音频功能。",
    "voiceId": "voice_888",
    "voiceSpeed": 1.0,
    "emotionName": "happy",
    "pronRules": [
      {"oldStr": "行", "newStr": "xing"}
    ],
    "boardId": "board_123"
  }
}
```

`voiceId` and the text to synthesize are the core inputs. `voiceSpeed` supports
0.8–1.2. Supported emotions include `happy`, `neutral`, `surprised`, `angry`,
`sad`, `fearful`, and `disgusted`.

Pronunciation rules replace exact text spans. Use them sparingly and confirm
ambiguous pronunciations with the user.

## Polling

```json
{
  "req": {
    "taskType": "text_to_speech",
    "taskId": "task_123",
    "needCloudFrontUrl": true
  }
}
```

Follow [the common workflow](../SKILL.md#common-agent-workflow) for board
selection and timeout recovery.

## Segmented Narration

For long narration, split at natural sentence or paragraph boundaries, keep
the same voice, speed, emotion, and pronunciation rules, process independent
segments concurrently when appropriate, and return them in order.

Historical pricing is **0.1 credits per task**, with failed tasks refunded.
Verify current pricing when the service provides it.

On success, lead with the audio URL, then include duration, voice, and cost when
available.
