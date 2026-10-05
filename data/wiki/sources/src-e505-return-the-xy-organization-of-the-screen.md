---
id: src-e505-return-the-xy-organization-of-the-screen
type: source
title: 'Source Summary: return the x,y organization of the screen'
aliases:
- return the x,y organization of the screen
- e505-return-the-xy-organization-of-the-screen.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e505-return-the-xy-organization-of-the-screen.md
  sha256: 7bd0d34a7184b19baf7f3a1ffee3f553474e0c2291d11ef96c9a996737369a3b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: return the x,y organization of the screen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e505-return-the-xy-organization-of-the-screen.md`
**SHA256**: `7bd0d34a7184b19baf7f3a1ffee3f553474e0c2291d11ef96c9a996737369a3b`

## Summary



# $E505 — return the x,y organization of the screen

## Disassemblatura
```assembly
.E505  A2 28    LDX #$28   ; get the x size
.E507  A0 19    LDY #$19   ; get the y size
.E509  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E505**: get the x size
- **$E507**: get the y size

### Commodore-64-intern-Buch (Commodore)
- **$E505**: 40 Spalten
- **$E507**: 25 Zeilen
- **$E509**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$E505**: 40 columns
- **$E507**: 25 rows

### Magnus...
