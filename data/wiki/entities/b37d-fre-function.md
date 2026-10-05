---
id: b37d-fre-function
type: entity
title: FRE function
aliases:
- FRE function
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b37d-fre-function.md
  sha256: a5847467455522ba6663279c66ae83307b487dcaeeb51ed9f0d7aa9d606b8b9a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b37d-fre-function
---

# FRE function



# $B37D — FRE function

## Disassemblatura
```assembly
.B37D  A5 0D    LDA $0D
.B37F  F0 03    BEQ $B384
.B381  20 A6 B6 JSR $B6A6
.B384  20 26 B5 JSR $B526
.B387  38       SEC
.B388  A5 33    LDA $33
.B38A  E5 31    SBC $31
.B38C  A8       TAY
.B38D  A5 34    LDA $34
.B38F  E5 32    SBC $32
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$B37D**: Typflag
- **$B37F**: kein String
- **$B381**: FRESTR
- **$B384**: Garbage Collection
- **$B387**: Carry setzen (Subtr.)
- **$B388**: Stringanfang (LOW)
- **$B38A**: - Variablenende (LOW)
- **$B38C**: ergibt freien Speicher
- **$B38D**: Stringanfang (HIGH)
- **$B38F**: - Variablenende (HIGH)
- **$B391**: Wert laden und
- **$B393**: Flag auf numerisch setzen
- **$B395**: LOW- und HIGH-Byte des
- **$B397**: Ergebnisses merken
- **$B399**: und nach
- **$B39B**: Fließkomma wandlen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B37D**: LOOK AT VALUE OF ARGUMENT
- **$B37F**: =0 MEANS REAL, =$FF MEANS STRING
- **$B381**: STRING, SO SET IT FREE IS TEMP
- **$B384**: COLLECT ALL THE GARBAGE IN SIGHT
- **$B387**: COMPUTE SPACE BETWEEN ARRAYS AND
- **$B388**: STRING TEMP AREA
- **$B38F**: FREE SPACE IN Y,A FALL INTO GIVAYF TO FLOAT THE VALUE NOTE THAT VALUES OVER 32767 WILL RETURN AS NEGATIVE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b37d-fre-function]]
