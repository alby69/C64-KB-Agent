---
id: e195-do-ready-return-to-basic
type: entity
title: do READY return to BASIC
aliases:
- do READY return to BASIC
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e195-do-ready-return-to-basic.md
  sha256: 091ac220c0563e372f0ccdc1552de64a6aa9a1ad799c8e67d0bc4e7502ba34cf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e195-do-ready-return-to-basic
---

# do READY return to BASIC



# $E195 — do READY return to BASIC

## Disassemblatura
```assembly
.E195  20 B7 FF JSR $FFB7   ; read I/O status word
.E198  29 BF    AND #$BF   ; mask x0xx xxxx, clear read error
.E19A  F0 05    BEQ $E1A1   ; branch if no errors
.E19C  A2 1D    LDX #$1D   ; error $1D, load error
.E19E  4C 37 A4 JMP $A437   ; do error #X then warm start
.E1A1  A5 7B    LDA $7B   ; get BASIC execute pointer high byte
.E1A3  C9 02    CMP #$02   ; compare with $02xx
.E1A5  D0 0E    BNE $E1B5   ; branch if not immediate mode
.E1A7  86 2D    STX $2D   ; set start of variables low byte
.E1A9  84 2E    STY $2E   ; set start of variables high byte
.E1AB  A9 76    LDA #$76   ; set "READY." pointer low byte
.E1AD  A0 A3    LDY #$A3   ; set "READY." pointer high byte
.E1AF  20 1E AB JSR $AB1E   ; print null terminated string
.E1B2  4C 2A A5 JMP $A52A   ; reset execution, clear variables, flush stack, rebuild BASIC chain and do warm start
.E1B5  20 8E A6 JSR $A68E   ; set BASIC execute pointer to start of memory - 1
.E1B8  20 33 A5 JSR $A533   ; rebuild BASIC line chaining
.E1BB  4C 77 A6 JMP $A677   ; rebuild BASIC line chaining, do RESTORE and return
```


## Commenti

### Original Disassembly (—)
- **$E195**: read I/O status word
- **$E198**: mask x0xx xxxx, clear read error
- **$E19A**: branch if no errors
- **$E19C**: error $1D, load error
- **$E19E**: do error #X then warm start
- **$E1A1**: get BASIC execute pointer high byte
- **$E1A3**: compare with $02xx
- **$E1A5**: branch if not immediate mode
- **$E1A7**: set start of variables low byte
- **$E1A9**: set start of variables high byte
- **$E1AB**: set "READY." pointer low byte
- **$E1AD**: set "READY." pointer high byte
- **$E1AF**: print null terminated string
- **$E1B2**: reset execution, clear variables, flush stack, rebuild BASIC chain and do warm start
- **$E1B5**: set BASIC execute pointer to start of memory - 1
- **$E1B8**: rebuild BASIC line chaining
- **$E1BB**: rebuild BASIC line chaining, do RESTORE and return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e195-do-ready-return-to-basic]]
