---
id: e453-initialise-the-basic-vectors
type: entity
title: initialise the BASIC vectors
aliases:
- initialise the BASIC vectors
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e453-initialise-the-basic-vectors.md
  sha256: db50776f77144a1f42ef123adac03a570000c391eaed543f44405fe96fae5191
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e453-initialise-the-basic-vectors
---

# initialise the BASIC vectors



# $E453 — initialise the BASIC vectors

## Disassemblatura
```assembly
.E453  A2 0B    LDX #$0B   ; set byte count
.E455  BD 47 E4 LDA $E447,X   ; get byte from table
.E458  9D 00 03 STA $0300,X   ; save byte to RAM
.E45B  CA       DEX   ; decrement index
.E45C  10 F7    BPL $E455   ; loop if more to do
.E45E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E453**: set byte count
- **$E455**: get byte from table
- **$E458**: save byte to RAM
- **$E45B**: decrement index
- **$E45C**: loop if more to do

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E453**: 6 vectors to be copied
- **$E45B**: next byte
- **$E45C**: ready
- **$E45E**: return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e453-initialise-the-basic-vectors]]
