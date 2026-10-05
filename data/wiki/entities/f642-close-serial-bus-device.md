---
id: f642-close-serial-bus-device
type: entity
title: close serial bus device
aliases:
- close serial bus device
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f642-close-serial-bus-device.md
  sha256: d8f43df79450af6a24d1df6f6d910d6c31e53c9ec10c05710465d5ad7524371a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f642-close-serial-bus-device
---

# close serial bus device



# $F642 — close serial bus device

## Disassemblatura
```assembly
.F642  24 B9    BIT $B9
.F644  30 11    BMI $F657
.F646  A5 BA    LDA $BA
.F648  20 0C ED JSR $ED0C
.F64B  A5 B9    LDA $B9
.F64D  29 EF    AND #$EF
.F64F  09 E0    ORA #$E0
.F651  20 B9 ED JSR $EDB9
.F654  20 FE ED JSR $EDFE
.F657  18       CLC
.F658  60       RTS
.F659  4A       LSR
.F65A  B0 03    BCS $F65F
.F65C  4C 13 F7 JMP $F713
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F642**: Sekundäradresse testen
- **$F644**: verzweige falls keine Sekundäradresse
- **$F646**: Geräteadresse laden
- **$F648**: und LISTEN senden
- **$F64B**: Sekundäradresse laden
- **$F64D**: Sekundäradresse
- **$F64F**: für CLOSE berechnen
- **$F651**: und ausgeben
- **$F654**: UNLISTEN senden
- **$F657**: Carry =0 (ok Kennzeichen)
- **$F658**: Rücksprung
- **$F659**: Bit 0 ins Carry schieben
- **$F65A**: falls gesetzt, dann zu Band
- **$F65C**: sonst RS-232, 'ILLEGAL DIVICE NUMBER'
- **$F65F**: Bandpuffer Startadresse holen
- **$F662**: falls HIGH-Byte der Band Pufferstartadresse kleiner 2 dann 'ILLEGAL DEVICE NUMBER'
- **$F664**: wartet auf Record & Play- Taste
- **$F667**: STOP, dann Abbruch
- **$F669**: 'SAVING' (Name) ausgeben
- **$F66C**: Header-Typ 3 = Maschinen programm (absolut)
- **$F66E**: Sekundäradresse laden
- **$F670**: Bit 0 gesetzt (1 oder 3)
- **$F672**: falls ja, dann Maschinen programm
- **$F674**: Header-Typ 1 = BASIC- Programm (verschiebbar)
- **$F676**: Header in Akku schieben
- **$F677**: Header auf Band schreiben
- **$F67A**: Aussprung bei Stop-Taste
- **$F67C**: Programm auf Band schreiben
- **$F67F**: Aussprung bei Stop-Taste
- **$F681**: Sekundäradresse laden
- **$F683**: Bit 1 gesetzt (2 oder 3)
- **$F685**: falls nicht, dann fertig
- **$F687**: EOT Kontrollbyte
- **$F689**: Block auf Band schreiben
- **$F68C**: Skip zu $F68E
- **$F68D**: Carry =0 (ok Kennzeichen)
- **$F68E**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f642-close-serial-bus-device]]
