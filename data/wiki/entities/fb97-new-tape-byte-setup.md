---
id: fb97-new-tape-byte-setup
type: entity
title: new tape byte setup
aliases:
- new tape byte setup
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fb97-new-tape-byte-setup.md
  sha256: 80bce4874d7ccfd81045055cfd3ef0f01059db6ec73a0613a9985481759ddc39
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fb97-new-tape-byte-setup
---

# new tape byte setup



# $FB97 — new tape byte setup

## Disassemblatura
```assembly
.FB97  A9 08    LDA #$08   ; eight bits to do
.FB99  85 A3    STA $A3   ; set bit count
.FB9B  A9 00    LDA #$00   ; clear A
.FB9D  85 A4    STA $A4   ; clear tape bit cycle phase
.FB9F  85 A8    STA $A8   ; clear start bit first cycle done flag
.FBA1  85 9B    STA $9B   ; clear byte parity
.FBA3  85 A9    STA $A9   ; clear start bit check flag, set no start bit yet
.FBA5  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FB97**: eight bits to do
- **$FB99**: set bit count
- **$FB9B**: clear A
- **$FB9D**: clear tape bit cycle phase
- **$FB9F**: clear start bit first cycle done flag
- **$FBA1**: clear byte parity
- **$FBA3**: clear start bit check flag, set no start bit yet

### Commodore-64-intern-Buch (Commodore)
- **$FB97**: Zähler für 8 Bits
- **$FB99**: Nach $A3
- **$FB9B**: Akku mit $00 laden
- **$FB9D**: Bit-Impuls-Flag löschen
- **$FB9F**: Lesefehler Byte löschen
- **$FBA1**: Parity-Bit löschen
- **$FBA3**: Impulswechsel-Flag löschen
- **$FBA5**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fb97-new-tape-byte-setup]]
