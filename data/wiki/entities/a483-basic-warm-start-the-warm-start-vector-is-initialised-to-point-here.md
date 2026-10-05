---
id: a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here
type: entity
title: BASIC warm start, the warm start vector is initialised to point here
aliases:
- BASIC warm start, the warm start vector is initialised to point here
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here.md
  sha256: 290d04c5f1a11085e9d3cfd6796ee19379b9c9dbb1fe22b7ce55ec76f0f80561
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here
---

# BASIC warm start, the warm start vector is initialised to point here



# $A483 — BASIC warm start, the warm start vector is initialised to point here

## Disassemblatura
```assembly
.A483  20 60 A5 JSR $A560   ; call for BASIC input
.A486  86 7A    STX $7A   ; save BASIC execute pointer low byte
.A488  84 7B    STY $7B   ; save BASIC execute pointer high byte
.A48A  20 73 00 JSR $0073   ; increment and scan memory
.A48D  AA       TAX   ; copy byte to set flags
.A48E  F0 F0    BEQ $A480   ; loop if no input got to interpret the input line now ....
.A490  A2 FF    LDX #$FF   ; current line high byte to -1, indicates immediate mode
.A492  86 3A    STX $3A   ; set current line number high byte
.A494  90 06    BCC $A49C   ; if numeric character go handle new BASIC line no line number .. immediate mode
.A496  20 79 A5 JSR $A579   ; crunch keywords into BASIC tokens
.A499  4C E1 A7 JMP $A7E1   ; go scan and interpret code
```


## Commenti

### Original Disassembly (—)
- **$A483**: call for BASIC input
- **$A486**: save BASIC execute pointer low byte
- **$A488**: save BASIC execute pointer high byte
- **$A48A**: increment and scan memory
- **$A48D**: copy byte to set flags
- **$A48E**: loop if no input got to interpret the input line now ....
- **$A490**: current line high byte to -1, indicates immediate mode
- **$A492**: set current line number high byte
- **$A494**: if numeric character go handle new BASIC line no line number .. immediate mode
- **$A496**: crunch keywords into BASIC tokens
- **$A499**: go scan and interpret code

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a483-basic-warm-start-the-warm-start-vector-is-initialised-to-point-here]]
