---
id: f838-wait-for-playrecord
type: entity
title: wait for PLAY/RECORD
aliases:
- wait for PLAY/RECORD
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f838-wait-for-playrecord.md
  sha256: dc9d57077e8a36156f0cb1abcfeb90d40f7a0d265eff12b896189a814bdd3b82
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f838-wait-for-playrecord
---

# wait for PLAY/RECORD



# $F838 — wait for PLAY/RECORD

## Disassemblatura
```assembly
.F838  20 2E F8 JSR $F82E   ; return the cassette sense in Zb
.F83B  F0 F9    BEQ $F836   ; exit if switch closed cassette switch was open
.F83D  A0 2E    LDY #$2E   ; index to "PRESS RECORD & PLAY ON TAPE"
.F83F  D0 DD    BNE $F81E   ; display message and wait for switch, branch always
```


## Commenti

### Original Disassembly (—)
- **$F838**: return the cassette sense in Zb
- **$F83B**: exit if switch closed cassette switch was open
- **$F83D**: index to "PRESS RECORD & PLAY ON TAPE"
- **$F83F**: display message and wait for switch, branch always

### Commodore-64-intern-Buch (Commodore)
- **$F838**: fragt Bandtaste ab
- **$F83B**: gedrückt, dann fertig
- **$F83D**: Offset für 'PRESS RECORD & PLAY ON TAPE'
- **$F83F**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f838-wait-for-playrecord]]
