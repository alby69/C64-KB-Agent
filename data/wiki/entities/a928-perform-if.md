---
id: a928-perform-if
type: entity
title: perform IF
aliases:
- perform IF
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a928-perform-if.md
  sha256: 3c7ebde8c47999f30f7203f257c0c7c7d389ae5555f36947c19c1699ce8f3940
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a928-perform-if
---

# perform IF



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

## References
- Source: [[src-a928-perform-if]]
