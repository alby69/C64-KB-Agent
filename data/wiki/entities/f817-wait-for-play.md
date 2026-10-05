---
id: f817-wait-for-play
type: entity
title: wait for PLAY
aliases:
- wait for PLAY
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f817-wait-for-play.md
  sha256: 1655a19503abe0caa12f4be450e780026e9310b64ffccd3fd295194b03653051
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f817-wait-for-play
---

# wait for PLAY



# $F817 — wait for PLAY

## Disassemblatura
```assembly
.F817  20 2E F8 JSR $F82E   ; return cassette sense in Zb
.F81A  F0 1A    BEQ $F836   ; if switch closed just exit cassette switch was open
.F81C  A0 1B    LDY #$1B   ; index to "PRESS PLAY ON TAPE"
.F81E  20 2F F1 JSR $F12F   ; display kernel I/O message
.F821  20 D0 F8 JSR $F8D0   ; scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
.F824  20 2E F8 JSR $F82E   ; return cassette sense in Zb
.F827  D0 F8    BNE $F821   ; loop if the cassette switch is open
.F829  A0 6A    LDY #$6A   ; index to "OK"
.F82B  4C 2F F1 JMP $F12F   ; display kernel I/O message and return
```


## Commenti

### Original Disassembly (—)
- **$F817**: return cassette sense in Zb
- **$F81A**: if switch closed just exit cassette switch was open
- **$F81C**: index to "PRESS PLAY ON TAPE"
- **$F81E**: display kernel I/O message
- **$F821**: scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
- **$F824**: return cassette sense in Zb
- **$F827**: loop if the cassette switch is open
- **$F829**: index to "OK"
- **$F82B**: display kernel I/O message and return

### Commodore-64-intern-Buch (Commodore)
- **$F817**: fragt BandtTaste ab
- **$F81A**: gedrückt, dann fertig
- **$F81C**: Offset für 'PRESS PLAY ON TAPE'
- **$F81E**: und ausgeben
- **$F821**: testet auf STOP-Taste
- **$F824**: fragt BandtTaste ab
- **$F827**: nicht gedrückt so erneut abfragen
- **$F829**: Offset für 'OK'
- **$F82B**: und ausgeben, Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f817-wait-for-play]]
