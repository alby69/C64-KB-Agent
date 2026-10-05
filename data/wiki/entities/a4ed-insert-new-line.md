---
id: a4ed-insert-new-line
type: entity
title: insert new line
aliases:
- insert new line
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a4ed-insert-new-line.md
  sha256: 344c9fe224bae3bc382c74580b534c1e127fe86e94f8452cf127db247b9bd89c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a4ed-insert-new-line
---

# insert new line



# $A4ED — insert new line

## Disassemblatura
```assembly
.A4ED  20 59 A6 JSR $A659
.A4F0  20 33 A5 JSR $A533
.A4F3  AD 00 02 LDA $0200
.A4F6  F0 88    BEQ $A480
.A4F8  18       CLC
.A4F9  A5 2D    LDA $2D
.A4FB  85 5A    STA $5A
.A4FD  65 0B    ADC $0B
.A4FF  85 58    STA $58
.A501  A4 2E    LDY $2E
.A503  84 5B    STY $5B
.A505  90 01    BCC $A508
.A507  C8       INY
.A508  84 59    STY $59
.A50A  20 B8 A3 JSR $A3B8
.A50D  A5 14    LDA $14
.A50F  A4 15    LDY $15
.A511  8D FE 01 STA $01FE
.A514  8C FF 01 STY $01FF
.A517  A5 31    LDA $31
.A519  A4 32    LDY $32
.A51B  85 2D    STA $2D
.A51D  84 2E    STY $2E
.A51F  A4 0B    LDY $0B
.A521  88       DEY
.A522  B9 FC 01 LDA $01FC,Y
.A525  91 5F    STA ($5F),Y
.A527  88       DEY
.A528  10 F8    BPL $A522
.A52A  20 59 A6 JSR $A659
.A52D  20 33 A5 JSR $A533
.A530  4C 80 A4 JMP $A480
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A4ED**: CLR-Befehl
- **$A4F0**: Programmzeilen neu binden
- **$A4F3**: Zeichen im Puffer ?
- **$A4F6**: nein, dann zur Warteschleife
- **$A4F8**: Carry löschen
- **$A4F9**: Variablenanfangszeiger (LOW)
- **$A4FB**: als Endadresse (Quellbereich)
- **$A4FD**: + Länge der Zeile als End-
- **$A4FF**: adresse des Zielbereichs LOW
- **$A501**: Variablenanfangszeiger als
- **$A503**: Endadr. des Quellbereichs LOW
- **$A505**: Kein Übertrag? dann $A508
- **$A507**: Übertrag addieren
- **$A508**: Als Endadresse des Zielbereichs
- **$A50A**: BASIC-Zeilen verschieben
- **$A50D**: Zeilennummer aus
- **$A50F**: $14/15 vor
- **$A511**: BASIC-Eingabepuffer setzen
- **$A514**: (ab $0200)
- **$A517**: Neuer Variablen-
- **$A519**: endzeiger
- **$A51B**: als Zeiger auf Programm-
- **$A51D**: ende speichern
- **$A51F**: Zeilenlänge holen
- **$A521**: und um 1 vermindern
- **$A522**: Zeile aus Eingabepuffer
- **$A525**: ins Programm kopieren
- **$A527**: Schon alle Zeichen?
- **$A528**: Nein: dann weiterkopieren
- **$A52A**: CLR-Befehl
- **$A52D**: Programmzeilen neu binden
- **$A530**: zur Eingabe-Warteschleife

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a4ed-insert-new-line]]
