---
title: evaluate integer expression
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
- b1b2-nach-integer
- b1bb-convert-fac-to-integer
- b1bf-convert-fac-to-integer
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B1B2
  address_end: $B1CE
  symbol: evaluate-integer-expression
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B1B2**: increment and scan memory'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B1B2**: CHRGET nächstes Zeichen holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B1B2 — evaluate integer expression

## Disassemblatura
```assembly
.B1B2  20 73 00 JSR $0073   ; increment and scan memory
.B1B5  20 9E AD JSR $AD9E   ; evaluate expression evaluate integer expression, sign check
.B1B8  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.B1BB  A5 66    LDA $66   ; get FAC1 sign (b7)
.B1BD  30 0D    BMI $B1CC   ; do illegal quantity error if -ve evaluate integer expression, no sign check
.B1BF  A5 61    LDA $61   ; get FAC1 exponent
.B1C1  C9 90    CMP #$90   ; compare with exponent = 2^16 (n>2^15)
.B1C3  90 09    BCC $B1CE   ; if n<2^16 go convert FAC1 floating to fixed and return
.B1C5  A9 A5    LDA #$A5   ; set pointer low byte to -32768
.B1C7  A0 B1    LDY #$B1   ; set pointer high byte to -32768
.B1C9  20 5B BC JSR $BC5B   ; compare FAC1 with (AY)
.B1CC  D0 7A    BNE $B248   ; if <> do illegal quantity error then warm start
.B1CE  4C 9B BC JMP $BC9B   ; convert FAC1 floating to fixed and return
```


## Commenti

### Original Disassembly (—)
- **$B1B2**: increment and scan memory
- **$B1B5**: evaluate expression evaluate integer expression, sign check
- **$B1B8**: check if source is numeric, else do type mismatch
- **$B1BB**: get FAC1 sign (b7)
- **$B1BD**: do illegal quantity error if -ve evaluate integer expression, no sign check
- **$B1BF**: get FAC1 exponent
- **$B1C1**: compare with exponent = 2^16 (n>2^15)
- **$B1C3**: if n<2^16 go convert FAC1 floating to fixed and return
- **$B1C5**: set pointer low byte to -32768
- **$B1C7**: set pointer high byte to -32768
- **$B1C9**: compare FAC1 with (AY)
- **$B1CC**: if <> do illegal quantity error then warm start
- **$B1CE**: convert FAC1 floating to fixed and return

### Commodore-64-intern-Buch (Commodore)
- **$B1B2**: CHRGET nächstes Zeichen holen
- **$B1B5**: FRMEVL, Ausdruck auswerten
- **$B1B8**: prüft auf numerisch
- **$B1BB**: Vorzeichen?
- **$B1BD**: negativ: dann 'ILLEGAL QUANT'
- **$B1BF**: Exponent
- **$B1C1**: Betrag größer 32768?
- **$B1C3**: nein: $B1CE
- **$B1C5**: Zeiger auf
- **$B1C7**: Konstante -32768 setzen
- **$B1C9**: Vergleich FAC mit Konstante
- **$B1CC**: ungleich: 'ILLEGAL QUANT'
- **$B1CE**: wandelt Fließkomma in Integer

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*