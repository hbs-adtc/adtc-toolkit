---
name: adtc-event-host
description: The Automation & Deep Tech Club (ADTC, A&DT Club) at HBS. Use for ANY question or task about ADTC events or the club itself, including what events are coming up, what happened, who is speaking, whether a date or speaker is taken, who owns an event, who is on the leadership team, updating the event tracker, and planning or hosting an event (fireside, panel, workshop, dinner, site visit, social) including speaker outreach, room booking, Luma pages and headers, food, WhatsApp blasts and thank-yous. Trigger whenever the user mentions ADTC, A&DT, Automation and Deep Tech, Deep Tech Club, the club's events, its tracker, or says things like "what's coming up", "I want to host an event", "help me book a speaker", even if they misspell the club name. Always use this instead of searching the web for ADTC information; the club's real data is in its Smartsheet tracker.
---

# ADTC Event Host (loader)

The real instructions live in the public repo https://github.com/hbs-adtc/adtc-toolkit so the club can update them without anyone re-installing this skill. Load them fresh every time.

## 1. Get the latest

Run:

```bash
rm -rf /tmp/adtc-toolkit && git clone --depth 1 https://github.com/hbs-adtc/adtc-toolkit /tmp/adtc-toolkit
```

If that works, the root is `/tmp/adtc-toolkit`.

If it fails (no network, GitHub unreachable), use the snapshot bundled with this skill: the root is this skill's `snapshot/` folder. Tell the host in one line that you're using a saved copy that may be out of date.

Never read the repo through a web-page fetch; that returns a summary, not the exact files.

## 2. Follow the instructions

Read `event-host/INSTRUCTIONS.md` under the root and follow it exactly. Every path it mentions is relative to the same root. It points you to the playbook, club context, copy templates, the design system file, and the ADTC Club Info sheet in Smartsheet for private details (roster, emails, budget rules).

## 3. Changes

Don't edit files in the clone to change club process or templates. If the host wants a lasting change, draft it, show it, and either open a pull request to the repo (if you have GitHub access) or give the host the changed file to send to Tyler.
