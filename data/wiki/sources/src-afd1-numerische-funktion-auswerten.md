---
id: src-afd1-numerische-funktion-auswerten
type: source
title: 'Source Summary: numerische Funktion auswerten'
aliases:
- numerische Funktion auswerten
- afd1-numerische-funktion-auswerten.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/afd1-numerische-funktion-auswerten.md
  sha256: f73ac6fe003447270450d4b96889138a1b90f2bd24766e3c4a9ed47655cacec2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: numerische Funktion auswerten

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/afd1-numerische-funktion-auswerten.md`
**SHA256**: `f73ac6fe003447270450d4b96889138a1b90f2bd24766e3c4a9ed47655cacec2`

## Summary



# $AFD1 — numerische Funktion auswerten

## Disassemblatura
```assembly
.AFD1  20 F1 AE JSR $AEF1   ; holt Term in Klammern
.AFD4  68       PLA   ; BASIC-Code für Funktion holen
.AFD5  A8       TAY   ; und als Zeiger ins Y-Reg.
.AFD6  B9 EA 9F LDA $9FEA,Y   ; Vektor für Funktionsbe-
.AFD9  85 55    STA $55   ; rechnung holen und speichern
.AFDB  B9 EB 9F LDA $9FEB,Y   ; 2.Byte holen
.AFDE  85 56    STA $56   ; und speichern
.AFE0  20 54 00 JSR $0054   ; Funktion ausführen
.AFE3  4C 8D AD JMP $...
