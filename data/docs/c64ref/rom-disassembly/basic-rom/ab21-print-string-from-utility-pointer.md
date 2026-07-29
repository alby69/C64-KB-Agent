---
title: print string from utility pointer
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
- ab21-print-string-at-facmofaclo
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $AB21
  address_end: $AB38
  symbol: print-string-from-utility-pointer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AB21**: pop string off descriptor stack, or from top of string
      space ret...'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AB21**: GET ADDRESS INTO INDEX, (A)=LENGTH'
---

# $AB21 — print string from utility pointer

## Disassemblatura
```assembly
.AB21  20 A6 B6 JSR $B6A6   ; pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
.AB24  AA       TAX   ; copy length
.AB25  A0 00    LDY #$00   ; clear index
.AB27  E8       INX   ; increment length, for pre decrement loop
.AB28  CA       DEX   ; decrement length
.AB29  F0 BC    BEQ $AAE7   ; exit if done
.AB2B  B1 22    LDA ($22),Y   ; get byte from string
.AB2D  20 47 AB JSR $AB47   ; print the character
.AB30  C8       INY   ; increment index
.AB31  C9 0D    CMP #$0D   ; compare byte with [CR]
.AB33  D0 F3    BNE $AB28   ; loop if not [CR]
.AB35  20 E5 AA JSR $AAE5   ; toggle A, EOR #$FF. what is the point of this ??
.AB38  4C 28 AB JMP $AB28   ; loop
```


## Commenti

### Original Disassembly (—)
- **$AB21**: pop string off descriptor stack, or from top of string space returns with A = length, X = pointer low byte, Y = pointer high byte
- **$AB24**: copy length
- **$AB25**: clear index
- **$AB27**: increment length, for pre decrement loop
- **$AB28**: decrement length
- **$AB29**: exit if done
- **$AB2B**: get byte from string
- **$AB2D**: print the character
- **$AB30**: increment index
- **$AB31**: compare byte with [CR]
- **$AB33**: loop if not [CR]
- **$AB35**: toggle A, EOR #$FF. what is the point of this ??
- **$AB38**: loop

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AB21**: GET ADDRESS INTO INDEX, (A)=LENGTH
- **$AB24**: USE X-REG FOR COUNTER
- **$AB25**: USE Y-REG FOR SCANNER
- **$AB29**: FINISHED
- **$AB2B**: NEXT CHAR FROM STRING
- **$AB2D**: PRINT THE CHAR
- **$AB30**: <<< NEXT THREE LINES ARE USELESS >>>
- **$AB31**: WAS IT <RETURN>?
- **$AB33**: NO
- **$AB35**: EOR #$FF WOULD DO IT, BUT WHY? <<< ABOVE THREE LINES ARE USELESS >>>
- **$AB3F**: PRINT A SPACE
- **$AB41**: SKIP OVER NEXT LINE
- **$AB44**: SKIP OVER NEXT LINE
- **$AB45**: PRINT QUESTION MARK

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*