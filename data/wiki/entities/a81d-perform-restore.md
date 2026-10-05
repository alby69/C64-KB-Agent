---
id: a81d-perform-restore
type: entity
title: perform RESTORE
aliases:
- perform RESTORE
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a81d-perform-restore.md
  sha256: f4fb1cf6940906d31e32ea61a7085a392d0ea21c281d577f3fe632f57694302e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a81d-perform-restore
---

# perform RESTORE



# $A81D — perform RESTORE

## Disassemblatura
```assembly
.A81D  38       SEC   ; set carry for subtract
.A81E  A5 2B    LDA $2B   ; get start of memory low byte
.A820  E9 01    SBC #$01   ; -1
.A822  A4 2C    LDY $2C   ; get start of memory high byte
.A824  B0 01    BCS $A827   ; branch if no rollunder
.A826  88       DEY   ; else decrement high byte
.A827  85 41    STA $41   ; set DATA pointer low byte
.A829  84 42    STY $42   ; set DATA pointer high byte
.A82B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A81D**: set carry for subtract
- **$A81E**: get start of memory low byte
- **$A820**: -1
- **$A822**: get start of memory high byte
- **$A824**: branch if no rollunder
- **$A826**: else decrement high byte
- **$A827**: set DATA pointer low byte
- **$A829**: set DATA pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$A81D**: Carry setzen (Subtraktion)
- **$A81E**: Programmstartzeiger (LOW)
- **$A820**: laden und davon 1 abziehen
- **$A822**: und HIGH-Byte holen
- **$A826**: LOW-Byte -1
- **$A827**: als DATA-Zeiger
- **$A829**: abspeichern
- **$A82B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$A82C**: test stop key

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A81D**: SET DATPTR TO BEGINNING OF PROGRAM
- **$A826**: SET DATPTR TO Y,A

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a81d-perform-restore]]
