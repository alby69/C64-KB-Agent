---
title: add 0.5 to FAC1 (round FAC1)
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
- b849-fac-fac-05
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B849
  address_end: $B84D
  symbol: add-05-to-fac1-round-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B849**: set 0.5 pointer low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B849**: Zeiger auf'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$B849**: low  BF11'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B849**: FAC+1/2 -> FAC'
---

# $B849 — add 0.5 to FAC1 (round FAC1)

## Disassemblatura
```assembly
.B849  A9 11    LDA #$11   ; set 0.5 pointer low byte
.B84B  A0 BF    LDY #$BF   ; set 0.5 pointer high byte
.B84D  4C 67 B8 JMP $B867   ; add (AY) to FAC1
```


## Commenti

### Original Disassembly (—)
- **$B849**: set 0.5 pointer low byte
- **$B84B**: set 0.5 pointer high byte
- **$B84D**: add (AY) to FAC1

### Commodore-64-intern-Buch (Commodore)
- **$B849**: Zeiger auf
- **$B84B**: Konstante 0.5
- **$B84D**: FAC = FAC + Konstante (A/Y)

### Marko Mäkelä (Marko Mäkelä)
- **$B849**: low  BF11
- **$B84B**: high BF11

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B849**: FAC+1/2 -> FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*