---
id: src-a57c-crunch-basic-tokens-the-crunch-basic-tokens-vector-is-initialised-to-point-here
type: source
title: 'Source Summary: crunch BASIC tokens, the crunch BASIC tokens vector is initialised
  to point here'
aliases:
- crunch BASIC tokens, the crunch BASIC tokens vector is initialised to point here
- a57c-crunch-basic-tokens-the-crunch-basic-tokens-vector-is-initialised-to-point-here.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a57c-crunch-basic-tokens-the-crunch-basic-tokens-vector-is-initialised-to-point-here.md
  sha256: 0e409a607ec6238b8faff3d217bc5952ef30269c446a64625f1437102a0a2808
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: crunch BASIC tokens, the crunch BASIC tokens vector is initialised to point here

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a57c-crunch-basic-tokens-the-crunch-basic-tokens-vector-is-initialised-to-point-here.md`
**SHA256**: `0e409a607ec6238b8faff3d217bc5952ef30269c446a64625f1437102a0a2808`

## Summary



# $A57C — crunch BASIC tokens, the crunch BASIC tokens vector is initialised to point here

## Disassemblatura
```assembly
.A57C  A6 7A    LDX $7A   ; get BASIC execute pointer low byte
.A57E  A0 04    LDY #$04   ; set save index
.A580  84 0F    STY $0F   ; clear open quote/DATA flag
.A582  BD 00 02 LDA $0200,X   ; get a byte from the input buffer
.A585  10 07    BPL $A58E   ; if b7 clear go do crunching
.A587  C9 FF    CMP #$FF   ; compare with the token for PI, this toke is input directly fr...
