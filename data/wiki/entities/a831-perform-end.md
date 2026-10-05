---
id: a831-perform-end
type: entity
title: perform END
aliases:
- perform END
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a831-perform-end.md
  sha256: 330ed03b065f46435df0d61b6b9acb37c3a78b5eb9906d8db65321abf0bc09f9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a831-perform-end
---

# perform END



# $A831 — perform END

## Disassemblatura
```assembly
.A831  18       CLC   ; clear carry
.A832  D0 3C    BNE $A870   ; return if wasn't CTRL-C
.A834  A5 7A    LDA $7A   ; get BASIC execute pointer low byte
.A836  A4 7B    LDY $7B   ; get BASIC execute pointer high byte
.A838  A6 3A    LDX $3A   ; get current line number high byte
.A83A  E8       INX   ; increment it
.A83B  F0 0C    BEQ $A849   ; branch if was immediate mode
.A83D  85 3D    STA $3D   ; save continue pointer low byte
.A83F  84 3E    STY $3E   ; save continue pointer high byte
.A841  A5 39    LDA $39   ; get current line number low byte
.A843  A4 3A    LDY $3A   ; get current line number high byte
.A845  85 3B    STA $3B   ; save break line number low byte
.A847  84 3C    STY $3C   ; save break line number high byte
.A849  68       PLA   ; dump return address low byte
.A84A  68       PLA   ; dump return address high byte
.A84B  A9 81    LDA #$81   ; set [CR][LF]"BREAK" pointer low byte
.A84D  A0 A3    LDY #$A3   ; set [CR][LF]"BREAK" pointer high byte
.A84F  90 03    BCC $A854   ; if was program end skip the print string
.A851  4C 69 A4 JMP $A469   ; print string and do warm start
.A854  4C 86 E3 JMP $E386   ; do warm start
```


## Commenti

### Original Disassembly (—)
- **$A831**: clear carry
- **$A832**: return if wasn't CTRL-C
- **$A834**: get BASIC execute pointer low byte
- **$A836**: get BASIC execute pointer high byte
- **$A838**: get current line number high byte
- **$A83A**: increment it
- **$A83B**: branch if was immediate mode
- **$A83D**: save continue pointer low byte
- **$A83F**: save continue pointer high byte
- **$A841**: get current line number low byte
- **$A843**: get current line number high byte
- **$A845**: save break line number low byte
- **$A847**: save break line number high byte
- **$A849**: dump return address low byte
- **$A84A**: dump return address high byte
- **$A84B**: set [CR][LF]"BREAK" pointer low byte
- **$A84D**: set [CR][LF]"BREAK" pointer high byte
- **$A84F**: if was program end skip the print string
- **$A851**: print string and do warm start
- **$A854**: do warm start

### Commodore-64-intern-Buch (Commodore)
- **$A831**: C=0 Flag für END
- **$A832**: RUN/STOP nicht gedrückt: RTS
- **$A834**: Programmzeiger laden
- **$A836**: (LOW und HIGH-Byte)
- **$A838**: Direkt-Modus?
- **$A83A**: (Zeilennummer -1)
- **$A83B**: ja: $A849
- **$A83D**: als Zeiger für CONT setzen
- **$A83F**: (LOW und HIGH)
- **$A841**: Nummer der laufenden Zeile
- **$A843**: holen (LOW und HIGH)
- **$A845**: und als Zeilennummer für
- **$A847**: CONT merken
- **$A849**: Rücksprungadresse
- **$A84A**: vom Stapel entfernen
- **$A84B**: Zeiger auf Startadresse
- **$A84D**: BREAK setzen
- **$A84F**: END Flag?
- **$A851**: nein: 'BREAK IN XXX' ausgeben
- **$A854**: zum BASIC-Warmstart

### Marko Mäkelä (Marko Mäkelä)
- **$A84B**: low  A381
- **$A84D**: high A381

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A831**: CARRY=0 TO AVOID PRINTING MESSAGE
- **$A832**: IF NOT END OF STATEMENT, DO NOTHING
- **$A83A**: RUNNING?
- **$A83B**: NO, DIRECT MODE
- **$A84B**: " BREAK" AND BELL

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a831-perform-end]]
