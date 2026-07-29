---
title: perform SQR()
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
- bf71-basic-funktion-sqr
- bf78-hoch-konstante-ay
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BF71
  address_end: $BF78
  symbol: perform-sqr
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BF71**: round and copy FAC1 to FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BF71**: FAC runden und nach ARG'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BF74**: SET UP POWER OF 0.5'
---

# $BF71 — perform SQR()

## Disassemblatura
```assembly
.BF71  20 0C BC JSR $BC0C   ; round and copy FAC1 to FAC2
.BF74  A9 11    LDA #$11   ; set 0.5 pointer low address
.BF76  A0 BF    LDY #$BF   ; set 0.5 pointer high address
.BF78  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
```


## Commenti

### Original Disassembly (—)
- **$BF71**: round and copy FAC1 to FAC2
- **$BF74**: set 0.5 pointer low address
- **$BF76**: set 0.5 pointer high address
- **$BF78**: unpack memory (AY) into FAC1

### Commodore-64-intern-Buch (Commodore)
- **$BF71**: FAC runden und nach ARG
- **$BF74**: Zeiger auf
- **$BF76**: Konstante 0.5

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BF74**: SET UP POWER OF 0.5

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*