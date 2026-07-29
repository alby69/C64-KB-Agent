---
title: copy FAC2 to FAC1
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
- bbfc-arg-nach-fac-bertragen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BBFC
  address_end: $BC0B
  symbol: copy-fac2-to-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BBFC**: get FAC2 sign (b7) save FAC1 sign and copy ABS(FAC2)
      to FAC1'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BBFC**: ARG-Vorzeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BBFC**: COPY SIGN'
---

# $BBFC — copy FAC2 to FAC1

## Disassemblatura
```assembly
.BBFC  A5 6E    LDA $6E   ; get FAC2 sign (b7) save FAC1 sign and copy ABS(FAC2) to FAC1
.BBFE  85 66    STA $66   ; save FAC1 sign (b7)
.BC00  A2 05    LDX #$05   ; 5 bytes to copy
.BC02  B5 68    LDA $68,X   ; get byte from FAC2,X
.BC04  95 60    STA $60,X   ; save byte at FAC1,X
.BC06  CA       DEX   ; decrement count
.BC07  D0 F9    BNE $BC02   ; loop if not all done
.BC09  86 70    STX $70   ; clear FAC1 rounding byte
.BC0B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BBFC**: get FAC2 sign (b7) save FAC1 sign and copy ABS(FAC2) to FAC1
- **$BBFE**: save FAC1 sign (b7)
- **$BC00**: 5 bytes to copy
- **$BC02**: get byte from FAC2,X
- **$BC04**: save byte at FAC1,X
- **$BC06**: decrement count
- **$BC07**: loop if not all done
- **$BC09**: clear FAC1 rounding byte

### Commodore-64-intern-Buch (Commodore)
- **$BBFC**: ARG-Vorzeichen
- **$BBFE**: in FAC-Reg übertragen
- **$BC00**: 5 Bytes
- **$BC02**: ARG in
- **$BC04**: FAC
- **$BC06**: übertragen
- **$BC07**: schon alle Zeichen ?
- **$BC09**: FAC-Rundungsstelle löschen
- **$BC0B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BBFC**: COPY SIGN
- **$BC00**: MOVE 5 BYTES
- **$BC09**: ZERO EXTENSION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*