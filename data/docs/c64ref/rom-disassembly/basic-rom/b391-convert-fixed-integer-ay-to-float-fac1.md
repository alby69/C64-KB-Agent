---
title: convert fixed integer AY to float FAC1
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
- b391-float-the-signed-integer-in-ay
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $B391
  address_end: $B39B
  symbol: convert-fixed-integer-ay-to-float-fac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B391**: set type = numeric'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B391**: MARK FAC VALUE TYPE REAL'
---

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