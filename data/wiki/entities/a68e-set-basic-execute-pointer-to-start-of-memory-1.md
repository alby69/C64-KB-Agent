---
id: a68e-set-basic-execute-pointer-to-start-of-memory-1
type: entity
title: set BASIC execute pointer to start of memory - 1
aliases:
- set BASIC execute pointer to start of memory - 1
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a68e-set-basic-execute-pointer-to-start-of-memory-1.md
  sha256: 469b064b65217a7d132cb8e5dd737bf6e9612e26f00faebbfa821c21147f7d88
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a68e-set-basic-execute-pointer-to-start-of-memory-1
---

# set BASIC execute pointer to start of memory - 1



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

## References
- Source: [[src-a68e-set-basic-execute-pointer-to-start-of-memory-1]]
