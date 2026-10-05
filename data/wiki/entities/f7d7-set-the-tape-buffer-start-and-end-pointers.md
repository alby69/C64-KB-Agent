---
id: f7d7-set-the-tape-buffer-start-and-end-pointers
type: entity
title: set the tape buffer start and end pointers
aliases:
- set the tape buffer start and end pointers
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f7d7-set-the-tape-buffer-start-and-end-pointers.md
  sha256: 24af910372527aff9f686612bd95a7f9a3ab5573ea35dbec7d49a97b992091b5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f7d7-set-the-tape-buffer-start-and-end-pointers
---

# set the tape buffer start and end pointers



# $F7D7 — set the tape buffer start and end pointers

## Disassemblatura
```assembly
.F7D7  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F7DA  8A       TXA   ; copy tape buffer start pointer low byte
.F7DB  85 C1    STA $C1   ; save as I/O address pointer low byte
.F7DD  18       CLC   ; clear carry for add
.F7DE  69 C0    ADC #$C0   ; add buffer length low byte
.F7E0  85 AE    STA $AE   ; save tape buffer end pointer low byte
.F7E2  98       TYA   ; copy tape buffer start pointer high byte
.F7E3  85 C2    STA $C2   ; save as I/O address pointer high byte
.F7E5  69 00    ADC #$00   ; add buffer length high byte
.F7E7  85 AF    STA $AF   ; save tape buffer end pointer high byte
.F7E9  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F7D7**: get tape buffer start pointer in XY
- **$F7DA**: copy tape buffer start pointer low byte
- **$F7DB**: save as I/O address pointer low byte
- **$F7DD**: clear carry for add
- **$F7DE**: add buffer length low byte
- **$F7E0**: save tape buffer end pointer low byte
- **$F7E2**: copy tape buffer start pointer high byte
- **$F7E3**: save as I/O address pointer high byte
- **$F7E5**: add buffer length high byte
- **$F7E7**: save tape buffer end pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$F7D7**: BandpufferaAdresse holen
- **$F7DA**: Pufferanfang LOW in Akku
- **$F7DB**: und speichern
- **$F7DD**: Carry für Addition löschen
- **$F7DE**: Endadresse = Startadresse + Länge $C0 (192)
- **$F7E0**: und Endadresse speichern
- **$F7E2**: Pufferanfang HIGH in Akku
- **$F7E3**: und speichern
- **$F7E5**: mit Übertrag addieren
- **$F7E7**: und speichern
- **$F7E9**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f7d7-set-the-tape-buffer-start-and-end-pointers]]
