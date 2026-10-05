---
id: e8a1-test-for-line-decrement
type: entity
title: test for line decrement
aliases:
- test for line decrement
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e8a1-test-for-line-decrement.md
  sha256: 45c60248682dddf99e262d72b55ca617544842469a755cbc3ec419511f48df3f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e8a1-test-for-line-decrement
---

# test for line decrement



# $E8A1 — test for line decrement

## Disassemblatura
```assembly
.E8A1  A2 02    LDX #$02   ; set the count
.E8A3  A9 00    LDA #$00   ; set the column
.E8A5  C5 D3    CMP $D3   ; compare the column with the cursor column
.E8A7  F0 07    BEQ $E8B0   ; if at the start of the line go decrement the cursor row and exit
.E8A9  18       CLC   ; else clear carry for add
.E8AA  69 28    ADC #$28   ; increment to next line
.E8AC  CA       DEX   ; decrement loop count
.E8AD  D0 F6    BNE $E8A5   ; loop if more to test
.E8AF  60       RTS
.E8B0  C6 D6    DEC $D6   ; else decrement the cursor row
.E8B2  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E8A1**: set the count
- **$E8A3**: set the column
- **$E8A5**: compare the column with the cursor column
- **$E8A7**: if at the start of the line go decrement the cursor row and exit
- **$E8A9**: else clear carry for add
- **$E8AA**: increment to next line
- **$E8AC**: decrement loop count
- **$E8AD**: loop if more to test
- **$E8B0**: else decrement the cursor row

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E8A1**: test if PNTR is at the first column
- **$E8A3**: yepp
- **$E8A5**: add $28 (40)
- **$E8A7**: to test if cursor is at line two in the logical line
- **$E8AA**: test two lines
- **$E8AD**: decrement line number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e8a1-test-for-line-decrement]]
