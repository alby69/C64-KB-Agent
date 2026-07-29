---
title: check room on stack for A bytes
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
- a3fb-prfung-auf-platz-im-stapel
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A3FB
  address_end: $A407
  symbol: check-room-on-stack-for-a-bytes
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A3FB**: *2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A3FB**: Akku muß die halbe Zahl an'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A3FE**: ...MEM FULL ERR'
---

# $A3FB — check room on stack for A bytes

## Disassemblatura
```assembly
.A3FB  0A       ASL   ; *2
.A3FC  69 3E    ADC #$3E   ; need at least $3E bytes free
.A3FE  B0 35    BCS $A435   ; if overflow go do out of memory error then warm start
.A400  85 22    STA $22   ; save result in temp byte
.A402  BA       TSX   ; copy stack
.A403  E4 22    CPX $22   ; compare new limit with stack
.A405  90 2E    BCC $A435   ; if stack < limit do out of memory error then warm start
.A407  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A3FB**: *2
- **$A3FC**: need at least $3E bytes free
- **$A3FE**: if overflow go do out of memory error then warm start
- **$A400**: save result in temp byte
- **$A402**: copy stack
- **$A403**: compare new limit with stack
- **$A405**: if stack < limit do out of memory error then warm start

### Commodore-64-intern-Buch (Commodore)
- **$A3FB**: Akku muß die halbe Zahl an
- **$A3FC**: erforderlichem Platz haben
- **$A3FE**: gibt 'OUT OF MEMORY'
- **$A400**: Wert merken
- **$A402**: Ist Stapelzeiger kleiner
- **$A403**: (2 * Akku + 62)?
- **$A405**: Wenn ja, dann OUT OF MEMORY
- **$A407**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A3FE**: ...MEM FULL ERR
- **$A405**: ...MEM FULL ERR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*