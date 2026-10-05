---
id: ae58-do-functions
type: entity
title: do functions
aliases:
- do functions
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae58-do-functions.md
  sha256: 1e4066f2eea1cad4b498fa1921bfcbf360244680679073ae0d5eb9eb6a9ddac4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ae58-do-functions
---

# do functions



# $AE58 — do functions

## Disassemblatura
```assembly
.AE58  A0 FF    LDY #$FF   ; flag function
.AE5A  68       PLA   ; pull precedence byte
.AE5B  F0 23    BEQ $AE80   ; exit if done
.AE5D  C9 64    CMP #$64   ; compare previous precedence with $64
.AE5F  F0 03    BEQ $AE64   ; branch if was $64 (< function)
.AE61  20 8D AD JSR $AD8D   ; check if source is numeric, else do type mismatch
.AE64  84 4B    STY $4B   ; save precedence stacked flag pop FAC2 and return
.AE66  68       PLA   ; pop byte
.AE67  4A       LSR   ; shift out comparison evaluation lowest bit
.AE68  85 12    STA $12   ; save the comparison evaluation flag
.AE6A  68       PLA   ; pop exponent
.AE6B  85 69    STA $69   ; save FAC2 exponent
.AE6D  68       PLA   ; pop mantissa 1
.AE6E  85 6A    STA $6A   ; save FAC2 mantissa 1
.AE70  68       PLA   ; pop mantissa 2
.AE71  85 6B    STA $6B   ; save FAC2 mantissa 2
.AE73  68       PLA   ; pop mantissa 3
.AE74  85 6C    STA $6C   ; save FAC2 mantissa 3
.AE76  68       PLA   ; pop mantissa 4
.AE77  85 6D    STA $6D   ; save FAC2 mantissa 4
.AE79  68       PLA   ; pop sign
.AE7A  85 6E    STA $6E   ; save FAC2 sign (b7)
.AE7C  45 66    EOR $66   ; EOR FAC1 sign (b7)
.AE7E  85 6F    STA $6F   ; save sign compare (FAC1 EOR FAC2)
.AE80  A5 61    LDA $61   ; get FAC1 exponent
.AE82  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AE58**: flag function
- **$AE5A**: pull precedence byte
- **$AE5B**: exit if done
- **$AE5D**: compare previous precedence with $64
- **$AE5F**: branch if was $64 (< function)
- **$AE61**: check if source is numeric, else do type mismatch
- **$AE64**: save precedence stacked flag pop FAC2 and return
- **$AE66**: pop byte
- **$AE67**: shift out comparison evaluation lowest bit
- **$AE68**: save the comparison evaluation flag
- **$AE6A**: pop exponent
- **$AE6B**: save FAC2 exponent
- **$AE6D**: pop mantissa 1
- **$AE6E**: save FAC2 mantissa 1
- **$AE70**: pop mantissa 2
- **$AE71**: save FAC2 mantissa 2
- **$AE73**: pop mantissa 3
- **$AE74**: save FAC2 mantissa 3
- **$AE76**: pop mantissa 4
- **$AE77**: save FAC2 mantissa 4
- **$AE79**: pop sign
- **$AE7A**: save FAC2 sign (b7)
- **$AE7C**: EOR FAC1 sign (b7)
- **$AE7E**: save sign compare (FAC1 EOR FAC2)
- **$AE80**: get FAC1 exponent

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ae58-do-functions]]
