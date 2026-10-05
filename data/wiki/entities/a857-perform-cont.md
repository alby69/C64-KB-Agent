---
id: a857-perform-cont
type: entity
title: perform CONT
aliases:
- perform CONT
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a857-perform-cont.md
  sha256: 1b23438e55529729b14c315d744366be614753ae1b0346ddaa0b9f0ec5a5e7a4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a857-perform-cont
---

# perform CONT



# $A857 — perform CONT

## Disassemblatura
```assembly
.A857  D0 17    BNE $A870   ; exit if following byte to allow syntax error
.A859  A2 1A    LDX #$1A   ; error code $1A, can't continue error
.A85B  A4 3E    LDY $3E   ; get continue pointer high byte
.A85D  D0 03    BNE $A862   ; go do continue if we can
.A85F  4C 37 A4 JMP $A437   ; else do error #X then warm start we can continue so ...
.A862  A5 3D    LDA $3D   ; get continue pointer low byte
.A864  85 7A    STA $7A   ; save BASIC execute pointer low byte
.A866  84 7B    STY $7B   ; save BASIC execute pointer high byte
.A868  A5 3B    LDA $3B   ; get break line low byte
.A86A  A4 3C    LDY $3C   ; get break line high byte
.A86C  85 39    STA $39   ; set current line number low byte
.A86E  84 3A    STY $3A   ; set current line number high byte
.A870  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A857**: exit if following byte to allow syntax error
- **$A859**: error code $1A, can't continue error
- **$A85B**: get continue pointer high byte
- **$A85D**: go do continue if we can
- **$A85F**: else do error #X then warm start we can continue so ...
- **$A862**: get continue pointer low byte
- **$A864**: save BASIC execute pointer low byte
- **$A866**: save BASIC execute pointer high byte
- **$A868**: get break line low byte
- **$A86A**: get break line high byte
- **$A86C**: set current line number low byte
- **$A86E**: set current line number high byte

### Commodore-64-intern-Buch (Commodore)
- **$A857**: Kein Trennzeichen: SYNTAX ERR
- **$A859**: Fehlernr. für 'CAN'T CONTINUE
- **$A85B**: CONT gesperrt?
- **$A85D**: nein: $A862
- **$A85F**: Fehlermeldung ausgeben
- **$A862**: CONT-Zeiger (LOW) laden
- **$A864**: und CONT-Zeiger als Programm-
- **$A866**: zeiger abspeichern
- **$A868**: und
- **$A86A**: Zeilennummer wieder
- **$A86C**: setzen
- **$A86E**: (LOW- und HIGH-Byte)
- **$A870**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$A859**: error number

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A857**: IF NOT END OF STATEMENT, DO NOTHING
- **$A85B**: MEANINGFUL RE-ENTRY?
- **$A85D**: YES
- **$A85F**: NO
- **$A862**: RESTORE TXTPTR
- **$A868**: RESTORE LINE NUMBER

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a857-perform-cont]]
