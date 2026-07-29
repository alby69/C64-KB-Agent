---
title: FLOAT UNSIGNED VALUE IN FAC+1,2
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
- bc44-float-unsigned-value-in-fac12
- bc5b-fac
- clear
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $BC44
  address_end: $BC48
  symbol: float-unsigned-value-in-fac12
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC44**: MSBIT=0, SET CARRY; =1, CLEAR CARRY'
---

# $BC44 — FLOAT UNSIGNED VALUE IN FAC+1,2

## Disassemblatura
```assembly
.BC44  A5 62    LDA $62   ; MSBIT=0, SET CARRY; =1, CLEAR CARRY
.BC46  49 FF    EOR #$FF
.BC48  2A       ROL
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC44**: MSBIT=0, SET CARRY; =1, CLEAR CARRY

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*