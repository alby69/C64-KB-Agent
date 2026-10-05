---
id: src-af14-check-address-range-return-cb-1-if-address-in-basic-rom
type: source
title: 'Source Summary: check address range, return Cb = 1 if address in BASIC ROM'
aliases:
- check address range, return Cb = 1 if address in BASIC ROM
- af14-check-address-range-return-cb-1-if-address-in-basic-rom.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af14-check-address-range-return-cb-1-if-address-in-basic-rom.md
  sha256: aa689133ccdcb23e96775997a91529b1bd82e9aa9cded8bb6b39882390641282
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: check address range, return Cb = 1 if address in BASIC ROM

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/af14-check-address-range-return-cb-1-if-address-in-basic-rom.md`
**SHA256**: `aa689133ccdcb23e96775997a91529b1bd82e9aa9cded8bb6b39882390641282`

## Summary



# $AF14 — check address range, return Cb = 1 if address in BASIC ROM

## Disassemblatura
```assembly
.AF14  38       SEC   ; set carry for subtract
.AF15  A5 64    LDA $64   ; get variable address low byte
.AF17  E9 00    SBC #$00   ; subtract $A000 low byte
.AF19  A5 65    LDA $65   ; get variable address high byte
.AF1B  E9 A0    SBC #$A0   ; subtract $A000 high byte
.AF1D  90 08    BCC $AF27   ; exit if address < $A000
.AF1F  A9 A2    LDA #$A2   ; get end of BASIC marker low byte
.AF21  E5 ...
