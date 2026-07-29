---
title: negate FAC1
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- b947-mantisse-von-fac-invertieren
- b94d-2s-complement-of-fac-mantissa-only
- b96f-increment-fac-mantissa
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B947
  address_end: $B97D
  symbol: negate-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B947**: get FAC1 sign (b7)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B947**: FAC Vorzeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B947 — negate FAC1

## Disassemblatura
```assembly
.B947  A5 66    LDA $66   ; get FAC1 sign (b7)
.B949  49 FF    EOR #$FF   ; complement it
.B94B  85 66    STA $66   ; save FAC1 sign (b7) twos complement FAC1 mantissa
.B94D  A5 62    LDA $62   ; get FAC1 mantissa 1
.B94F  49 FF    EOR #$FF   ; complement it
.B951  85 62    STA $62   ; save FAC1 mantissa 1
.B953  A5 63    LDA $63   ; get FAC1 mantissa 2
.B955  49 FF    EOR #$FF   ; complement it
.B957  85 63    STA $63   ; save FAC1 mantissa 2
.B959  A5 64    LDA $64   ; get FAC1 mantissa 3
.B95B  49 FF    EOR #$FF   ; complement it
.B95D  85 64    STA $64   ; save FAC1 mantissa 3
.B95F  A5 65    LDA $65   ; get FAC1 mantissa 4
.B961  49 FF    EOR #$FF   ; complement it
.B963  85 65    STA $65   ; save FAC1 mantissa 4
.B965  A5 70    LDA $70   ; get FAC1 rounding byte
.B967  49 FF    EOR #$FF   ; complement it
.B969  85 70    STA $70   ; save FAC1 rounding byte
.B96B  E6 70    INC $70   ; increment FAC1 rounding byte
.B96D  D0 0E    BNE $B97D   ; exit if no overflow increment FAC1 mantissa
.B96F  E6 65    INC $65   ; increment FAC1 mantissa 4
.B971  D0 0A    BNE $B97D   ; finished if no rollover
.B973  E6 64    INC $64   ; increment FAC1 mantissa 3
.B975  D0 06    BNE $B97D   ; finished if no rollover
.B977  E6 63    INC $63   ; increment FAC1 mantissa 2
.B979  D0 02    BNE $B97D   ; finished if no rollover
.B97B  E6 62    INC $62   ; increment FAC1 mantissa 1
.B97D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B947**: get FAC1 sign (b7)
- **$B949**: complement it
- **$B94B**: save FAC1 sign (b7) twos complement FAC1 mantissa
- **$B94D**: get FAC1 mantissa 1
- **$B94F**: complement it
- **$B951**: save FAC1 mantissa 1
- **$B953**: get FAC1 mantissa 2
- **$B955**: complement it
- **$B957**: save FAC1 mantissa 2
- **$B959**: get FAC1 mantissa 3
- **$B95B**: complement it
- **$B95D**: save FAC1 mantissa 3
- **$B95F**: get FAC1 mantissa 4
- **$B961**: complement it
- **$B963**: save FAC1 mantissa 4
- **$B965**: get FAC1 rounding byte
- **$B967**: complement it
- **$B969**: save FAC1 rounding byte
- **$B96B**: increment FAC1 rounding byte
- **$B96D**: exit if no overflow increment FAC1 mantissa
- **$B96F**: increment FAC1 mantissa 4
- **$B971**: finished if no rollover
- **$B973**: increment FAC1 mantissa 3
- **$B975**: finished if no rollover
- **$B977**: increment FAC1 mantissa 2
- **$B979**: finished if no rollover
- **$B97B**: increment FAC1 mantissa 1

### Commodore-64-intern-Buch (Commodore)
- **$B947**: FAC Vorzeichen
- **$B949**: invertieren
- **$B94B**: und speichern
- **$B94D**: FAC
- **$B94F**: invertieren
- **$B951**: und speichern
- **$B953**: FAC
- **$B955**: invertieren
- **$B957**: und speichern
- **$B959**: FAC
- **$B95B**: invertieren
- **$B95D**: und speichern
- **$B95F**: FAC
- **$B961**: invertieren
- **$B963**: und speichern
- **$B965**: FAC-Rundungsbyte
- **$B967**: invertieren
- **$B969**: und speichern
- **$B96B**: Mantisse erhöhen
- **$B96D**: nicht Null? dann RTS
- **$B96F**: FAC erhöhen
- **$B971**: nicht Null? dann RTS
- **$B973**: FAC erhöhen
- **$B975**: nicht Null? dann RTS
- **$B977**: FAC erhöhen
- **$B979**: nicht Null? dann RTS
- **$B97B**: FAC erhöhen
- **$B97D**: Rücksprung
- **$B97E**: Nummer für 'OVERFLOW'
- **$B980**: Fehlermeldung ausgeben

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*