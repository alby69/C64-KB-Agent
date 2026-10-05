---
id: src-e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a
type: source
title: 'Source Summary: set the colour code. enter with the colour character in A.
  if A does not contain a'
aliases:
- set the colour code. enter with the colour character in A. if A does not contain
  a
- e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a.md
  sha256: 74e6178b9b86cb941e249cf0aee9006ff870652b2df2b52bd00a92ad8afb508d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set the colour code. enter with the colour character in A. if A does not contain a

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e8cb-set-the-colour-code-enter-with-the-colour-character-in-a-if-a-does-not-contain-a.md`
**SHA256**: `74e6178b9b86cb941e249cf0aee9006ff870652b2df2b52bd00a92ad8afb508d`

## Summary



# $E8CB — set the colour code. enter with the colour character in A. if A does not contain a

## Disassemblatura
```assembly
.E8CB  A2 0F    LDX #$0F   ; set the colour code count
.E8CD  DD DA E8 CMP $E8DA,X   ; compare the character with a table code
.E8D0  F0 04    BEQ $E8D6   ; if a match go save the colour and exit
.E8D2  CA       DEX   ; else decrement the index
.E8D3  10 F8    BPL $E8CD   ; loop if more to do
.E8D5  60       RTS
.E8D6  8E 86 02 STX $0286   ; save the current colour code
...
