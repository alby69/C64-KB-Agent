---
id: src-b2e9-arrayelement-suchen
type: source
title: 'Source Summary: Arrayelement suchen'
aliases:
- Arrayelement suchen
- b2e9-arrayelement-suchen.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b2e9-arrayelement-suchen.md
  sha256: 285e113dfd697a0ad86a5b542339e92eaa532649d2e7eca36cfa96f5c73f2f3a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Arrayelement suchen

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b2e9-arrayelement-suchen.md`
**SHA256**: `285e113dfd697a0ad86a5b542339e92eaa532649d2e7eca36cfa96f5c73f2f3a`

## Summary



# $B2E9 — Arrayelement suchen

## Disassemblatura
```assembly
.B2E9  C8       INY   ; Zeiger erhöhen
.B2EA  B1 5F    LDA ($5F),Y   ; Zahl der Dimensionen
.B2EC  85 0B    STA $0B   ; speichern
.B2EE  A9 00    LDA #$00   ; Nullwert laden und
.B2F0  85 71    STA $71   ; Zeiger auf Polynom-
.B2F2  85 72    STA $72   ; auswertung löschen
.B2F4  C8       INY   ; Zeiger erhöhen
.B2F5  68       PLA   ; 1. Indexwert vom Stapel
.B2F6  AA       TAX   ; holen und ins X-Reg. bringen
.B2F7  85 64    STA $64...
