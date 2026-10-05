---
id: src-ef2e-set-dsr-signal-not-present
type: source
title: 'Source Summary: set DSR signal not present'
aliases:
- set DSR signal not present
- ef2e-set-dsr-signal-not-present.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef2e-set-dsr-signal-not-present.md
  sha256: 12252d0b62d0a12577b744d80b3ee5140535d5b1ba455dd319c142dd79b01730
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set DSR signal not present

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef2e-set-dsr-signal-not-present.md`
**SHA256**: `12252d0b62d0a12577b744d80b3ee5140535d5b1ba455dd319c142dd79b01730`

## Summary



# $EF2E — set DSR signal not present

## Disassemblatura
```assembly
.EF2E  A9 40    LDA #$40   ; set DSR signal not present
.EF30  2C       .BYTE $2C   ; makes next line BIT $10A9
```


## Commenti

### Original Disassembly (—)
- **$EF2E**: set DSR signal not present
- **$EF30**: makes next line BIT $10A9

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EF2E**: entrypoint for 'NO DSR'
- **$EF30**: mask next LDA-command
- **$EF31**: entrypoint...
