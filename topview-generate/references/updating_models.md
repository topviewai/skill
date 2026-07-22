# Updating Models and Features

`topview_get_generation_config` is the source of truth for current models,
submit values, required fields, allowed parameters, defaults, and model
selection policy.

## Check a Requested Model

Choose the intended media type and task type:

```json
{
  "req": {
    "type": "image",
    "taskType": "image_edit",
    "refresh": true
  }
}
```

For video:

```json
{
  "req": {
    "type": "video",
    "taskType": "omni_reference",
    "refresh": true
  }
}
```

Use `refresh=true` when a recently released model may not be in the short
configuration cache. Keep `includeRawConfig=false` for normal generation; use
raw config only to diagnose missing normalized fields.

## Selection Rules

1. Match the user's requested model against the returned model entries.
2. Confirm the model supports the intended `taskType` and actual input mode.
3. Send `models[].submitModel` exactly; `displayName` is for user-facing text.
4. Include every field in `requiredSubmitFields`.
5. Choose constrained values from `submitParameterOptions`.
6. Use `defaultSubmitParameters` only for values the user omitted.
7. If no model was requested, follow `modelSelectionPolicy`; otherwise use the
   skill's documented preference only when compatible.

Do not maintain or edit a separate local model registry. Static recommendation
tables are UX guidance and must never override live config.

## When the Model Is Missing

- Retry the config lookup once with `refresh=true`.
- If still absent, say that the model is not currently exposed for that task
  type and offer compatible returned alternatives.
- If the capability itself is not exposed by any direct creative MCP tool,
  suggest the [Topview web app](https://www.topview.ai).
- Update this skill's static recommendation text only when useful; never make
  documentation changes a prerequisite for using a model already present in
  live config.
