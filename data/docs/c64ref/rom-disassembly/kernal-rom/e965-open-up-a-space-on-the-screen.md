---
title: open up a space on the screen
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
- e965-fortsetzungszeile
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E965
  address_end: $E9C5
  symbol: open-up-a-space-on-the-screen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E965**: get the cursor row'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E965**: Zeiger auf Cursorzeile'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E965**: TBLX, current cursor line number'
---

# $E965 — open up a space on the screen

## Disassemblatura
```assembly
.E965  A6 D6    LDX $D6   ; get the cursor row
.E967  E8       INX   ; increment the row
.E968  B5 D9    LDA $D9,X   ; get the start of line X pointer high byte
.E96A  10 FB    BPL $E967   ; loop if not start of logical line
.E96C  8E A5 02 STX $02A5   ; save the screen row marker
.E96F  E0 18    CPX #$18   ; compare it with the last line
.E971  F0 0E    BEQ $E981   ; if = last line go ??
.E973  90 0C    BCC $E981   ; if < last line go ?? else it was > last line
.E975  20 EA E8 JSR $E8EA   ; scroll the screen
.E978  AE A5 02 LDX $02A5   ; get the screen row marker
.E97B  CA       DEX   ; decrement the screen row marker
.E97C  C6 D6    DEC $D6   ; decrement the cursor row
.E97E  4C DA E6 JMP $E6DA   ; add this row to the current logical line and return
.E981  A5 AC    LDA $AC   ; copy tape buffer pointer
.E983  48       PHA   ; save it
.E984  A5 AD    LDA $AD   ; copy tape buffer pointer
.E986  48       PHA   ; save it
.E987  A5 AE    LDA $AE   ; copy tape buffer end pointer
.E989  48       PHA   ; save it
.E98A  A5 AF    LDA $AF   ; copy tape buffer end pointer
.E98C  48       PHA   ; save it
.E98D  A2 19    LDX #$19   ; set to end line + 1 for predecrement loop
.E98F  CA       DEX   ; decrement the line number
.E990  20 F0 E9 JSR $E9F0   ; fetch a screen address
.E993  EC A5 02 CPX $02A5   ; compare it with the screen row marker
.E996  90 0E    BCC $E9A6   ; if < screen row marker go ??
.E998  F0 0C    BEQ $E9A6   ; if = screen row marker go ??
.E99A  BD EF EC LDA $ECEF,X   ; else get the start of the previous line low byte from the ROM table
.E99D  85 AC    STA $AC   ; save previous line pointer low byte
.E99F  B5 D8    LDA $D8,X   ; get the start of the previous line pointer high byte
.E9A1  20 C8 E9 JSR $E9C8   ; shift the screen line down
.E9A4  30 E9    BMI $E98F   ; loop, branch always
.E9A6  20 FF E9 JSR $E9FF   ; clear screen line X
.E9A9  A2 17    LDX #$17
.E9AB  EC A5 02 CPX $02A5   ; compare it with the screen row marker
.E9AE  90 0F    BCC $E9BF
.E9B0  B5 DA    LDA $DA,X
.E9B2  29 7F    AND #$7F
.E9B4  B4 D9    LDY $D9,X   ; get start of line X pointer high byte
.E9B6  10 02    BPL $E9BA
.E9B8  09 80    ORA #$80
.E9BA  95 DA    STA $DA,X
.E9BC  CA       DEX
.E9BD  D0 EC    BNE $E9AB
.E9BF  AE A5 02 LDX $02A5   ; get the screen row marker
.E9C2  20 DA E6 JSR $E6DA   ; add this row to the current logical line
.E9C5  4C 58 E9 JMP $E958   ; restore the tape buffer pointers and exit
```


## Commenti

