---
id: a642-perform-new
type: entity
title: perform NEW
aliases:
- perform NEW
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a642-perform-new.md
  sha256: 6b73323d61df8fd4c9a465349860e78add96c44e728694c0c4d647eec2084cfa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a642-perform-new
---

# perform NEW



# $A642 — perform NEW

## Disassemblatura
```assembly
.A642  D0 FD    BNE $A641   ; exit if following byte to allow syntax error
.A644  A9 00    LDA #$00   ; clear A
.A646  A8       TAY   ; clear index
.A647  91 2B    STA ($2B),Y   ; clear pointer to next line low byte
.A649  C8       INY   ; increment index
.A64A  91 2B    STA ($2B),Y   ; clear pointer to next line high byte, erase program
.A64C  A5 2B    LDA $2B   ; get start of memory low byte
.A64E  18       CLC   ; clear carry for add
.A64F  69 02    ADC #$02   ; add null program length
.A651  85 2D    STA $2D   ; set start of variables low byte
.A653  A5 2C    LDA $2C   ; get start of memory high byte
.A655  69 00    ADC #$00   ; add carry
.A657  85 2E    STA $2E   ; set start of variables high byte
```


## Commenti

### Original Disassembly (—)
- **$A642**: exit if following byte to allow syntax error
- **$A644**: clear A
- **$A646**: clear index
- **$A647**: clear pointer to next line low byte
- **$A649**: increment index
- **$A64A**: clear pointer to next line high byte, erase program
- **$A64C**: get start of memory low byte
- **$A64E**: clear carry for add
- **$A64F**: add null program length
- **$A651**: set start of variables low byte
- **$A653**: get start of memory high byte
- **$A655**: add carry
- **$A657**: set start of variables high byte

### Commodore-64-intern-Buch (Commodore)
- **$A642**: Kein Trennzeichen: SYNTAX ERROR
- **$A644**: Nullcode laden
- **$A646**: und als Zähler ins Y-Reg.
- **$A647**: Nullcode an Programmanfang
- **$A649**: Zähler erhöhen
- **$A64A**: noch einen Nullcode dahinter
- **$A64C**: Zeiger auf Programmst. (LOW)
- **$A64E**: Carry löschen
- **$A64F**: Programmstart + 2 ergibt
- **$A651**: neuen Variablenstart (LOW)
- **$A653**: Zeiger auf Programmst. (HIGH)
- **$A655**: + Übertrag ergibt neuen
- **$A657**: Variablenstart (HIGH)
- **$A659**: CHRGET, Routine neu setzen
- **$A65C**: Zero-Flag für CLR = 1 setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A642**: IGNORE IF MORE TO THE STATEMENT
- **$A659**: SET TXTPTR TO TXTTAB - 1
- **$A65C**: (THIS COULD HAVE BEEN ".HS 2C")

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a642-perform-new]]
