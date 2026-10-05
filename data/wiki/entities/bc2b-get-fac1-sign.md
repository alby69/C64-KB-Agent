---
id: bc2b-get-fac1-sign
type: entity
title: get FAC1 sign
aliases:
- get FAC1 sign
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc2b-get-fac1-sign.md
  sha256: 94bdff8b583a46cf548918e6c641ac2927c137140c87502c849439d95c5672e9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bc2b-get-fac1-sign
---

# get FAC1 sign



# $BC2B — get FAC1 sign

## Disassemblatura
```assembly
.BC2B  A5 61    LDA $61   ; get FAC1 exponent
.BC2D  F0 09    BEQ $BC38   ; exit if zero (already correct SGN(0)=0)
```


## Commenti

### Original Disassembly (—)
- **$BC2B**: get FAC1 exponent
- **$BC2D**: exit if zero (already correct SGN(0)=0)

### Commodore-64-intern-Buch (Commodore)
- **$BC2B**: wenn null,
- **$BC2D**: dann RTS
- **$BC2F**: FAC-Vorzeichen
- **$BC31**: holen
- **$BC32**: negativ?
- **$BC34**: dann RTS
- **$BC36**: sonst positiv
- **$BC38**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC2B**: CHECK SIGN OF FAC AND
- **$BC2D**: RETURN -1,0,1 IN A-REG
- **$BC31**: MSBIT TO CARRY
- **$BC32**: -1
- **$BC34**: MSBIT = 1
- **$BC36**: +1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bc2b-get-fac1-sign]]
