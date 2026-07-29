---
title: perform IF
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
- a928-basic-befehl-if
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A928
  address_end: $A939
  symbol: perform-if
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A928**: evaluate expression'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A928**: FRMEVL Ausdruck berechnen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A937**: CONDITION TRUE OR FALSE?'
---

# $A928 — perform IF

## Disassemblatura
```assembly
.A928  20 9E AD JSR $AD9E   ; evaluate expression
.A92B  20 79 00 JSR $0079   ; scan memory
.A92E  C9 89    CMP #$89   ; compare with "GOTO" token
.A930  F0 05    BEQ $A937   ; if it was  the token for GOTO go do IF ... GOTO wasn't IF ... GOTO so must be IF ... THEN
.A932  A9 A7    LDA #$A7   ; set "THEN" token
.A934  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.A937  A5 61    LDA $61   ; get FAC1 exponent
.A939  D0 05    BNE $A940   ; if result was non zero continue execution else REM rest of line
```


## Commenti

### Original Disassembly (—)
- **$A928**: evaluate expression
- **$A92B**: scan memory
- **$A92E**: compare with "GOTO" token
- **$A930**: if it was  the token for GOTO go do IF ... GOTO wasn't IF ... GOTO so must be IF ... THEN
- **$A932**: set "THEN" token
- **$A934**: scan for CHR$(A), else do syntax error then warm start
- **$A937**: get FAC1 exponent
- **$A939**: if result was non zero continue execution else REM rest of line

### Commodore-64-intern-Buch (Commodore)
- **$A928**: FRMEVL Ausdruck berechnen
- **$A92B**: CHRGOT letztes Zeichen
- **$A92E**: 'GOTO'-Code?
- **$A930**: ja: $A937
- **$A932**: 'THEN'-Code
- **$A934**: prüft auf Code
- **$A937**: Ergebnis des IF-Ausdrucks
- **$A939**: Ausdruck wahr?

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A937**: CONDITION TRUE OR FALSE?
- **$A939**: BRANCH IF TRUE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*