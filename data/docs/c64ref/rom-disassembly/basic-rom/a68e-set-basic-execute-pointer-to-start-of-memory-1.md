---
title: set BASIC execute pointer to start of memory - 1
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
- a68e-basic-start
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A68E
  address_end: $A69B
  symbol: set-basic-execute-pointer-to-start-of-memory-1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A68E**: clear carry for add'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A68E**: Carry löschen (Addition)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A68E**: TXTPTR = TXTTAB - 1'
---

# $A68E — set BASIC execute pointer to start of memory - 1

## Disassemblatura
```assembly
.A68E  18       CLC   ; clear carry for add
.A68F  A5 2B    LDA $2B   ; get start of memory low byte
.A691  69 FF    ADC #$FF   ; add -1 low byte
.A693  85 7A    STA $7A   ; set BASIC execute pointer low byte
.A695  A5 2C    LDA $2C   ; get start of memory high byte
.A697  69 FF    ADC #$FF   ; add -1 high byte
.A699  85 7B    STA $7B   ; save BASIC execute pointer high byte
.A69B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A68E**: clear carry for add
- **$A68F**: get start of memory low byte
- **$A691**: add -1 low byte
- **$A693**: set BASIC execute pointer low byte
- **$A695**: get start of memory high byte
- **$A697**: add -1 high byte
- **$A699**: save BASIC execute pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$A68E**: Carry löschen (Addition)
- **$A68F**: Zeiger auf Programmstart (LOW)
- **$A691**: minus 1 ergibt
- **$A693**: neuen CHRGET-Zeiger (LOW)
- **$A695**: Programmstart (HIGH)
- **$A697**: minus 1 ergibt
- **$A699**: CHRGET-Zeiger (HIGH)
- **$A69B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A68E**: TXTPTR = TXTTAB - 1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*