# The tracker (Smartsheet)

Two sheets in the **ADTC** workspace in Smartsheet, read and written through the Smartsheet connector. Find them by name.

| Sheet | What's in it |
|---|---|
| **ADTC Events** | One row per event: past, live, planned or just an idea. |
| **ADTC Club Info** | Private details: the leadership roster with emails (`Type` = Leader), defaults like room, time slot, food budget and spending approver (`Type` = Default), and links (`Type` = Link). |

If the Smartsheet connector isn't connected, or the sheets aren't shared with this person, say so in one line, tell the host to connect Smartsheet in Claude and ask Tyler for Editor access to the ADTC workspace, then carry on and ask for any value you need instead of guessing.

## ADTC Events columns

| Column | Rule |
|---|---|
| ID | Permanent, next number in sequence (ADTC-036, ...). Never reuse or renumber. |
| Title | Public event name once it exists, otherwise a short working name. |
| Status | Idea, Outreach, Confirmed, Live, Done or Dropped. |
| Date | Only once the speaker has confirmed. Blank otherwise. |
| Start / End | 24-hour local time, e.g. 17:30. |
| Term | Fall 2026, Spring 2027, and so on. |
| Pillar | Robotics, Future of Compute, Biotech, Climate Tech, Manufacturing, Materials Science or Cross-pillar. |
| Format | Fireside, Panel, Workshop, Office hours, Dinner, Site visit, Social, Reverse pitch or Hackathon. |
| Owner | Full name of the leader driving it, matching the roster. |
| Speakers | Semicolon-separated, with (title, company) when known. |
| Organization, Contact, Co-hosts / partners, Location, Luma | As named. Luma is the full URL. |
| Next step | The single next action, with a date. Clear it when Done. |
| Notes | Context. Start with NEEDS REVIEW: when a human must confirm something. |

Don't store RSVP counts, attendance or descriptions; the Luma page has them.

## Status meanings

Idea: no outreach yet. Outreach: talking to the speaker, no confirmed date. Confirmed: speaker and date agreed. Live: room booked and Luma published. Done: happened. Dropped: not happening; keep the row and say why in Notes.

## Rules

1. Read all of ADTC Events before proposing a date or contacting a speaker.
2. Flag any event that isn't Dropped within 3 days of a proposed date.
3. Before contacting a speaker or organization, search Speakers, Organization and Contact. If another owner has an open row, tell the host to coordinate with that owner first.
4. Show the exact row or change before writing it.
5. Edit only rows the host owns unless they say otherwise. Never delete rows; set Status to Dropped.
