---
id: src-ff5f
type: source
title: 'Source Summary: R'
aliases:
- R
- ff5f.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff5f.md
  sha256: 74992e072fbe9391ddfe4220a7e71f6ba83086b8f38eb0b91ab7030608768014
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: R

**Raw Source File**: `data/docs/c64ref/kernal-api/ff5f.md`
**SHA256**: `74992e072fbe9391ddfe4220a7e71f6ba83086b8f38eb0b91ab7030608768014`

## Summary



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
active screen-editor variable tables, tab-stop bitm...
