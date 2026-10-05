---
id: b1b2-evaluate-integer-expression
type: entity
title: evaluate integer expression
aliases:
- evaluate integer expression
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b1b2-evaluate-integer-expression.md
  sha256: 00d07214ec7d6d61ea9b7962dd7656465c5b8fffb87dc3c9f5ff7d1495f12bb1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b1b2-evaluate-integer-expression
---

# evaluate integer expression



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

## References
- Source: [[src-b1b2-evaluate-integer-expression]]
