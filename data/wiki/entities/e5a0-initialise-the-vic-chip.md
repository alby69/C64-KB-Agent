---
id: e5a0-initialise-the-vic-chip
type: entity
title: initialise the vic chip
aliases:
- initialise the vic chip
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e5a0-initialise-the-vic-chip.md
  sha256: 14ce65efbac65193129907383bcc8588689fcb1678ca8c46047c4fd4c165cc52
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e5a0-initialise-the-vic-chip
---

# initialise the vic chip



# $E5A0 — initialise the vic chip

## Disassemblatura
```assembly
.E5A0  A9 03    LDA #$03   ; set the screen as the output device
.E5A2  85 9A    STA $9A   ; save the output device number
.E5A4  A9 00    LDA #$00   ; set the keyboard as the input device
.E5A6  85 99    STA $99   ; save the input device number
.E5A8  A2 2F    LDX #$2F   ; set the count/index
.E5AA  BD B8 EC LDA $ECB8,X   ; get a vic ii chip initialisation value
.E5AD  9D FF CF STA $CFFF,X   ; save it to the vic ii chip
.E5B0  CA       DEX   ; decrement the count/index
.E5B1  D0 F7    BNE $E5AA   ; loop if more to do
.E5B3  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E5A0**: set the screen as the output device
- **$E5A2**: save the output device number
- **$E5A4**: set the keyboard as the input device
- **$E5A6**: save the input device number
- **$E5A8**: set the count/index
- **$E5AA**: get a vic ii chip initialisation value
- **$E5AD**: save it to the vic ii chip
- **$E5B0**: decrement the count/index
- **$E5B1**: loop if more to do

### Commodore-64-intern-Buch (Commodore)
- **$E5A0**: Ausgabe auf
- **$E5A2**: Bildschirm
- **$E5A4**: Eingabe von
- **$E5A6**: Tastatur
- **$E5A8**: 47
- **$E5AA**: Konstanten
- **$E5AD**: in Videokontroller schreiben
- **$E5B0**: Zähler erniedrigen
- **$E5B1**: schon alle?
- **$E5B3**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e5a0-initialise-the-vic-chip]]
