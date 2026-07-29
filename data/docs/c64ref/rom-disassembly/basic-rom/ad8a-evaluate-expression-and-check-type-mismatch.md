---
title: evaluate expression and check type mismatch
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ad8a-auf-numerisch-prfen
- ad8f-prft-auf-string
- ad90-make-sure-fac-is-correct-type
- bit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AD8A
  address_end: $AD9B
  symbol: evaluate-expression-and-check-type-mismatch
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AD8A**: evaluate expression check if source and destination
      are numeric'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AD8A**: FRMEVL Term holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

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