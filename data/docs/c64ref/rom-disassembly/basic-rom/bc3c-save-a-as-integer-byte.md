---
title: save A as integer byte
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
- bc3c-convert-a-into-fac-as-signed-value-128-to-127
- bc44-float-unsigned-value-in-fac12
- bc49-float-unsigned-value-in-fac12
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $BC3C
  address_end: $BC55
  symbol: save-a-as-integer-byte
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC3C**: save FAC1 mantissa 1'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC3C**: PUT IN HIGH BYTE OF MANTISSA'
---

# $BC3C — save A as integer byte

## Disassemblatura
```assembly
.BC3C  85 62    STA $62   ; save FAC1 mantissa 1
.BC3E  A9 00    LDA #$00   ; clear A
.BC40  85 63    STA $63   ; clear FAC1 mantissa 2
.BC42  A2 88    LDX #$88   ; set exponent set exponent = X, clear FAC1 3 and 4 and normalise
.BC44  A5 62    LDA $62   ; get FAC1 mantissa 1
.BC46  49 FF    EOR #$FF   ; complement it
.BC48  2A       ROL   ; sign bit into carry set exponent = X, clear mantissa 4 and 3 and normalise FAC1
.BC49  A9 00    LDA #$00   ; clear A
.BC4B  85 65    STA $65   ; clear FAC1 mantissa 4
.BC4D  85 64    STA $64   ; clear FAC1 mantissa 3 set exponent = X and normalise FAC1
.BC4F  86 61    STX $61   ; set FAC1 exponent
.BC51  85 70    STA $70   ; clear FAC1 rounding byte
.BC53  85 66    STA $66   ; clear FAC1 sign (b7)
.BC55  4C D2 B8 JMP $B8D2   ; do ABS and normalise FAC1
```


## Commenti

### Original Disassembly (—)
- **$BC3C**: save FAC1 mantissa 1
- **$BC3E**: clear A
- **$BC40**: clear FAC1 mantissa 2
- **$BC42**: set exponent set exponent = X, clear FAC1 3 and 4 and normalise
- **$BC44**: get FAC1 mantissa 1
- **$BC46**: complement it
- **$BC48**: sign bit into carry set exponent = X, clear mantissa 4 and 3 and normalise FAC1
- **$BC49**: clear A
- **$BC4B**: clear FAC1 mantissa 4
- **$BC4D**: clear FAC1 mantissa 3 set exponent = X and normalise FAC1
- **$BC4F**: set FAC1 exponent
- **$BC51**: clear FAC1 rounding byte
- **$BC53**: clear FAC1 sign (b7)
- **$BC55**: do ABS and normalise FAC1

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC3C**: PUT IN HIGH BYTE OF MANTISSA
- **$BC3E**: CLEAR 2ND BYTE OF MANTISSA
- **$BC42**: USE EXPONENT 2^9

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*