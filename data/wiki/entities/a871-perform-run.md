---
id: a871-perform-run
type: entity
title: perform RUN
aliases:
- perform RUN
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a871-perform-run.md
  sha256: 3041925889c77e3d6f3d3efc9ba8c4a86fa0e39d6e7598031c7b0cdbf808487d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a871-perform-run
---

# perform RUN



# $A871 — perform RUN

## Disassemblatura
```assembly
.A871  08       PHP   ; save status
.A872  A9 00    LDA #$00   ; no control or kernal messages
.A874  20 90 FF JSR $FF90   ; control kernal messages
.A877  28       PLP   ; restore status
.A878  D0 03    BNE $A87D   ; branch if RUN n
.A87A  4C 59 A6 JMP $A659   ; reset execution to start, clear variables, flush stack and return
.A87D  20 60 A6 JSR $A660   ; go do "CLEAR"
.A880  4C 97 A8 JMP $A897   ; get n and do GOTO n
```


## Commenti

### Original Disassembly (—)
- **$A871**: save status
- **$A872**: no control or kernal messages
- **$A874**: control kernal messages
- **$A877**: restore status
- **$A878**: branch if RUN n
- **$A87A**: reset execution to start, clear variables, flush stack and return
- **$A87D**: go do "CLEAR"
- **$A880**: get n and do GOTO n

### Commodore-64-intern-Buch (Commodore)
- **$A871**: Statusregister retten
- **$A872**: Wert laden und
- **$A874**: Flag für Programmodus setzen
- **$A877**: Statusregister zurückholen
- **$A878**: weitere Zeichen (Zeilennr.)?
- **$A87A**: Programmzeiger setzen, CLR
- **$A87D**: CLR-Befehl
- **$A880**: GOTO-Befehl

### Marko Mäkelä (Marko Mäkelä)
- **$A87D**: do CLR
- **$A880**: do GOTO

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A871**: SAVE STATUS WHILE SUBTRACTING
- **$A877**: GET STATUS AGAIN (FROM CHRGET)
- **$A878**: PROBABLY A LINE NUMBER
- **$A87A**: START AT BEGINNING OF PROGRAM
- **$A87D**: CLEAR VARIABLES
- **$A880**: JOIN GOSUB STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a871-perform-run]]
