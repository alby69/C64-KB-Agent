---
id: src-abf9-print-and-get-basic-input
type: source
title: 'Source Summary: print "? " and get BASIC input'
aliases:
- print "? " and get BASIC input
- abf9-print-and-get-basic-input.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/abf9-print-and-get-basic-input.md
  sha256: 3b8bc6558f8eaac1071d47bb7f94a5df15713448610e06510c76e755d8f55cbc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print "? " and get BASIC input

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/abf9-print-and-get-basic-input.md`
**SHA256**: `3b8bc6558f8eaac1071d47bb7f94a5df15713448610e06510c76e755d8f55cbc`

## Summary



# $ABF9 — print "? " and get BASIC input

## Disassemblatura
```assembly
.ABF9  A5 13    LDA $13   ; get current I/O channel
.ABFB  D0 06    BNE $AC03   ; skip "?" prompt if not default channel
.ABFD  20 45 AB JSR $AB45   ; print "?"
.AC00  20 3B AB JSR $AB3B   ; print [SPACE] or [CURSOR RIGHT]
.AC03  4C 60 A5 JMP $A560   ; call for BASIC input and return
```


## Commenti

### Original Disassembly (—)
- **$ABF9**: get current I/O channel
- **$ABFB**: skip "?" prompt if not default channel
- *...
