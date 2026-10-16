"""Rebuild adtc-event-host.zip: the loader SKILL.md plus a snapshot of the repo for offline fallback.
Run from the repo root: python3 build-skill.py"""
import zipfile, os
files = ['adtc-design-system.html'] + ['event-host/' + f for f in sorted(os.listdir('event-host'))]
with zipfile.ZipFile('adtc-event-host.zip', 'w', zipfile.ZIP_DEFLATED) as z:
    z.write('loader/SKILL.md', 'adtc-event-host/SKILL.md')
    for f in files:
        z.write(f, 'adtc-event-host/snapshot/' + f)
print('built adtc-event-host.zip with', len(files) + 1, 'files')