### Original Disassembly (—)
- **$E965**: get the cursor row
- **$E967**: increment the row
- **$E968**: get the start of line X pointer high byte
- **$E96A**: loop if not start of logical line
- **$E96C**: save the screen row marker
- **$E96F**: compare it with the last line
- **$E971**: if = last line go ??
- **$E973**: if < last line go ?? else it was > last line
- **$E975**: scroll the screen
- **$E978**: get the screen row marker
- **$E97B**: decrement the screen row marker
- **$E97C**: decrement the cursor row
- **$E97E**: add this row to the current logical line and return
- **$E981**: copy tape buffer pointer
- **$E983**: save it
- **$E984**: copy tape buffer pointer
- **$E986**: save it
- **$E987**: copy tape buffer end pointer
- **$E989**: save it
- **$E98A**: copy tape buffer end pointer
- **$E98C**: save it
- **$E98D**: set to end line + 1 for predecrement loop
- **$E98F**: decrement the line number
- **$E990**: fetch a screen address
- **$E993**: compare it with the screen row marker
- **$E996**: if < screen row marker go ??
- **$E998**: if = screen row marker go ??
- **$E99A**: else get the start of the previous line low byte from the ROM table
- **$E99D**: save previous line pointer low byte
- **$E99F**: get the start of the previous line pointer high byte
- **$E9A1**: shift the screen line down
- **$E9A4**: loop, branch always
- **$E9A6**: clear screen line X
- **$E9AB**: compare it with the screen row marker
- **$E9B4**: get start of line X pointer high byte
- **$E9BF**: get the screen row marker
- **$E9C2**: add this row to the current logical line
- **$E9C5**: restore the tape buffer pointers and exit

### Commodore-64-intern-Buch (Commodore)
- **$E965**: Zeiger auf Cursorzeile
- **$E967**: Zeiger erhöhen
- **$E968**: untere Zeile gleich
- **$E96A**: Cursorzeile, dann zu $E967
- **$E96C**: Zeilennummer
- **$E96F**: gleich
- **$E971**: 24
- **$E973**: dann zu $E981
- **$E975**: Bildschirm scrollen
- **$E978**: Zeilennummer
- **$E97B**: erniedrigen
- **$E97C**: Zeiger auf Cursorzeile erniedrigen
- **$E97E**: Zeile initialisieren
- **$E981**: Alle
- **$E983**: benötigten
- **$E984**: Zeiger
- **$E986**: in
- **$E987**: den
- **$E989**: Stack
- **$E98A**: schie-
- **$E98C**: ben
- **$E98D**: 25
- **$E98F**: Zeilennummer
- **$E990**: Zeilen-Zeiger berechnen
- **$E993**: alle Zeilen verschoben ?,
- **$E996**: wenn ja,
- **$E998**: dann zu $E9A6
- **$E99A**: LOW-Byte des Zeilenanfangs
- **$E99D**: setzen
- **$E99F**: HIGH-Byte setzen
- **$E9A1**: Zeile nach oben schieben
- **$E9A4**: Unbedingter Sprung
- **$E9A6**: Bildschirmzeile löschen
- **$E9A9**: HIGH-Byte-Tabelle
- **$E9AB**: verschieben
- **$E9AE**: alles verschoben ?
- **$E9B0**: HIGH-
- **$E9B2**: Byte-
- **$E9B4**: und
- **$E9B6**: Doppelzeilen-
- **$E9B8**: Tabelle
- **$E9BA**: nach
- **$E9BC**: unten schieben
- **$E9BD**: schon alles ?
- **$E9BF**: Zeilennummer
- **$E9C2**: MSB neu berechnen
- **$E9C5**: Register zurückholen, RTS

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E965**: TBLX, current cursor line number
- **$E967**: test next
- **$E968**: LDTB1, screen line link table
- **$E96C**: temp line for index
- **$E96F**: bottom of screen
- **$E971**: yes
- **$E973**: above bottom line
- **$E975**: scroll screen down
- **$E978**: temp line for index
- **$E97C**: TBLX
- **$E97E**: adjust link table and end
- **$E981**: push SAL, scrolling pointer
- **$E987**: push EAL, end of program
- **$E990**: set start of line
- **$E993**: temp line for index
- **$E99A**: screen line address table
- **$E99D**: SAL
- **$E99F**: LDTB1
- **$E9A1**: move screen line
- **$E9A6**: clear screen line
- **$E9A9**: fix screen line link table
- **$E9AB**: temp line for index
- **$E9B0**: LDTB1+1
- **$E9B4**: LDTB1
- **$E9BC**: next line
- **$E9BD**: till line zero
- **$E9BF**: temp line for index
- **$E9C2**: adjust link table
- **$E9C5**: pull SAL and EAL

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*