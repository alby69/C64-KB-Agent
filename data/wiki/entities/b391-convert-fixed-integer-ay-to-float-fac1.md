---
id: b391-convert-fixed-integer-ay-to-float-fac1
type: entity
title: convert fixed integer AY to float FAC1
aliases:
- convert fixed integer AY to float FAC1
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b391-convert-fixed-integer-ay-to-float-fac1.md
  sha256: 748eafdf12a6bc2d26c841054b2c7c8b851b75dfa5ebf371ec2ed4c4ebb1b083
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b391-convert-fixed-integer-ay-to-float-fac1
---

# convert fixed integer AY to float FAC1



# $B391 — convert fixed integer AY to float FAC1

## Disassemblatura
```assembly
.B391  A2 00    LDX #$00   ; set type = numeric
.B393  86 0D    STX $0D   ; clear data type flag, $FF = string, $00 = numeric
.B395  85 62    STA $62   ; save FAC1 mantissa 1
.B397  84 63    STY $63   ; save FAC1 mantissa 2
.B399  A2 90    LDX #$90   ; set exponent=2^16 (integer)
.B39B  4C 44 BC JMP $BC44   ; set exp = X, clear FAC1 3 and 4, normalise and return
```


## Commenti

### Original Disassembly (—)
- **$B391**: set type = numeric
- **$B393**: clear data type flag, $FF = string, $00 = numeric
- **$B395**: save FAC1 mantissa 1
- **$B397**: save FAC1 mantissa 2
- **$B399**: set exponent=2^16 (integer)
- **$B39B**: set exp = X, clear FAC1 3 and 4, normalise and return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B391**: MARK FAC VALUE TYPE REAL
- **$B395**: SAVE VALUE FROM A,Y IN MANTISSA
- **$B399**: SET EXPONENT TO 2^16
- **$B39B**: CONVERT TO SIGNED FP

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b391-convert-fixed-integer-ay-to-float-fac1]]
