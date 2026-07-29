---
title: R
source_url: https://github.com/mist64/c64ref/blob/main/src/kernal/machine_language_routines.txt
category: reference
topics:
- kernal-api
- system-routines
- jumps
difficulty: intermediate
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: kernal
  source_files:
  - machine_language_routines.txt
  address: $FF5F
  sources:
  - name: Machine Language Routines
    author: Todd D Heimarck
    description: outine switches active screen displays. The active display
---

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