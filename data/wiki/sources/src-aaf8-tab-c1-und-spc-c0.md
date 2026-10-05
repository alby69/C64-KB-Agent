---
id: src-aaf8-tab-c1-und-spc-c0
type: source
title: 'Source Summary: TAB( (C=1) und SPC( (C=0)'
aliases:
- TAB( (C=1) und SPC( (C=0)
- aaf8-tab-c1-und-spc-c0.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aaf8-tab-c1-und-spc-c0.md
  sha256: 3759b9da7e9605c907c730857216d6c232095cf15701616cdba225794cbd457a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: TAB( (C=1) und SPC( (C=0)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aaf8-tab-c1-und-spc-c0.md`
**SHA256**: `3759b9da7e9605c907c730857216d6c232095cf15701616cdba225794cbd457a`

## Summary



# $AAF8 — TAB( (C=1) und SPC( (C=0)

## Disassemblatura
```assembly
.AAF8  08       PHP   ; Flags merken
.AAF9  38       SEC   ; Carry setzen
.AAFA  20 F0 FF JSR $FFF0   ; Cursorposition holen
.AAFD  84 09    STY $09   ; und Spalte merken
.AAFF  20 9B B7 JSR $B79B   ; Byte-Wert holen
.AB02  C9 29    CMP #$29   ; ')' Klammer zu?
.AB04  D0 59    BNE $AB5F   ; nein: 'SYNTAX ERROR'
.AB06  28       PLP   ; Flags wiederherstellen
.AB07  90 06    BCC $AB0F   ; zu SPC(
.AB09  8A       TXA   ; TAB-Wert...
