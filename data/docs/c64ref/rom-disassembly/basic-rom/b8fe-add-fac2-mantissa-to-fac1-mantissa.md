---
title: add FAC2 mantissa to FAC1 mantissa
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
- b8fe-add-mantissas-of-fac-and-arg-into-fac
- b91d-finish-normalizing-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $B8FE
  address_end: $B946
  symbol: add-fac2-mantissa-to-fac1-mantissa
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B8FE**: add FAC2 rounding byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $B8FE — add FAC2 mantissa to FAC1 mantissa

## Disassemblatura
```assembly
.B8FE  65 56    ADC $56   ; add FAC2 rounding byte
.B900  85 70    STA $70   ; save FAC1 rounding byte
.B902  A5 65    LDA $65   ; get FAC1 mantissa 4
.B904  65 6D    ADC $6D   ; add FAC2 mantissa 4
.B906  85 65    STA $65   ; save FAC1 mantissa 4
.B908  A5 64    LDA $64   ; get FAC1 mantissa 3
.B90A  65 6C    ADC $6C   ; add FAC2 mantissa 3
.B90C  85 64    STA $64   ; save FAC1 mantissa 3
.B90E  A5 63    LDA $63   ; get FAC1 mantissa 2
.B910  65 6B    ADC $6B   ; add FAC2 mantissa 2
.B912  85 63    STA $63   ; save FAC1 mantissa 2
.B914  A5 62    LDA $62   ; get FAC1 mantissa 1
.B916  65 6A    ADC $6A   ; add FAC2 mantissa 1
.B918  85 62    STA $62   ; save FAC1 mantissa 1
.B91A  4C 36 B9 JMP $B936   ; test and normalise FAC1 for C=0/1
.B91D  69 01    ADC #$01   ; add 1 to exponent offset
.B91F  06 70    ASL $70   ; shift FAC1 rounding byte
.B921  26 65    ROL $65   ; shift FAC1 mantissa 4
.B923  26 64    ROL $64   ; shift FAC1 mantissa 3
.B925  26 63    ROL $63   ; shift FAC1 mantissa 2
.B927  26 62    ROL $62   ; shift FAC1 mantissa 1 normalise FAC1
.B929  10 F2    BPL $B91D   ; loop if not normalised
.B92B  38       SEC   ; set carry for subtract
.B92C  E5 61    SBC $61   ; subtract FAC1 exponent
.B92E  B0 C7    BCS $B8F7   ; branch if underflow (set result = $0)
.B930  49 FF    EOR #$FF   ; complement exponent
.B932  69 01    ADC #$01   ; +1 (twos complement)
.B934  85 61    STA $61   ; save FAC1 exponent test and normalise FAC1 for C=0/1
.B936  90 0E    BCC $B946   ; exit if no overflow normalise FAC1 for C=1
.B938  E6 61    INC $61   ; increment FAC1 exponent
.B93A  F0 42    BEQ $B97E   ; if zero do overflow error then warm start
.B93C  66 62    ROR $62   ; shift FAC1 mantissa 1
.B93E  66 63    ROR $63   ; shift FAC1 mantissa 2
.B940  66 64    ROR $64   ; shift FAC1 mantissa 3
.B942  66 65    ROR $65   ; shift FAC1 mantissa 4
.B944  66 70    ROR $70   ; shift FAC1 rounding byte
.B946  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B8FE**: add FAC2 rounding byte
- **$B900**: save FAC1 rounding byte
- **$B902**: get FAC1 mantissa 4
- **$B904**: add FAC2 mantissa 4
- **$B906**: save FAC1 mantissa 4
- **$B908**: get FAC1 mantissa 3
- **$B90A**: add FAC2 mantissa 3
- **$B90C**: save FAC1 mantissa 3
- **$B90E**: get FAC1 mantissa 2
- **$B910**: add FAC2 mantissa 2
- **$B912**: save FAC1 mantissa 2
- **$B914**: get FAC1 mantissa 1
- **$B916**: add FAC2 mantissa 1
- **$B918**: save FAC1 mantissa 1
- **$B91A**: test and normalise FAC1 for C=0/1
- **$B91D**: add 1 to exponent offset
- **$B91F**: shift FAC1 rounding byte
- **$B921**: shift FAC1 mantissa 4
- **$B923**: shift FAC1 mantissa 3
- **$B925**: shift FAC1 mantissa 2
- **$B927**: shift FAC1 mantissa 1 normalise FAC1
- **$B929**: loop if not normalised
- **$B92B**: set carry for subtract
- **$B92C**: subtract FAC1 exponent
- **$B92E**: branch if underflow (set result = $0)
- **$B930**: complement exponent
- **$B932**: +1 (twos complement)
- **$B934**: save FAC1 exponent test and normalise FAC1 for C=0/1
- **$B936**: exit if no overflow normalise FAC1 for C=1
- **$B938**: increment FAC1 exponent
- **$B93A**: if zero do overflow error then warm start
- **$B93C**: shift FAC1 mantissa 1
- **$B93E**: shift FAC1 mantissa 2
- **$B940**: shift FAC1 mantissa 3
- **$B942**: shift FAC1 mantissa 4
- **$B944**: shift FAC1 rounding byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*