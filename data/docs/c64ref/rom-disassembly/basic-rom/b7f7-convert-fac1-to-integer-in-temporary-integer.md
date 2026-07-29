---
title: convert FAC_1 to integer in temporary integer
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
- b7f7-16-bit-zahl-wandeln
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B7F7
  address_end: $B80C
  symbol: convert-fac1-to-integer-in-temporary-integer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B7F7**: get FAC1 sign'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B7F7**: Vorzeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B7F7**: FAC < 2^16?'
---

# $B7F7 — convert FAC_1 to integer in temporary integer

## Disassemblatura
```assembly
.B7F7  A5 66    LDA $66   ; get FAC1 sign
.B7F9  30 9D    BMI $B798   ; if -ve do illegal quantity error then warm start
.B7FB  A5 61    LDA $61   ; get FAC1 exponent
.B7FD  C9 91    CMP #$91   ; compare with exponent = 2^16
.B7FF  B0 97    BCS $B798   ; if >= do illegal quantity error then warm start
.B801  20 9B BC JSR $BC9B   ; convert FAC1 floating to fixed
.B804  A5 64    LDA $64   ; get FAC1 mantissa 3
.B806  A4 65    LDY $65   ; get FAC1 mantissa 4
.B808  84 14    STY $14   ; save temporary integer low byte
.B80A  85 15    STA $15   ; save temporary integer high byte
.B80C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B7F7**: get FAC1 sign
- **$B7F9**: if -ve do illegal quantity error then warm start
- **$B7FB**: get FAC1 exponent
- **$B7FD**: compare with exponent = 2^16
- **$B7FF**: if >= do illegal quantity error then warm start
- **$B801**: convert FAC1 floating to fixed
- **$B804**: get FAC1 mantissa 3
- **$B806**: get FAC1 mantissa 4
- **$B808**: save temporary integer low byte
- **$B80A**: save temporary integer high byte

### Commodore-64-intern-Buch (Commodore)
- **$B7F7**: Vorzeichen
- **$B7F9**: negativ, dann 'ILLEGAL QUANTITY'
- **$B7FB**: Exponent
- **$B7FD**: Zahl mit 65536 vergleichen
- **$B7FF**: größer, dann
- **$B801**: 'ILLEGAL QUANTITY' FAC in Adressformat wandeln
- **$B804**: Wert
- **$B806**: holen
- **$B808**: und nach $14/$15
- **$B80A**: speichern
- **$B80C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B7F7**: FAC < 2^16?
- **$B7FF**: NO, ILLEGAL QUANTITY
- **$B801**: CONVERT TO INTEGER
- **$B804**: COPY IT INTO LINNUM
- **$B808**: TO LINNUM

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*