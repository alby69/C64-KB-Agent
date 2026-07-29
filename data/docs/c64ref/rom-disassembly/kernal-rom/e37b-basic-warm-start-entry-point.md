---
title: BASIC warm start entry point
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e37b-basic-nmi-einsprung
- e38b-handle-error-messages
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E37B
  address_end: $E391
  symbol: basic-warm-start-entry-point
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E37B**: close input and output channels'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E37B**: CLRCH'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$E388**: normally E38B'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E37B**: CLRCHN, close all I/O channels'
---

# $E37B — BASIC warm start entry point

## Disassemblatura
```assembly
.E37B  20 CC FF JSR $FFCC   ; close input and output channels
.E37E  A9 00    LDA #$00   ; clear A
.E380  85 13    STA $13   ; set current I/O channel, flag default
.E382  20 7A A6 JSR $A67A   ; flush BASIC stack and clear continue pointer
.E385  58       CLI   ; enable the interrupts
.E386  A2 80    LDX #$80   ; set -ve error, just do warm start
.E388  6C 00 03 JMP ($0300)   ; go handle error message, normally $E38B
.E38B  8A       TXA   ; copy the error number
.E38C  30 03    BMI $E391   ; if -ve go do warm start
.E38E  4C 3A A4 JMP $A43A   ; else do error #X then warm start
.E391  4C 74 A4 JMP $A474   ; do warm start
```


## Commenti

### Original Disassembly (—)
- **$E37B**: close input and output channels
- **$E37E**: clear A
- **$E380**: set current I/O channel, flag default
- **$E382**: flush BASIC stack and clear continue pointer
- **$E385**: enable the interrupts
- **$E386**: set -ve error, just do warm start
- **$E388**: go handle error message, normally $E38B
- **$E38B**: copy the error number
- **$E38C**: if -ve go do warm start
- **$E38E**: else do error #X then warm start
- **$E391**: do warm start

### Commodore-64-intern-Buch (Commodore)
- **$E37B**: CLRCH
- **$E37E**: Eingabegerät gleich
- **$E380**: Tastatur
- **$E382**: BASIC initialisieren
- **$E385**: Interrupt freigeben
- **$E386**: Flag für kein Fehler
- **$E388**: BASIC Warmstart Vektor JMP $E38B
- **$E38B**: Fehlernummer in Akku
- **$E38C**: kein Fehler, dann 'ready.'
- **$E38E**: Fehlermeldung ausgeben
- **$E391**: Ready - Modus

### Marko Mäkelä (Marko Mäkelä)
- **$E388**: normally E38B

### Magnus Nyman (Magnus Nyman)
- **$E37B**: CLRCHN, close all I/O channels
- **$E380**: input prompt flag
- **$E382**: do CLR
- **$E385**: enable IRQ
- **$E386**: error code #$80
- **$E388**: perform error
- **$E38B**: error number
- **$E38C**: larger than $80
- **$E38E**: nope, print error
- **$E391**: print READY

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*