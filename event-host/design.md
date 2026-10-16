# ADTC Design System

Everything visual lives in one file: `adtc-design-system.html` (repo root) (tokens, Luma header templates, flyer, deck slides, email signature, logo variants, pillar icons, example covers, rules). Read it before making anything visual, and never invent colors, fonts or marks outside it.

## Making a Luma header or flyer

1. Pick the template by who's on stage: one guest in conversation, `tpl-luma-speaker-split`; 2 or 3 people, `tpl-luma-panel`; one headliner featured big, `tpl-luma-spotlight`; a printable or feed flyer, `tpl-flyer`. Look at the matching example cover in the file first.
2. Copy the contents of that `<script type="text/html" id="tpl-...">` block into a new HTML file. It is a complete 1080px page.
3. Fill every `{{...}}` and delete optional blocks you don't need (co-host, subtitle, location, food badge, TBA seat). Break long titles by hand with `<br>`.
4. Photos: ask the host for headshots and, if there's a co-host, their logo in black. Speaker split uses a square B&W crop. Panel and spotlight need background-removed B&W cutouts: if you can run Python, `pip install rembg`, remove the background, convert to grayscale, and embed as a data URI. If you can't, leave the speaker photo out rather than use one with a background.
5. Render a PNG at native size (1080 x 1080, or 1080 x 1350 for the flyer) so the host can upload it to Luma. If you can't render, give them the HTML and tell them to screenshot it at that size.

## Slides and email signature

For a club deck, build from `tpl-slide-title`, `tpl-slide-thesis`, `tpl-slide-agenda`, `tpl-slide-pillars` and `tpl-slide-closing` (1920 x 1080 each). For an officer's email signature, use `tpl-email-signature`; Gmail strips SVG, so render the mark to PNG first.

The repo also holds `A_DT_Club_Deck.html`, the original Claude Design export. It's a compiled bundle for people to view; don't try to read or edit it.

## Changing a template for everyone

Only for a fix every future header should get, not a one-off tweak. Edit the template's script block in the file, bump the version in the header comment and add a line to the Changelog section (version, date, host's name, change). Show the host the before and after and get a yes. Then open a pull request to the repo if you have GitHub access; otherwise give the host the updated file to send to Tyler. Never delete a template; add a new one.
