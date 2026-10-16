# ADTC Toolkit

What a leader of the Automation & Deep Tech Club at HBS needs to run an event with Claude. This repo is the single source of truth: Claude reads it fresh every time, so a change merged here reaches every leader without anyone re-installing anything.

| Path | What it is |
|---|---|
| `adtc-event-host.zip` | The skill to upload to Claude, once. It's a small loader that pulls the latest from this repo, plus a saved copy for when GitHub is unreachable. |
| `event-host/` | The instructions Claude follows: `INSTRUCTIONS.md`, the playbook, club context, copy templates, design rules. |
| `adtc-design-system.html` | The design system Claude uses: Luma headers, flyer, deck slides, email signature, logo, pillar icons, colors, rules. Open it in a browser. |
| `A_DT_Club_Deck.html` | The original export from Claude Design. View-only. |
| `loader/SKILL.md`, `build-skill.py` | The loader's source and the script that rebuilds the zip. |

Private details (roster, emails, budget rules, links) live in the **Club info** tab of the Events Tracker, which leaders can access. Nothing private is in this repo.

## Set up (once)

1. In Claude, turn on Settings › Capabilities › Code execution and file creation.
2. Download `adtc-event-host.zip`, then Customize › Skills › + › Create skill › Upload a skill.
3. Connect Google Drive, Gmail and Calendar in Claude.
4. Ask Tyler for Editor access to the Events Tracker for the Google account your Claude uses.
5. Try it: "I want to host a robotics fireside in November."

## Changing things

| To change | Edit | Re-upload the skill? |
|---|---|---|
| Roster, budget, room defaults, links | Club info tab in the Events Tracker | No |
| The playbook, copy, or how Claude runs an event | `event-host/` | No |
| A template or the brand | `adtc-design-system.html` (bump the version, add a changelog line) | No |
| The loader itself (rare) | `loader/SKILL.md`, then `python3 build-skill.py` | Yes |

Open a pull request for anything in the repo. Running `build-skill.py` after big changes also refreshes the saved copy inside the zip.
