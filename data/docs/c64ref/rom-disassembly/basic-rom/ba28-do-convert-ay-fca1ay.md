---
title: do convert AY, FCA1*(AY)
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
- ba28-konstante-ay-fac
- ba2b-fac
- ba59-multiply-arg-by-a-into-result
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BA28
  address_end: $BA8B
  symbol: do-convert-ay-fca1ay
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BA28**: unpack memory (AY) into FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BA28**: Konstante nach ARG'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $BA28 — do convert AY, FCA1*(AY)

## Disassemblatura
```assembly
.BA28  20 8C BA JSR $BA8C   ; unpack memory (AY) into FAC2
.BA2B  D0 03    BNE $BA30   ; multiply FAC1 by FAC2 ??
.BA2D  4C 8B BA JMP $BA8B   ; exit if zero
.BA30  20 B7 BA JSR $BAB7   ; test and adjust accumulators
.BA33  A9 00    LDA #$00   ; clear A
.BA35  85 26    STA $26   ; clear temp mantissa 1
.BA37  85 27    STA $27   ; clear temp mantissa 2
.BA39  85 28    STA $28   ; clear temp mantissa 3
.BA3B  85 29    STA $29   ; clear temp mantissa 4
.BA3D  A5 70    LDA $70   ; get FAC1 rounding byte
.BA3F  20 59 BA JSR $BA59   ; go do shift/add FAC2
.BA42  A5 65    LDA $65   ; get FAC1 mantissa 4
.BA44  20 59 BA JSR $BA59   ; go do shift/add FAC2
.BA47  A5 64    LDA $64   ; get FAC1 mantissa 3
.BA49  20 59 BA JSR $BA59   ; go do shift/add FAC2
.BA4C  A5 63    LDA $63   ; get FAC1 mantissa 2
.BA4E  20 59 BA JSR $BA59   ; go do shift/add FAC2
.BA51  A5 62    LDA $62   ; get FAC1 mantissa 1
.BA53  20 5E BA JSR $BA5E   ; go do shift/add FAC2
.BA56  4C 8F BB JMP $BB8F   ; copy temp to FAC1, normalise and return
.BA59  D0 03    BNE $BA5E   ; branch if byte <> zero
.BA5B  4C 83 B9 JMP $B983   ; shift FCAtemp << A+8 times else do shift and add
.BA5E  4A       LSR   ; shift byte
.BA5F  09 80    ORA #$80   ; set top bit (mark for 8 times)
.BA61  A8       TAY   ; copy result
.BA62  90 19    BCC $BA7D   ; skip next if bit was zero
.BA64  18       CLC   ; clear carry for add
.BA65  A5 29    LDA $29   ; get temp mantissa 4
.BA67  65 6D    ADC $6D   ; add FAC2 mantissa 4
.BA69  85 29    STA $29   ; save temp mantissa 4
.BA6B  A5 28    LDA $28   ; get temp mantissa 3
.BA6D  65 6C    ADC $6C   ; add FAC2 mantissa 3
.BA6F  85 28    STA $28   ; save temp mantissa 3
.BA71  A5 27    LDA $27   ; get temp mantissa 2
.BA73  65 6B    ADC $6B   ; add FAC2 mantissa 2
.BA75  85 27    STA $27   ; save temp mantissa 2
.BA77  A5 26    LDA $26   ; get temp mantissa 1
.BA79  65 6A    ADC $6A   ; add FAC2 mantissa 1
.BA7B  85 26    STA $26   ; save temp mantissa 1
.BA7D  66 26    ROR $26   ; shift temp mantissa 1
.BA7F  66 27    ROR $27   ; shift temp mantissa 2
.BA81  66 28    ROR $28   ; shift temp mantissa 3
.BA83  66 29    ROR $29   ; shift temp mantissa 4
.BA85  66 70    ROR $70   ; shift temp rounding byte
.BA87  98       TYA   ; get byte back
.BA88  4A       LSR   ; shift byte
.BA89  D0 D6    BNE $BA61   ; loop if all bits not done
.BA8B  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BA28**: unpack memory (AY) into FAC2
- **$BA2B**: multiply FAC1 by FAC2 ??
- **$BA2D**: exit if zero
- **$BA30**: test and adjust accumulators
- **$BA33**: clear A
- **$BA35**: clear temp mantissa 1
- **$BA37**: clear temp mantissa 2
- **$BA39**: clear temp mantissa 3
- **$BA3B**: clear temp mantissa 4
- **$BA3D**: get FAC1 rounding byte
- **$BA3F**: go do shift/add FAC2
- **$BA42**: get FAC1 mantissa 4
- **$BA44**: go do shift/add FAC2
- **$BA47**: get FAC1 mantissa 3
- **$BA49**: go do shift/add FAC2
- **$BA4C**: get FAC1 mantissa 2
- **$BA4E**: go do shift/add FAC2
- **$BA51**: get FAC1 mantissa 1
- **$BA53**: go do shift/add FAC2
- **$BA56**: copy temp to FAC1, normalise and return
- **$BA59**: branch if byte <> zero
- **$BA5B**: shift FCAtemp << A+8 times else do shift and add
- **$BA5E**: shift byte
- **$BA5F**: set top bit (mark for 8 times)
- **$BA61**: copy result
- **$BA62**: skip next if bit was zero
- **$BA64**: clear carry for add
- **$BA65**: get temp mantissa 4
- **$BA67**: add FAC2 mantissa 4
- **$BA69**: save temp mantissa 4
- **$BA6B**: get temp mantissa 3
- **$BA6D**: add FAC2 mantissa 3
- **$BA6F**: save temp mantissa 3
- **$BA71**: get temp mantissa 2
- **$BA73**: add FAC2 mantissa 2
- **$BA75**: save temp mantissa 2
- **$BA77**: get temp mantissa 1
- **$BA79**: add FAC2 mantissa 1
- **$BA7B**: save temp mantissa 1
- **$BA7D**: shift temp mantissa 1
- **$BA7F**: shift temp mantissa 2
- **$BA81**: shift temp mantissa 3
- **$BA83**: shift temp mantissa 4
- **$BA85**: shift temp rounding byte
- **$BA87**: get byte back
- **$BA88**: shift byte
- **$BA89**: loop if all bits not done

### Commodore-64-intern-Buch (Commodore)
- **$BA28**: Konstante nach ARG

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*