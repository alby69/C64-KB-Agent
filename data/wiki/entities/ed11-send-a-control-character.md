---
id: ed11-send-a-control-character
type: entity
title: send a control character
aliases:
- send a control character
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ed11-send-a-control-character.md
  sha256: c447cb83f0133a7dfd788d017ef86fe5fbba4f7a8badf4e50c85a22efcf0d070
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ed11-send-a-control-character
---

# send a control character



# $ED11 — send a control character

## Disassemblatura
```assembly
.ED11  48       PHA   ; save device address
.ED12  24 94    BIT $94   ; test deferred character flag
.ED14  10 0A    BPL $ED20   ; if no deferred character continue
.ED16  38       SEC   ; else flag EOI
.ED17  66 A3    ROR $A3   ; rotate into EOI flag byte
.ED19  20 40 ED JSR $ED40   ; Tx byte on serial bus
.ED1C  46 94    LSR $94   ; clear deferred character flag
.ED1E  46 A3    LSR $A3   ; clear EOI flag
.ED20  68       PLA   ; restore the device address
```


## Commenti

### Original Disassembly (—)
- **$ED11**: save device address
- **$ED12**: test deferred character flag
- **$ED14**: if no deferred character continue
- **$ED16**: else flag EOI
- **$ED17**: rotate into EOI flag byte
- **$ED19**: Tx byte on serial bus
- **$ED1C**: clear deferred character flag
- **$ED1E**: clear EOI flag
- **$ED20**: restore the device address

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ed11-send-a-control-character]]
