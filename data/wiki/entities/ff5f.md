---
id: ff5f
type: entity
title: R
aliases:
- R
tags:
- jumps
- system-routines
- kernal-api
sources:
- path: data/docs/c64ref/kernal-api/ff5f.md
  sha256: 74992e072fbe9391ddfe4220a7e71f6ba83086b8f38eb0b91ab7030608768014
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ff5f
---

# R



# $FF5F — R ($FF5F)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF5F`
- **Chiamata**: `JSR None` o `SYS 65375`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine switches active screen displays. The active display
 one which has a live cursor, and to which screen
 output is directed. The routine exchanges the active
active screen-editor variable tables, tab-stop bitmaps,
ne-link bitmaps; and it toggles the active screen flag
ion $D7). The routine doesn't physically tum either
chip on or off—both chips always remain enabled.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ff5f]]
