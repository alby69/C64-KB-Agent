---
id: abf9-print-and-get-basic-input
type: entity
title: print "? " and get BASIC input
aliases:
- print "? " and get BASIC input
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
links_out:
- src-abf9-print-and-get-basic-input
---

# print "? " and get BASIC input



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
- **$ABFD**: print "?"
- **$AC00**: print [SPACE] or [CURSOR RIGHT]
- **$AC03**: call for BASIC input and return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-abf9-print-and-get-basic-input]]
