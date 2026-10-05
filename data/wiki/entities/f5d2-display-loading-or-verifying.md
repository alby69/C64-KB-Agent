---
id: f5d2-display-loading-or-verifying
type: entity
title: display "LOADING" or "VERIFYING"
aliases:
- display "LOADING" or "VERIFYING"
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5d2-display-loading-or-verifying.md
  sha256: a3c28e1837cea0e16dd0070c3834a614684a1fe78fd64d0ef4c78b584362e7ed
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f5d2-display-loading-or-verifying
---

# display "LOADING" or "VERIFYING"



# $F5D2 — display "LOADING" or "VERIFYING"

## Disassemblatura
```assembly
.F5D2  A0 49    LDY #$49   ; point to "LOADING"
.F5D4  A5 93    LDA $93   ; get load/verify flag
.F5D6  F0 02    BEQ $F5DA   ; branch if load
.F5D8  A0 59    LDY #$59   ; point to "VERIFYING"
.F5DA  4C 2B F1 JMP $F12B   ; display kernel I/O message if in direct mode and return
```


## Commenti

### Original Disassembly (—)
- **$F5D2**: point to "LOADING"
- **$F5D4**: get load/verify flag
- **$F5D6**: branch if load
- **$F5D8**: point to "VERIFYING"
- **$F5DA**: display kernel I/O message if in direct mode and return

### Commodore-64-intern-Buch (Commodore)
- **$F5D2**: Offset für 'LOADING'
- **$F5D4**: Load/Verify-Flag laden
- **$F5D6**: Load wenn 0, dann ausgeben
- **$F5D8**: sonst Offset für 'VERIFYING'
- **$F5DA**: Meldung ausgeben, Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F5D2**: offset to verify message
- **$F5D4**: VERCK, load/verify flag
- **$F5D6**: verify
- **$F5D8**: offset to load message
- **$F5DA**: output message flagged by (Y)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f5d2-display-loading-or-verifying]]
