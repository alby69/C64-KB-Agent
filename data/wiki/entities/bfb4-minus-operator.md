---
id: bfb4-minus-operator
type: entity
title: minus operator
aliases:
- minus operator
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bfb4-minus-operator.md
  sha256: 171e44f04bdf2e0bd4c413b5e51884b9588cd9dcc967657b764193fec4e71804
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bfb4-minus-operator
---

# minus operator



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

## References
- Source: [[src-bfb4-minus-operator]]
