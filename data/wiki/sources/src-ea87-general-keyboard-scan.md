---
id: src-ea87-general-keyboard-scan
type: source
title: 'Source Summary: ;  GENERAL KEYBOARD SCAN'
aliases:
- ;  GENERAL KEYBOARD SCAN
- ea87-general-keyboard-scan.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ea87-general-keyboard-scan.md
  sha256: 235326d02b625c6345ad5a6c5a7a852917a47f0f5f1bfbb28665d9d423947902
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;  GENERAL KEYBOARD SCAN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ea87-general-keyboard-scan.md`
**SHA256**: `235326d02b625c6345ad5a6c5a7a852917a47f0f5f1bfbb28665d9d423947902`

## Summary



# $EA87 — ;  GENERAL KEYBOARD SCAN

## Disassemblatura
```assembly
.EA87  A9 00    LDA #$00   ; SCNKEY LDA #$00
.EA89  8D 8D 02 STA $028D   ; STA SHFLAG
.EA8C  A0 40    LDY #$40   ; LDY #64         ;LAST KEY INDEX
.EA8E  84 CB    STY $CB   ; STY SFDX        ;NULL KEY FOUND
.EA90  8D 00 DC STA $DC00   ; STA COLM        ;RAISE ALL LINES
.EA93  AE 01 DC LDX $DC01   ; LDX ROWS        ;CHECK FOR A KEY DOWN
.EA96  E0 FF    CPX #$FF   ; CPX #$FF        ;NO KEYS DOWN?
.EA98  F0 61    BEQ $EAFB   ; BEQ...
