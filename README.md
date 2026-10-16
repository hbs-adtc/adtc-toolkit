# ADTC Toolkit

What a leader of the Automation & Deep Tech Club at HBS needs to run an event with Claude.

| File | What it is |
|---|---|
| `adtc-event-host.skill` | The Claude skill. Download it once and add it in Claude's skills settings. |
| `adtc-design-system.html` | The design system: Luma header templates, flyer, logo, pillar icons, colors, rules. Open it in a browser. |
| `skill/adtc-event-host/` | The skill's source, for anyone changing it. |

Private details (roster, emails, budget rules, links) live in the **Club info** tab of the Events Tracker, which leaders can access. Nothing private is in this repo.

## Set up (once)

1. Download `adtc-event-host.skill` and add it in Claude's skills settings.
2. Connect Google Drive, Gmail and Calendar in Claude.
3. Ask Tyler for Editor access to the Events Tracker for the Google account your Claude uses.
4. Try it: "I want to host a robotics fireside in November."

## Changing things

- **Roster, budget, room defaults, links:** edit the Club info tab. No skill update needed.
- **A Luma template or the brand:** edit `adtc-design-system.html` (bump the version and add a changelog line), then open a pull request.
- **The skill:** edit `skill/adtc-event-host/`, rebuild `adtc-event-host.skill`, open a pull request, and tell leaders to re-add it.
