---
title: compute pointer to array body
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $B194
  address_end: $B1A4
  symbol: compute-pointer-to-array-body
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B194**: Anzahl der Dimensionen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B194**: GET # OF DIMENSIONS'
---

# $B194 — compute pointer to array body

## Disassemblatura
```assembly
.B194  A5 0B    LDA $0B
.B196  0A       ASL
.B197  69 05    ADC #$05
.B199  65 5F    ADC $5F
.B19B  A4 60    LDY $60
.B19D  90 01    BCC $B1A0
.B19F  C8       INY
.B1A0  85 58    STA $58
.B1A2  84 59    STY $59
.B1A4  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B194**: Anzahl der Dimensionen
- **$B196**: mal 2
- **$B197**: plus 5
- **$B199**: zu $5F und
- **$B19B**: $60 addieren
- **$B19D**: Erhöhung umgehen
- **$B19F**: Übertrag addieren
- **$B1A0**: Ergebnis-Zeiger nach
- **$B1A2**: $58/59 speichern
- **$B1A4**: Rücksprung
- **$B1A5**: Konstante -32768

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B194**: GET # OF DIMENSIONS
- **$B196**: #DIMS*2 (SIZE OF EACH DIM IN 2 BYTES)
- **$B197**: + 5 (2 FOR NAME, 2 FOR OFFSET TO NEXT ARRAY, AND 1 FOR #DIMS
- **$B199**: ADDRESS OF TH IS ARRAY IN ARYTAB
- **$B1A0**: ADDRESS OF FIRST VALUE IN ARRAY
- **$B1A5**: -32768 IN FLOATING POINT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*