---
id: b999-main-entry-to-right-shift-subroutine
type: entity
title: MAIN ENTRY TO RIGHT SHIFT SUBROUTINE
aliases:
- MAIN ENTRY TO RIGHT SHIFT SUBROUTINE
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b999-main-entry-to-right-shift-subroutine.md
  sha256: a1d8a0b243ab1c38faecabe03bf9543d005ff6dfd86ad1dc3a187b539a55e381
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b999-main-entry-to-right-shift-subroutine
---

# MAIN ENTRY TO RIGHT SHIFT SUBROUTINE



# $B999 — MAIN ENTRY TO RIGHT SHIFT SUBROUTINE

## Disassemblatura
```assembly
.B999  69 08    ADC #$08
.B99B  30 E8    BMI $B985   ; STILL MORE THAN 8 BITS TO GO
.B99D  F0 E6    BEQ $B985   ; EXACTLY 8 MORE BITS TO GO
.B99F  E9 08    SBC #$08   ; UNDO ADC ABOVE
.B9A1  A8       TAY   ; REMAINING SHIFT COUNT
.B9A2  A5 70    LDA $70
.B9A4  B0 14    BCS $B9BA   ; FINISHED SHIFTING
.B9A6  16 01    ASL $01,X   ; SIGN -> CARRY (SIGN EXTENSION)
.B9A8  90 02    BCC $B9AC   ; SIGN +
.B9AA  F6 01    INC $01,X   ; PUT SIGN IN LSB
.B9AC  76 01    ROR $01,X   ; RESTORE VALUE, SIGN STILL IN CARRY
.B9AE  76 01    ROR $01,X   ; START RIGHT SHIFT, INSERTING SIGN
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B99B**: STILL MORE THAN 8 BITS TO GO
- **$B99D**: EXACTLY 8 MORE BITS TO GO
- **$B99F**: UNDO ADC ABOVE
- **$B9A1**: REMAINING SHIFT COUNT
- **$B9A4**: FINISHED SHIFTING
- **$B9A6**: SIGN -> CARRY (SIGN EXTENSION)
- **$B9A8**: SIGN +
- **$B9AA**: PUT SIGN IN LSB
- **$B9AC**: RESTORE VALUE, SIGN STILL IN CARRY
- **$B9AE**: START RIGHT SHIFT, INSERTING SIGN

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b999-main-entry-to-right-shift-subroutine]]
