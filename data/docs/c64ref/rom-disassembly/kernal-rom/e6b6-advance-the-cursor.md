---
title: advance the cursor
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
- e6b6-neu-berechnen
- e6ed-retreat-cursor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E6B6
  address_end: $E700
  symbol: advance-the-cursor
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E6B6**: test for line increment'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E6B6**: Zeilenzeiger erhöhen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E6B6**: check line increment'
---

# $E6B6 — advance the cursor

## Disassemblatura
```assembly
.E6B6  20 B3 E8 JSR $E8B3   ; test for line increment
.E6B9  E6 D3    INC $D3   ; increment the cursor column
.E6BB  A5 D5    LDA $D5   ; get current screen line length
.E6BD  C5 D3    CMP $D3   ; compare ?? with the cursor column
.E6BF  B0 3F    BCS $E700   ; exit if line length >= cursor column
.E6C1  C9 4F    CMP #$4F   ; compare with max length
.E6C3  F0 32    BEQ $E6F7   ; if at max clear column, back cursor up and do newline
.E6C5  AD 92 02 LDA $0292   ; get the autoscroll flag
.E6C8  F0 03    BEQ $E6CD   ; branch if autoscroll on
.E6CA  4C 67 E9 JMP $E967   ; else open space on screen
.E6CD  A6 D6    LDX $D6   ; get the cursor row
.E6CF  E0 19    CPX #$19   ; compare with max + 1
.E6D1  90 07    BCC $E6DA   ; if less than max + 1 go add this row to the current logical line
.E6D3  20 EA E8 JSR $E8EA   ; else scroll the screen
.E6D6  C6 D6    DEC $D6   ; decrement the cursor row
.E6D8  A6 D6    LDX $D6   ; get the cursor row add this row to the current logical line
.E6DA  16 D9    ASL $D9,X   ; shift start of line X pointer high byte
.E6DC  56 D9    LSR $D9,X   ; shift start of line X pointer high byte back, make next screen line start of logical line, increment line length and set pointers clear b7, start of logical line
.E6DE  E8       INX   ; increment screen row
.E6DF  B5 D9    LDA $D9,X   ; get start of line X pointer high byte
.E6E1  09 80    ORA #$80   ; mark as start of logical line
.E6E3  95 D9    STA $D9,X   ; set start of line X pointer high byte
.E6E5  CA       DEX   ; restore screen row
.E6E6  A5 D5    LDA $D5   ; get current screen line length add one line length and set the pointers for the start of the line
.E6E8  18       CLC   ; clear carry for add
.E6E9  69 28    ADC #$28   ; add one line length
.E6EB  85 D5    STA $D5   ; save current screen line length
.E6ED  B5 D9    LDA $D9,X   ; get start of line X pointer high byte
.E6EF  30 03    BMI $E6F4   ; exit loop if start of logical line
.E6F1  CA       DEX   ; else back up one line
.E6F2  D0 F9    BNE $E6ED   ; loop if not on first line
.E6F4  4C F0 E9 JMP $E9F0   ; fetch a screen address
.E6F7  C6 D6    DEC $D6   ; decrement the cursor row
.E6F9  20 7C E8 JSR $E87C   ; do newline
.E6FC  A9 00    LDA #$00   ; clear A
.E6FE  85 D3    STA $D3   ; clear the cursor column
.E700  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E6B6**: test for line increment
- **$E6B9**: increment the cursor column
- **$E6BB**: get current screen line length
- **$E6BD**: compare ?? with the cursor column
- **$E6BF**: exit if line length >= cursor column
- **$E6C1**: compare with max length
- **$E6C3**: if at max clear column, back cursor up and do newline
- **$E6C5**: get the autoscroll flag
- **$E6C8**: branch if autoscroll on
- **$E6CA**: else open space on screen
- **$E6CD**: get the cursor row
- **$E6CF**: compare with max + 1
- **$E6D1**: if less than max + 1 go add this row to the current logical line
- **$E6D3**: else scroll the screen
- **$E6D6**: decrement the cursor row
- **$E6D8**: get the cursor row add this row to the current logical line
- **$E6DA**: shift start of line X pointer high byte
- **$E6DC**: shift start of line X pointer high byte back, make next screen line start of logical line, increment line length and set pointers clear b7, start of logical line
- **$E6DE**: increment screen row
- **$E6DF**: get start of line X pointer high byte
- **$E6E1**: mark as start of logical line
- **$E6E3**: set start of line X pointer high byte
- **$E6E5**: restore screen row
- **$E6E6**: get current screen line length add one line length and set the pointers for the start of the line
- **$E6E8**: clear carry for add
- **$E6E9**: add one line length
- **$E6EB**: save current screen line length
- **$E6ED**: get start of line X pointer high byte
- **$E6EF**: exit loop if start of logical line
- **$E6F1**: else back up one line
- **$E6F2**: loop if not on first line
- **$E6F4**: fetch a screen address
- **$E6F7**: decrement the cursor row
- **$E6F9**: do newline
- **$E6FC**: clear A
- **$E6FE**: clear the cursor column

### Commodore-64-intern-Buch (Commodore)
- **$E6B6**: Zeilenzeiger erhöhen
- **$E6B9**: Cursorspalte erhöhen
- **$E6BB**: Zeilenlänge holen
- **$E6BD**: Vergleich mit Cursorspalte
- **$E6BF**: nicht überschritten, dann RTS
- **$E6C1**: 79 Zeichen (Doppelzeile) ?
- **$E6C3**: wenn ja, dann zu $E6F7
- **$E6C5**: Zeilenübergang nicht
- **$E6C8**: im Editmodus, dann zu $E6CD
- **$E6CA**: neue Zeile einfügen
- **$E6CD**: Zeile
- **$E6CF**: 25 ?
- **$E6D1**: wenn ja, dann zu $E6DA
- **$E6D3**: SCROLL
- **$E6D6**: Cursorzeilenzeiger erniedrigen
- **$E6D8**: Zähler holen
- **$E6DA**: Zeile
- **$E6DC**: markieren
- **$E6DE**: Zähler erhöhen
- **$E6DF**: Startzeile
- **$E6E1**: markieren
- **$E6E3**: und speichern
- **$E6E5**: Zähler erniedrigen
- **$E6E6**: Zeilenlänge
- **$E6E8**: mit
- **$E6E9**: 40 addieren
- **$E6EB**: und speichern
- **$E6ED**: keine Doppelzeile,
- **$E6EF**: dann zu $E6F4
- **$E6F1**: Zähler erniedrigen
- **$E6F2**: noch nicht alle?, dann weiter
- **$E6F4**: Zeiger auf Farb-RAM für Zeile X
- **$E6F7**: Cursorzeile erniedrigen
- **$E6F9**: und initialisieren
- **$E6FC**: Spalte
- **$E6FE**: auf Null
- **$E700**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E6B6**: check line increment
- **$E6B9**: increment PNTR, cursor column on current line
- **$E6BB**: LNMX, physical screen line length
- **$E6BD**: compare to PNTR
- **$E6BF**: not beyond end of line, exit
- **$E6C1**: $4f = 79
- **$E6C3**: put cursor on new logical line
- **$E6C5**: AUTODN, auto scroll down flag
- **$E6C8**: auto scroll is on
- **$E6CA**: open a space on the screen
- **$E6CD**: read TBLX, current line number
- **$E6CF**: $19 = 25
- **$E6D1**: less than 25
- **$E6D3**: scroll down
- **$E6D6**: place cursor on line 24
- **$E6DA**: clear bit7 in LDTB1 to indicate that it is line 2
- **$E6DC**: in the logical line
- **$E6DE**: next line
- **$E6DF**: set bit7 in LDTB1 to indicate that it is line 1
- **$E6E1**: in the logical line
- **$E6E6**: add $28 (40) to LNMX to allow 80 characters
- **$E6E8**: on the logical line

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*