---
title: perform ASC()
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
- b78b-basic-funktion-asc
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B78B
  address_end: $B795
  symbol: perform-asc
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B78B**: evaluate string, get length in A (and Y)'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B78B**: String holen, Zeiger in $22/$23, Länge in Y'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B78B**: GET STRING, GET LENGTH IN Y-REG'
---

# $B78B — perform ASC()

## Disassemblatura
```assembly
.B78B  20 82 B7 JSR $B782   ; evaluate string, get length in A (and Y)
.B78E  F0 08    BEQ $B798   ; if null do illegal quantity error then warm start
.B790  A0 00    LDY #$00   ; set index to first character
.B792  B1 22    LDA ($22),Y   ; get byte
.B794  A8       TAY   ; copy to Y
.B795  4C A2 B3 JMP $B3A2   ; convert Y to byte in FAC1 and return
```


## Commenti

### Original Disassembly (—)
- **$B78B**: evaluate string, get length in A (and Y)
- **$B78E**: if null do illegal quantity error then warm start
- **$B790**: set index to first character
- **$B792**: get byte
- **$B794**: copy to Y
- **$B795**: convert Y to byte in FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$B78B**: String holen, Zeiger in $22/$23, Länge in Y
- **$B78E**: Länge gleich null, 'ILLEGAL QUANTITY'
- **$B790**: Zähler auf Null
- **$B792**: erstes Zeichen holen
- **$B794**: ASCII-Kode
- **$B795**: nach Fließkomma wandeln
- **$B798**: 'ILLEGAL QUANTITY'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B78B**: GET STRING, GET LENGTH IN Y-REG
- **$B78E**: ERROR IF LENGTH 0
- **$B792**: GET 1ST CHAR OF STRING
- **$B795**: FLOAT Y-REG INTO FAC
- **$B798**: ILLEGAL QUANTITY ERROR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*