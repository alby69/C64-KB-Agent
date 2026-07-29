---
title: set the tape buffer start and end pointers
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f7d7-ferstartadresse-c0-192
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F7D7
  address_end: $F7E9
  symbol: set-the-tape-buffer-start-and-end-pointers
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F7D7**: get tape buffer start pointer in XY'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F7D7**: BandpufferaAdresse holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

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