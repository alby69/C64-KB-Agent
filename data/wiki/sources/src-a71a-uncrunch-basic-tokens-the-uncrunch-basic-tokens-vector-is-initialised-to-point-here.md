---
id: src-a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here
type: source
title: 'Source Summary: uncrunch BASIC tokens, the uncrunch BASIC tokens vector is
  initialised to point here'
aliases:
- uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point
  here
- a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here.md
  sha256: 6b3935a52742c44c2435aa4e4a3aee02e660f2300a48db100b20bcf2c97f909c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point here

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a71a-uncrunch-basic-tokens-the-uncrunch-basic-tokens-vector-is-initialised-to-point-here.md`
**SHA256**: `6b3935a52742c44c2435aa4e4a3aee02e660f2300a48db100b20bcf2c97f909c`

## Summary



# $A71A — uncrunch BASIC tokens, the uncrunch BASIC tokens vector is initialised to point here

## Disassemblatura
```assembly
.A71A  10 D7    BPL $A6F3   ; just go print it if not token byte else was token byte so uncrunch it
.A71C  C9 FF    CMP #$FF   ; compare with the token for PI. in this case the token is the same as the PI character so it just needs printing
.A71E  F0 D3    BEQ $A6F3   ; just print it if so
.A720  24 0F    BIT $0F   ; test the open quote flag
.A722  30 CF    BMI $A6F3  ...
