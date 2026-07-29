---
title: perform GOTO
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
- a8a0-basic-befehl-goto
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A8A0
  address_end: $A8BA
  symbol: perform-goto
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A8A0**: get fixed-point number into temporary integer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A8A0**: Zeilennummer nach $14/$15'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A8A0**: GET GOTO LINE'
---

# $A8A0 — perform GOTO

## Disassemblatura
```assembly
.A8A0  20 6B A9 JSR $A96B   ; get fixed-point number into temporary integer
.A8A3  20 09 A9 JSR $A909   ; scan for next BASIC line
.A8A6  38       SEC   ; set carry for subtract
.A8A7  A5 39    LDA $39   ; get current line number low byte
.A8A9  E5 14    SBC $14   ; subtract temporary integer low byte
.A8AB  A5 3A    LDA $3A   ; get current line number high byte
.A8AD  E5 15    SBC $15   ; subtract temporary integer high byte
.A8AF  B0 0B    BCS $A8BC   ; if current line number >= temporary integer, go search from the start of memory
.A8B1  98       TYA   ; else copy line index to A
.A8B2  38       SEC   ; set carry (+1)
.A8B3  65 7A    ADC $7A   ; add BASIC execute pointer low byte
.A8B5  A6 7B    LDX $7B   ; get BASIC execute pointer high byte
.A8B7  90 07    BCC $A8C0   ; branch if no overflow to high byte
.A8B9  E8       INX   ; increment high byte
.A8BA  B0 04    BCS $A8C0   ; branch always (can never be carry)
```


## Commenti

### Original Disassembly (—)
- **$A8A0**: get fixed-point number into temporary integer
- **$A8A3**: scan for next BASIC line
- **$A8A6**: set carry for subtract
- **$A8A7**: get current line number low byte
- **$A8A9**: subtract temporary integer low byte
- **$A8AB**: get current line number high byte
- **$A8AD**: subtract temporary integer high byte
- **$A8AF**: if current line number >= temporary integer, go search from the start of memory
- **$A8B1**: else copy line index to A
- **$A8B2**: set carry (+1)
- **$A8B3**: add BASIC execute pointer low byte
- **$A8B5**: get BASIC execute pointer high byte
- **$A8B7**: branch if no overflow to high byte
- **$A8B9**: increment high byte
- **$A8BA**: branch always (can never be carry)

### Commodore-64-intern-Buch (Commodore)
- **$A8A0**: Zeilennummer nach $14/$15
- **$A8A3**: nächsten Zeilenanfang suchen
- **$A8A6**: Carry setzen (Subtraktion)
- **$A8A7**: aktuelle Zeilennummer (LOW)
- **$A8A9**: kleiner als laufende Zeile?
- **$A8AB**: aktuelle Zeilennummer (HIGH)
- **$A8AD**: kleiner als laufende Zeile?
- **$A8AF**: nein: $A8BC
- **$A8B1**: Differenz in Akku
- **$A8B2**: Carry setzen (Addition)
- **$A8B3**: Programmzeiger addieren
- **$A8B5**: sucht ab laufender Zeile
- **$A8B7**: unbedingter
- **$A8B9**: Sprung
- **$A8BA**: zu $A8C0
- **$A8BC**: sucht ab Programmstart
- **$A8C0**: sucht Programmzeile
- **$A8C3**: nicht gefunden: 'undef'd st.'
- **$A8C5**: von der Startadresse (Zeile)
- **$A8C7**: eins subtrahieren und als
- **$A8C9**: Programmzeiger (LOW)
- **$A8CB**: HIGH-Byte der Zeile laden
- **$A8CD**: Übertrag berücksichtigen
- **$A8CF**: und als Programmzeiger
- **$A8D1**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A8A0**: GET GOTO LINE
- **$A8A3**: POINT Y TO EOL
- **$A8AB**: IS CURRENT PAGE < GOTO PAGE?
- **$A8AF**: SEARCH FROM PROG START IF NOT
- **$A8B1**: OTHERWISE SEARCH FROM NEXT LINE
- **$A8BC**: GET PROGRAM BEGINNING
- **$A8C0**: SEARCH FOR GOTO LINE
- **$A8C3**: ERROR IF NOT THERE
- **$A8C5**: TXTPTR = START OF THE DESTINATION LINE
- **$A8D1**: RETURN TO NEWSTT OR GOSUB

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*