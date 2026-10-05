---
id: src-f30f-find-a-file
type: source
title: 'Source Summary: find a file'
aliases:
- find a file
- f30f-find-a-file.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f30f-find-a-file.md
  sha256: e11736fd00c672ef2de209deeabda9d0510ca5eeb2867fb61ae3a3b5ce1c6a8f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: find a file

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f30f-find-a-file.md`
**SHA256**: `e11736fd00c672ef2de209deeabda9d0510ca5eeb2867fb61ae3a3b5ce1c6a8f`

## Summary



# $F30F — find a file

## Disassemblatura
```assembly
.F30F  A9 00    LDA #$00   ; clear A
.F311  85 90    STA $90   ; clear the serial status byte
.F313  8A       TXA   ; copy the logical file number to A
```


## Commenti

### Original Disassembly (—)
- **$F30F**: clear A
- **$F311**: clear the serial status byte
- **$F313**: copy the logical file number to A

### Commodore-64-intern-Buch (Commodore)
- **$F30F**: Status
- **$F311**: löschen
- **$F313**: Filenummer in Akku schieben
- **$F314*...
