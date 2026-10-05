---
id: a93b-perform-rem
type: entity
title: perform REM
aliases:
- perform REM
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a93b-perform-rem.md
  sha256: 755dbacc3caa92e5890d1139a0b0ba75923ef3fc74866e0d065de126371c8e7f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a93b-perform-rem
---

# perform REM



# $A93B — perform REM

## Disassemblatura
```assembly
.A93B  20 09 A9 JSR $A909   ; scan for next BASIC line
.A93E  F0 BB    BEQ $A8FB   ; add Y to the BASIC execute pointer and return, branch always result was non zero so do rest of line
.A940  20 79 00 JSR $0079   ; scan memory
.A943  B0 03    BCS $A948   ; branch if not numeric character, is variable or keyword
.A945  4C A0 A8 JMP $A8A0   ; else perform GOTO n is variable or keyword
.A948  4C ED A7 JMP $A7ED   ; interpret BASIC code from BASIC execute pointer
```


## Commenti

### Original Disassembly (—)
- **$A93B**: scan for next BASIC line
- **$A93E**: add Y to the BASIC execute pointer and return, branch always result was non zero so do rest of line
- **$A940**: scan memory
- **$A943**: branch if not numeric character, is variable or keyword
- **$A945**: else perform GOTO n is variable or keyword
- **$A948**: interpret BASIC code from BASIC execute pointer

### Commodore-64-intern-Buch (Commodore)
- **$A93B**: nein, Zeilenanfang suchen
- **$A93E**: Programmz. auf nächste Zeile
- **$A940**: CHRGOT: letztes Zeichen holen
- **$A943**: keine Ziffer?
- **$A945**: zum GOTO-Befehl
- **$A948**: Befehl dekodieren, ausführen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A93B**: SKIP REST OF LINE
- **$A93E**: ...ALWAYS
- **$A940**: COMMAND OR NUMBER?
- **$A943**: COMMAND
- **$A945**: NUMBER

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a93b-perform-rem]]
