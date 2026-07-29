---
title: get FAC1 sign
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
- bc2b-vorzeichen-von-fac-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC2B
  address_end: $BC2D
  symbol: get-fac1-sign
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC2B**: get FAC1 exponent'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC2B**: wenn null,'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC2B**: CHECK SIGN OF FAC AND'
---

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