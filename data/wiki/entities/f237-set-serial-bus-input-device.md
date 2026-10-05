---
id: f237-set-serial-bus-input-device
type: entity
title: set serial bus input device
aliases:
- set serial bus input device
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f237-set-serial-bus-input-device.md
  sha256: 8d1fb9dbce2de5539d1fffc0b9d68eae90c7bf5255307abc6a801de6ad36d8e8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f237-set-serial-bus-input-device
---

# set serial bus input device



# $F237 — set serial bus input device

## Disassemblatura
```assembly
.F237  AA       TAX
.F238  20 09 ED JSR $ED09
.F23B  A5 B9    LDA $B9
.F23D  10 06    BPL $F245
.F23F  20 CC ED JSR $EDCC
.F242  4C 48 F2 JMP $F248
.F245  20 C7 ED JSR $EDC7
.F248  8A       TXA
.F249  24 90    BIT $90
.F24B  10 E6    BPL $F233
.F24D  4C 07 F7 JMP $F707
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F237**: Geräteadresse retten
- **$F238**: TALK senden
- **$F23B**: Sekundäradresse laden
- **$F23D**: verzweige wenn kleiner 128
- **$F23F**: wartet auf Takt-Signal
- **$F242**: nächsten Befehl überspringen
- **$F245**: Sekundäradresse für TALK senden
- **$F248**: Geräteadresse wiederholen
- **$F249**: Status abfragen
- **$F24B**: verzweige wenn ok
- **$F24D**: sonst 'DEVICE NOT PRESENT'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f237-set-serial-bus-input-device]]
