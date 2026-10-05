---
id: ad8a-evaluate-expression-and-check-type-mismatch
type: entity
title: evaluate expression and check type mismatch
aliases:
- evaluate expression and check type mismatch
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ad8a-evaluate-expression-and-check-type-mismatch.md
  sha256: a0d8cb1c576de242dc9af87e90d34ff05a81263e77244d95ed76f2b9e7ed82f3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ad8a-evaluate-expression-and-check-type-mismatch
---

# evaluate expression and check type mismatch



# $AD8A — evaluate expression and check type mismatch

## Disassemblatura
```assembly
.AD8A  20 9E AD JSR $AD9E   ; evaluate expression check if source and destination are numeric
.AD8D  18       CLC
.AD8E  24       .BYTE $24   ; makes next line BIT $38 check if source and destination are string
.AD8F  38       SEC   ; destination is string type match check, set C for string, clear C for numeric
.AD90  24 0D    BIT $0D   ; test data type flag, $FF = string, $00 = numeric
.AD92  30 03    BMI $AD97   ; branch if string
.AD94  B0 03    BCS $AD99   ; if destination is numeric do type mismatch error
.AD96  60       RTS
.AD97  B0 FD    BCS $AD96   ; exit if destination is string do type mismatch error
.AD99  A2 16    LDX #$16   ; error code $16, type mismatch error
.AD9B  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$AD8A**: evaluate expression check if source and destination are numeric
- **$AD8E**: makes next line BIT $38 check if source and destination are string
- **$AD8F**: destination is string type match check, set C for string, clear C for numeric
- **$AD90**: test data type flag, $FF = string, $00 = numeric
- **$AD92**: branch if string
- **$AD94**: if destination is numeric do type mismatch error
- **$AD97**: exit if destination is string do type mismatch error
- **$AD99**: error code $16, type mismatch error
- **$AD9B**: do error #X then warm start

### Commodore-64-intern-Buch (Commodore)
- **$AD8A**: FRMEVL Term holen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ad8a-evaluate-expression-and-check-type-mismatch]]
