---
title: add signed integer from A to float accu
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
  address: $BD7E
  address_end: $BD8E
  symbol: add-signed-integer-from-a-to-float-accu
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BD7E**: SAVE ADDEND'
---

# $BD7E — add signed integer from A to float accu

## Disassemblatura
```assembly
.BD7E  48       PHA
.BD7F  20 0C BC JSR $BC0C
.BD82  68       PLA
.BD83  20 3C BC JSR $BC3C
.BD86  A5 6E    LDA $6E
.BD88  45 66    EOR $66
.BD8A  85 6F    STA $6F
.BD8C  A6 61    LDX $61
.BD8E  4C 6A B8 JMP $B86A
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BD7E**: SAVE ADDEND
- **$BD82**: GET ADDEND AGAIN
- **$BD83**: CONVERT TO FP VALUE IN FAC
- **$BD8C**: TO SIGNAL IF FAC=0
- **$BD8E**: PERFORM THE ADDITION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*