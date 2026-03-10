# Auth Module

Authenticate with Topview using the OAuth 2.0 Device Authorization Grant.
Run once — credentials are saved locally and auto-loaded by all other modules.

## Subcommands

| Subcommand | Description |
|------------|-------------|
| `login`  | Full flow: init → open browser → poll → save credentials |
| `poll`   | Resume a previously interrupted login (recovery only) |
| `logout` | Remove saved credentials file |
| `status` | Show current login state (uid, email, name, masked api_key) |

## Usage

```bash
python {baseDir}/scripts/auth.py <subcommand>
```

## `login` — Complete Login Flow

```bash
python {baseDir}/scripts/auth.py login
```

This single command handles the **entire login flow**:
1. Calls the remote OAuth server to start a device session
2. Opens the authorization page in the user's browser
3. Automatically polls until the user authorizes (or the session expires)
4. Saves credentials to `~/.topview/credentials.json` on success

**The agent should tell the user to click Authorize in the browser while `login` is running:**

> "A browser window has opened for Topview authorization.
> Please log in (if needed) and click **Authorize**."

### Full sequence

```
Agent runs:  python auth.py login
                 ↓ browser opens to Topview authorization page
                 ↓ command keeps polling automatically
Agent tells user: "Please click Authorize in the browser"
                 ↓ user clicks Authorize
                 ↓ command detects approval, saves credentials
Credentials saved to ~/.topview/credentials.json ✓
```

## `poll` — Resume Interrupted Login

```bash
python {baseDir}/scripts/auth.py poll
```

Use **only** if `login` was interrupted (e.g., terminal closed during polling).
Reads the pending session from `~/.topview/pending_device.json` and resumes polling.

## `status` — Check Login State

```bash
python {baseDir}/scripts/auth.py status
```

Output when logged in:

```
Logged in
  uid:         NsDAaOPF4jLuAie4ewyg
  name:        John Doe
  email:       user@example.com
  api_key:     sk-...3HB
  charge_type: pro
  authorized:  2026-03-04T10:00:00+00:00
  file:        /Users/you/.topview/credentials.json
```

## `logout` — Remove Credentials

```bash
python {baseDir}/scripts/auth.py logout
```

## Credential File

Saved at: `~/.topview/credentials.json`. File permissions are set to `0600` (owner read/write only).

## Credential Load Priority

All modules use `shared/config.py` which loads credentials in this order:

1. Environment variables `TOPVIEW_UID` + `TOPVIEW_API_KEY` (CI/scripting)
2. `~/.topview/credentials.json` (set by `auth.py login`)
3. Error — prompts to run `auth.py login`

## Agent Rules

- **NEVER** ask the user to run `python auth.py login` or any other command themselves.
- **NEVER** ask the user to set `TOPVIEW_UID` or `TOPVIEW_API_KEY` env vars manually.
- **ALWAYS** run `auth.py login` yourself, then tell the user to authorize in the browser.
