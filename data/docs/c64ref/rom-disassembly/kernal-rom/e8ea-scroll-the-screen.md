---
title: scroll the screen
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
- e8ea-bildschirm-scrollen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E8EA
  address_end: $E964
  symbol: scroll-the-screen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E8EA**: copy the tape buffer start pointer'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E8EA**: Alle'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E8EA**: temp store SAL on stack'
---

# $E8EA — scroll the screen

## Disassemblatura
```assembly
.E8EA  A5 AC    LDA $AC   ; copy the tape buffer start pointer
.E8EC  48       PHA   ; save it
.E8ED  A5 AD    LDA $AD   ; copy the tape buffer start pointer
.E8EF  48       PHA   ; save it
.E8F0  A5 AE    LDA $AE   ; copy the tape buffer end pointer
.E8F2  48       PHA   ; save it
.E8F3  A5 AF    LDA $AF   ; copy the tape buffer end pointer
.E8F5  48       PHA   ; save it
.E8F6  A2 FF    LDX #$FF   ; set to -1 for pre increment loop
.E8F8  C6 D6    DEC $D6   ; decrement the cursor row
.E8FA  C6 C9    DEC $C9   ; decrement the input cursor row
.E8FC  CE A5 02 DEC $02A5   ; decrement the screen row marker
.E8FF  E8       INX   ; increment the line number
.E900  20 F0 E9 JSR $E9F0   ; fetch a screen address, set the start of line X
.E903  E0 18    CPX #$18   ; compare with last line
.E905  B0 0C    BCS $E913   ; branch if >= $16
.E907  BD F1 EC LDA $ECF1,X   ; get the start of the next line pointer low byte
.E90A  85 AC    STA $AC   ; save the next line pointer low byte
.E90C  B5 DA    LDA $DA,X   ; get the start of the next line pointer high byte
.E90E  20 C8 E9 JSR $E9C8   ; shift the screen line up
.E911  30 EC    BMI $E8FF   ; loop, branch always
.E913  20 FF E9 JSR $E9FF   ; clear screen line X now shift up the start of logical line bits
.E916  A2 00    LDX #$00   ; clear index
.E918  B5 D9    LDA $D9,X   ; get the start of line X pointer high byte
.E91A  29 7F    AND #$7F   ; clear the line X start of logical line bit
.E91C  B4 DA    LDY $DA,X   ; get the start of the next line pointer high byte
.E91E  10 02    BPL $E922   ; if next line is not a start of line skip the start set
.E920  09 80    ORA #$80   ; set line X start of logical line bit
.E922  95 D9    STA $D9,X   ; set start of line X pointer high byte
.E924  E8       INX   ; increment line number
.E925  E0 18    CPX #$18   ; compare with last line
.E927  D0 EF    BNE $E918   ; loop if not last line
.E929  A5 F1    LDA $F1   ; get start of last line pointer high byte
.E92B  09 80    ORA #$80   ; mark as start of logical line
.E92D  85 F1    STA $F1   ; set start of last line pointer high byte
.E92F  A5 D9    LDA $D9   ; get start of first line pointer high byte
.E931  10 C3    BPL $E8F6   ; if not start of logical line loop back and scroll the screen up another line
.E933  E6 D6    INC $D6   ; increment the cursor row
.E935  EE A5 02 INC $02A5   ; increment screen row marker
.E938  A9 7F    LDA #$7F   ; set keyboard column c7
.E93A  8D 00 DC STA $DC00   ; save VIA 1 DRA, keyboard column drive
.E93D  AD 01 DC LDA $DC01   ; read VIA 1 DRB, keyboard row port
.E940  C9 FB    CMP #$FB   ; compare with row r2 active, [CTL]
.E942  08       PHP   ; save status
.E943  A9 7F    LDA #$7F   ; set keyboard column c7
.E945  8D 00 DC STA $DC00   ; save VIA 1 DRA, keyboard column drive
.E948  28       PLP   ; restore status
.E949  D0 0B    BNE $E956   ; skip delay if ?? first time round the inner loop X will be $16
.E94B  A0 00    LDY #$00   ; clear delay outer loop count, do this 256 times
.E94D  EA       NOP   ; waste cycles
.E94E  CA       DEX   ; decrement inner loop count
.E94F  D0 FC    BNE $E94D   ; loop if not all done
.E951  88       DEY   ; decrement outer loop count
.E952  D0 F9    BNE $E94D   ; loop if not all done
.E954  84 C6    STY $C6   ; clear the keyboard buffer index
.E956  A6 D6    LDX $D6   ; get the cursor row restore the tape buffer pointers and exit
.E958  68       PLA   ; pull tape buffer end pointer
.E959  85 AF    STA $AF   ; restore it
.E95B  68       PLA   ; pull tape buffer end pointer
.E95C  85 AE    STA $AE   ; restore it
.E95E  68       PLA   ; pull tape buffer pointer
.E95F  85 AD    STA $AD   ; restore it
.E961  68       PLA   ; pull tape buffer pointer
.E962  85 AC    STA $AC   ; restore it
.E964  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E8EA**: copy the tape buffer start pointer
- **$E8EC**: save it
- **$E8ED**: copy the tape buffer start pointer
- **$E8EF**: save it
- **$E8F0**: copy the tape buffer end pointer
- **$E8F2**: save it
- **$E8F3**: copy the tape buffer end pointer
- **$E8F5**: save it
- **$E8F6**: set to -1 for pre increment loop
- **$E8F8**: decrement the cursor row
- **$E8FA**: decrement the input cursor row
- **$E8FC**: decrement the screen row marker
- **$E8FF**: increment the line number
- **$E900**: fetch a screen address, set the start of line X
- **$E903**: compare with last line
- **$E905**: branch if >= $16
- **$E907**: get the start of the next line pointer low byte
- **$E90A**: save the next line pointer low byte
- **$E90C**: get the start of the next line pointer high byte
- **$E90E**: shift the screen line up
- **$E911**: loop, branch always
- **$E913**: clear screen line X now shift up the start of logical line bits
- **$E916**: clear index
- **$E918**: get the start of line X pointer high byte
- **$E91A**: clear the line X start of logical line bit
- **$E91C**: get the start of the next line pointer high byte
- **$E91E**: if next line is not a start of line skip the start set
- **$E920**: set line X start of logical line bit
- **$E922**: set start of line X pointer high byte
- **$E924**: increment line number
- **$E925**: compare with last line
- **$E927**: loop if not last line
- **$E929**: get start of last line pointer high byte
- **$E92B**: mark as start of logical line
- **$E92D**: set start of last line pointer high byte
- **$E92F**: get start of first line pointer high byte
- **$E931**: if not start of logical line loop back and scroll the screen up another line
- **$E933**: increment the cursor row
- **$E935**: increment screen row marker
- **$E938**: set keyboard column c7
- **$E93A**: save VIA 1 DRA, keyboard column drive
- **$E93D**: read VIA 1 DRB, keyboard row port
- **$E940**: compare with row r2 active, [CTL]
- **$E942**: save status
- **$E943**: set keyboard column c7
- **$E945**: save VIA 1 DRA, keyboard column drive
- **$E948**: restore status
- **$E949**: skip delay if ?? first time round the inner loop X will be $16
- **$E94B**: clear delay outer loop count, do this 256 times
- **$E94D**: waste cycles
- **$E94E**: decrement inner loop count
- **$E94F**: loop if not all done
- **$E951**: decrement outer loop count
- **$E952**: loop if not all done
- **$E954**: clear the keyboard buffer index
- **$E956**: get the cursor row restore the tape buffer pointers and exit
- **$E958**: pull tape buffer end pointer
- **$E959**: restore it
- **$E95B**: pull tape buffer end pointer
- **$E95C**: restore it
- **$E95E**: pull tape buffer pointer
- **$E95F**: restore it
- **$E961**: pull tape buffer pointer
- **$E962**: restore it

### Commodore-64-intern-Buch (Commodore)
- **$E8EA**: Alle
- **$E8EC**: wichtigen
- **$E8ED**: Zeiger
- **$E8EF**: in
- **$E8F0**: den
- **$E8F2**: Stack
- **$E8F3**: schie-
- **$E8F5**: ben
- **$E8F6**: ab Zeile Null beginnen
- **$E8F8**: Cursorzeiger
- **$E8FA**: erniedrigen
- **$E8FC**: Fortsetzungszeile erniedrigen
- **$E8FF**: Zeilennummer erhöhen
- **$E900**: Zeiger auf Video-RAM für Zeile X
- **$E903**: 24
- **$E905**: schon alle Zeilen ?
- **$E907**: LOW-Byte holen
- **$E90A**: und speichern
- **$E90C**: HIGH-Byte
- **$E90E**: Bildschirmzeile nach oben schieben
- **$E911**: nächste Zeile
- **$E913**: unterste Bildschirmzeile löschen
- **$E916**: HIGH-
- **$E918**: Bytes
- **$E91A**: und
- **$E91C**: die
- **$E91E**: Doppel-
- **$E920**: zeilen
- **$E922**: ver-
- **$E924**: schieben
- **$E925**: nicht 24 ?,
- **$E927**: dann nochmal
- **$E929**: Zeile
- **$E92B**: als einfache Zeile
- **$E92D**: auszeichnen
- **$E92F**: wenn Fortsetzungszeile,
- **$E931**: dann nochmal
- **$E933**: Zeiger auf Cursor erhöhen
- **$E935**: Fortsetzungszeile erhöhen
- **$E938**: Kode
- **$E93A**: für
- **$E93D**: Tastaturabfrage
- **$E940**: CTRL-Taste gedrückt ?
- **$E942**: Statusregister retten
- **$E943**: code für
- **$E945**: Tastaturabfrage
- **$E948**: Statusregister holen
- **$E949**: nicht gedrückt ?
- **$E94B**: Ver-
- **$E94D**: zö-
- **$E94E**: geru-
- **$E94F**: ngs-
- **$E951**: sch-
- **$E952**: leife
- **$E954**: Anzahl der gedrückten Tasten gleich null
- **$E956**: alle
- **$E958**: benö-
- **$E959**: tigten
- **$E95B**: Zei-
- **$E95C**: ger
- **$E95E**: zu-
- **$E95F**: rück-
- **$E961**: ho-
- **$E962**: len
- **$E964**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E8EA**: temp store SAL on stack
- **$E8F0**: temp store EAL on stack
- **$E8F8**: decrement TBLX
- **$E8FA**: decrement LXSP
- **$E8FC**: temp store for line index
- **$E900**: set start of line (X)
- **$E907**: read low-byte screen addresses
- **$E90E**: move a screen line
- **$E913**: clear a screen line
- **$E918**: calculate new screen line link table
- **$E91A**: clear bit7
- **$E920**: set bit7
- **$E922**: store new value in table
- **$E924**: next line
- **$E925**: till all 25 are done
- **$E929**: bottom line link
- **$E92B**: unlink it
- **$E92D**: and store back
- **$E92F**: test top line link
- **$E931**: line is linked, scroll again
- **$E933**: increment TBLX
- **$E93D**: read keyboard decode column
- **$E940**: <CTRL> pressed
- **$E949**: nope, exit
- **$E954**: clear NDX
- **$E956**: read TBLX
- **$E958**: retrieve EAL
- **$E95E**: retrieve SAL
- **$E964**: exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*