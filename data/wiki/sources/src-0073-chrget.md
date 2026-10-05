---
id: src-0073-chrget
type: source
title: 'Source Summary: CHRGET subroutine; get Basic char'
aliases:
- CHRGET subroutine; get Basic char
- 0073-chrget.md
tags:
- memory-map
- zero-page
- rom-layout
- zero-page
sources:
- path: data/docs/c64ref/memory-map/0073-chrget.md
  sha256: 2bc77b834ad21c897ebe20f421e0ddd6356c1cdc0e8b056a0262f961d4dc44c9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: CHRGET subroutine; get Basic char

**Raw Source File**: `data/docs/c64ref/memory-map/0073-chrget.md`
**SHA256**: `2bc77b834ad21c897ebe20f421e0ddd6356c1cdc0e8b056a0262f961d4dc44c9`

## Summary



# CHRGET — CHRGET subroutine; get Basic char ($0073)

## Panoramica
Il registro o area di memoria CHRGET è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0073` (`115` decimale)
- **Range**: `$0073`-`$008A`
- **Dimensione**: `24 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
This code gets changed throughout execution.
It is made to be fast this way.
Also, [X] and [Y] are not disturbed.

"CHRGET" using [TXTPT...
