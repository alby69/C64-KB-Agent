---
title: times operator
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $BA2B
  address_end: $BA8B
  symbol: times-operator
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BA2B**: nicht null ?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BA2B**: FAC .NE. ZERO'
---

# $BA2B — times operator

## Disassemblatura
```assembly
.BA2B  D0 03    BNE $BA30
.BA2D  4C 8B BA JMP $BA8B
.BA30  20 B7 BA JSR $BAB7
.BA33  A9 00    LDA #$00
.BA35  85 26    STA $26
.BA37  85 27    STA $27
.BA39  85 28    STA $28
.BA3B  85 29    STA $29
.BA3D  A5 70    LDA $70
.BA3F  20 59 BA JSR $BA59
.BA42  A5 65    LDA $65
.BA44  20 59 BA JSR $BA59
.BA47  A5 64    LDA $64
.BA49  20 59 BA JSR $BA59
.BA4C  A5 63    LDA $63
.BA4E  20 59 BA JSR $BA59
.BA51  A5 62    LDA $62
.BA53  20 5E BA JSR $BA5E
.BA56  4C 8F BB JMP $BB8F
.BA59  D0 03    BNE $BA5E
.BA5B  4C 83 B9 JMP $B983
.BA5E  4A       LSR
.BA5F  09 80    ORA #$80
.BA61  A8       TAY
.BA62  90 19    BCC $BA7D
.BA64  18       CLC
.BA65  A5 29    LDA $29
.BA67  65 6D    ADC $6D
.BA69  85 29    STA $29
.BA6B  A5 28    LDA $28
.BA6D  65 6C    ADC $6C
.BA6F  85 28    STA $28
.BA71  A5 27    LDA $27
.BA73  65 6B    ADC $6B
.BA75  85 27    STA $27
.BA77  A5 26    LDA $26
.BA79  65 6A    ADC $6A
.BA7B  85 26    STA $26
.BA7D  66 26    ROR $26
.BA7F  66 27    ROR $27
.BA81  66 28    ROR $28
.BA83  66 29    ROR $29
.BA85  66 70    ROR $70
.BA87  98       TYA
.BA88  4A       LSR
.BA89  D0 D6    BNE $BA61
.BA8B  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$BA2B**: nicht null ?
- **$BA2D**: RTS
- **$BA30**: Exponent berechnen
- **$BA33**: Alle
- **$BA35**: Funktions-
- **$BA37**: register
- **$BA39**: lö-
- **$BA3B**: schen
- **$BA3D**: bitweise
- **$BA3F**: Multiplikation
- **$BA42**: bitweise
- **$BA44**: Multiplikation
- **$BA47**: bitweise
- **$BA49**: Multiplikation
- **$BA4C**: bitweise
- **$BA4E**: Multiplikation
- **$BA51**: bitweise
- **$BA53**: Multiplikation Register nach FAC, linksbündig machen
- **$BA56**: bitweise Multiplikation
- **$BA59**: Rechtsverschieben
- **$BA5B**: des Registers
- **$BA5E**: binäre Multiplikation
- **$BA5F**: des Akkus
- **$BA61**: mit ARG.
- **$BA62**: Das Ergebnis kommt
- **$BA64**: in das
- **$BA65**: Register für
- **$BA67**: Funktionen.
- **$BA69**: Bei gesetztem Bit
- **$BA6B**: im Akku
- **$BA6D**: wird ARG
- **$BA6F**: zum
- **$BA71**: Funktionsregister
- **$BA73**: addiert.
- **$BA75**: Zusätzlich
- **$BA77**: werden
- **$BA79**: die
- **$BA7B**: Funktionsregister
- **$BA7D**: noch
- **$BA7F**: verdoppelt.
- **$BA81**: Die Routine
- **$BA83**: arbeitet
- **$BA85**: im selben
- **$BA87**: Prinzip
- **$BA88**: wie
- **$BA89**: bei $B34C.
- **$BA8B**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BA2B**: FAC .NE. ZERO
- **$BA2D**: FAC = 0 * ARG = 0
- **$BA35**: INIT PRODUCT = 0

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*