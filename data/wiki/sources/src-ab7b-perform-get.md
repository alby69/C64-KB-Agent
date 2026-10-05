---
id: src-ab7b-perform-get
type: source
title: 'Source Summary: perform GET'
aliases:
- perform GET
- ab7b-perform-get.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ab7b-perform-get.md
  sha256: 0537571df5ed7bc9976a76cca08f1b29a6349cb8052079f8fe06affa68bca73b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform GET

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ab7b-perform-get.md`
**SHA256**: `0537571df5ed7bc9976a76cca08f1b29a6349cb8052079f8fe06affa68bca73b`

## Summary



# $AB7B — perform GET

## Disassemblatura
```assembly
.AB7B  20 A6 B3 JSR $B3A6   ; check not Direct, back here if ok
.AB7E  C9 23    CMP #$23   ; compare with "#"
.AB80  D0 10    BNE $AB92   ; branch if not GET#
.AB82  20 73 00 JSR $0073   ; increment and scan memory
.AB85  20 9E B7 JSR $B79E   ; get byte parameter
.AB88  A9 2C    LDA #$2C   ; set ","
.AB8A  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.AB8D  86 13    STX $13   ; set current I/O channel
.AB8F ...
