---
id: src-f07d-handshake
type: source
title: 'Source Summary: Handshake'
aliases:
- Handshake
- f07d-handshake.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f07d-handshake.md
  sha256: b061461730d5c46d775984cd3fa8ccfaefaef966cb658aeae00e72d896ee6522
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Handshake

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f07d-handshake.md`
**SHA256**: `b061461730d5c46d775984cd3fa8ccfaefaef966cb658aeae00e72d896ee6522`

## Summary



# $F07D — Handshake

## Disassemblatura
```assembly
.F07D  AD A1 02 LDA $02A1   ; RS-232 NMI Status laden
.F080  29 12    AND #$12   ; wenn RS-232 nicht aktiv
.F082  F0 F3    BEQ $F077   ; dann starten
.F084  18       CLC   ; Carry löschen (ok Kenneichen)
.F085  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F07D**: RS-232 NMI Status laden
- **$F080**: wenn RS-232 nicht aktiv
- **$F082**: dann starten
- **$F084**: Carry löschen (ok Kenneichen)
- **...
