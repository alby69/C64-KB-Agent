---
title: minus operator
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
  address: $BFB4
  address_end: $BFBE
  symbol: minus-operator
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BFB4**: Exponent'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BFB4**: IF FAC=0, NO NEED TO COMPLEMENT'
---

# $BFB4 — minus operator

## Disassemblatura
```assembly
.BFB4  A5 61    LDA $61
.BFB6  F0 06    BEQ $BFBE
.BFB8  A5 66    LDA $66
.BFBA  49 FF    EOR #$FF
.BFBC  85 66    STA $66
.BFBE  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$BFB4**: Exponent
- **$BFB6**: Zahl gleich null, dann fertig
- **$BFB8**: Vorzeichen
- **$BFBA**: invertieren und
- **$BFBC**: speichern
- **$BFBE**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BFB4**: IF FAC=0, NO NEED TO COMPLEMENT
- **$BFB6**: YES, FAC=0
- **$BFB8**: NO, SO TOGGLE SIGN
- **$BFBF**: LOG(E) TO BASE 2
- **$BFC4**: ( # OF TERMS IN POLYNOMIAL) - 1
- **$BFC5**: (LOG(2)^7)/8!
- **$BFCA**: (LOG(2)^6)/7!
- **$BFCF**: (LOG(2)^5)/6!
- **$BFD4**: (LOG(2)^4)/5!
- **$BFD9**: (LOG(2)^3)/4!
- **$BFDE**: (LOG(2)^2)/3!
- **$BFE3**: LOG(2)/2!
- **$BFE8**: 1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*