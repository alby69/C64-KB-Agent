---
id: src-ecf0-screen-lines-lo-byte-table
type: source
title: 'Source Summary: ; SCREEN LINES LO BYTE TABLE'
aliases:
- ; SCREEN LINES LO BYTE TABLE
- ecf0-screen-lines-lo-byte-table.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ecf0-screen-lines-lo-byte-table.md
  sha256: e90aad875207c4ab4dc0125c962cb12c9b6943d3f0d4c82865d2ba9912b34f39
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ; SCREEN LINES LO BYTE TABLE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ecf0-screen-lines-lo-byte-table.md`
**SHA256**: `e90aad875207c4ab4dc0125c962cb12c9b6943d3f0d4c82865d2ba9912b34f39`

## Summary



# $ECF0 — ; SCREEN LINES LO BYTE TABLE

## Disassemblatura
```assembly
.ECF0  00 28 50 78 A0 C8 F0 18   ; .BYTE <LINZ24 .END .LIB   SERIAL4.0 ;COMMAND SERIAL BUS DEVICE TO TALK ;
.ED09  09 40    ORA #$40   ; TALK   ORA #$40        ;MAKE A TALK ADR
.ED0B  2C       .BYTE $2C   ; .BYT   $2C             ;SKIP TWO BYTES ;COMMAND SERIAL BUS DEVICE TO LISTEN ;
.ED0C  09 20    ORA #$20   ; LISTN  ORA #$20        ;MAKE A LISTEN ADR
.ED0E  20 A4 F0 JSR $F0A4   ; JSR    RSP232          ;PROTECT SELF FROM...
