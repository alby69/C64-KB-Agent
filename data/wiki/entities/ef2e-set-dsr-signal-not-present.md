---
id: ef2e-set-dsr-signal-not-present
type: entity
title: set DSR signal not present
aliases:
- set DSR signal not present
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef2e-set-dsr-signal-not-present.md
  sha256: 12252d0b62d0a12577b744d80b3ee5140535d5b1ba455dd319c142dd79b01730
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ef2e-set-dsr-signal-not-present
---

# set DSR signal not present



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
- **$EF31**: entrypoint for 'NO CTS'
- **$EF33**: RSSTAT, 6551 status register image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ef2e-set-dsr-signal-not-present]]
