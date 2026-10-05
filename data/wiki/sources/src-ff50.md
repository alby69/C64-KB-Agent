---
id: src-ff50
type: source
title: 'Source Summary: ALL'
aliases:
- ALL
- ff50.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff50.md
  sha256: 2346c9663b39c4f38f5efdf7df28191c2f57f74c692bcb682c2b01016f253fcb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ALL

**Raw Source File**: `data/docs/c64ref/kernal-api/ff50.md`
**SHA256**: `2346c9663b39c4f38f5efdf7df28191c2f57f74c692bcb682c2b01016f253fcb`

## Summary



# $FF50 — ALL ($FF50)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF50`
- **Chiamata**: `JSR None` o `SYS 65360`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine passes a command to a DMA (Direct Memory Ac-
device. The DMA device will then take control of the
 to execute the command. The routine is written to sup-
he REC (RAM Expansion Controller) chip in the 1700
...
