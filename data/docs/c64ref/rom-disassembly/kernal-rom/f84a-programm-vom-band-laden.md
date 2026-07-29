---
title: Programm vom Band laden
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f84a-programm-vom-band-laden
- f92c-lesen
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F84A
  address_end: $F862
  symbol: programm-vom-band-laden
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F84A**: wartet auf Play-Taste'
---

# $F84A — Programm vom Band laden

## Disassemblatura
```assembly
.F84A  20 17 F8 JSR $F817   ; wartet auf Play-Taste
.F84D  B0 1F    BCS $F86E   ; STOP-Taste gedrückt ?
.F84F  78       SEI   ; Interrupt verhindern
.F850  A9 00    LDA #$00   ; Arbeitsspeicher für IRQ- Routine löschen
.F852  85 AA    STA $AA   ; Eingabebytespeicher (read)
.F854  85 B4    STA $B4   ; Band Hilfszeiger
.F856  85 B0    STA $B0   ; Kassetten Zeitkonstante
.F858  85 9E    STA $9E   ; Korrekturzähler Pass 1
.F85A  85 9F    STA $9F   ; Korrekturzähler Pass 2
.F85C  85 9C    STA $9C   ; Flag für Byte emfngen
.F85E  A9 90    LDA #$90   ; Bitwert IRQ an Pin 'Flag'
.F860  A2 0E    LDX #$0E   ; Nummer des IRQ-Vektors, $F92C
.F862  D0 11    BNE $F875   ; unbedingter Sprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F84A**: wartet auf Play-Taste
- **$F84D**: STOP-Taste gedrückt ?
- **$F84F**: Interrupt verhindern
- **$F850**: Arbeitsspeicher für IRQ- Routine löschen
- **$F852**: Eingabebytespeicher (read)
- **$F854**: Band Hilfszeiger
- **$F856**: Kassetten Zeitkonstante
- **$F858**: Korrekturzähler Pass 1
- **$F85A**: Korrekturzähler Pass 2
- **$F85C**: Flag für Byte emfngen
- **$F85E**: Bitwert IRQ an Pin 'Flag'
- **$F860**: Nummer des IRQ-Vektors, $F92C
- **$F862**: unbedingter Sprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*