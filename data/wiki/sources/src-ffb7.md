---
id: src-ffb7
type: source
title: 'Source Summary: /O status word'
aliases:
- /O status word
- ffb7.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ffb7.md
  sha256: 292655db30d956de025df75e0c93c69ac5dc072ca8ff96e49db6d28e1c91dce9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: /O status word

**Raw Source File**: `data/docs/c64ref/kernal-api/ffb7.md`
**SHA256**: `292655db30d956de025df75e0c93c69ac5dc072ca8ff96e49db6d28e1c91dce9`

## Summary



# $FFB7 — /O status word ($FFB7)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FFB7`
- **Chiamata**: `JSR None` o `SYS 65463`


## Note per Fonte

### C64 Programmer's Reference Guide (Commodore)
unication registers: A
aratory routines: None
r returns: None
k requirements: 2
sters affected: A

scription**: This routine returns the current status of the I/O devices
 accumulator. The routine is ...
