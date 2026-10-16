---
name: adtc-event-host
description: Plan and run an Automation & Deep Tech Club (ADTC) event at HBS end to end. Interviews the host for only what is missing, builds a dated T-minus plan from the club playbook, and drafts every asset (speaker outreach, Luma copy, room booking steps, food plan, WhatsApp blasts, fireside questions or workshop run sheet, thank-yous). Use whenever someone wants to host, plan, organize or prep an ADTC event, fireside chat, panel, workshop, office hours, dinner or site visit, or says things like "I want to host an event on X", "help me book a speaker", "what do I need to do for my event", "we have a speaker coming in November", even if they never say "ADTC" or "playbook".
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
