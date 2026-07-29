---
title: clear the screen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e544-bildschirm-lschen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E544
  address_end: $E564
  symbol: clear-the-screen
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E544**: get the screen memory page'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E544**: Speicherseite für Bildschirm-RAM'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E544**: get HIBASE, top of screen memory'
---

# $E544 — clear the screen

## Disassemblatura
```assembly
.E544  AD 88 02 LDA $0288   ; get the screen memory page
.E547  09 80    ORA #$80   ; set the high bit, flag every line is a logical line start
.E549  A8       TAY   ; copy to Y
.E54A  A9 00    LDA #$00   ; clear the line start low byte
.E54C  AA       TAX   ; clear the index
.E54D  94 D9    STY $D9,X   ; save the start of line X pointer high byte
.E54F  18       CLC   ; clear carry for add
.E550  69 28    ADC #$28   ; add the line length to the low byte
.E552  90 01    BCC $E555   ; if no rollover skip the high byte increment
.E554  C8       INY   ; else increment the high byte
.E555  E8       INX   ; increment the line index
.E556  E0 1A    CPX #$1A   ; compare it with the number of lines + 1
.E558  D0 F3    BNE $E54D   ; loop if not all done
.E55A  A9 FF    LDA #$FF   ; set the end of table marker
.E55C  95 D9    STA $D9,X   ; mark the end of the table
.E55E  A2 18    LDX #$18   ; set the line count, 25 lines to do, 0 to 24
.E560  20 FF E9 JSR $E9FF   ; clear screen line X
.E563  CA       DEX   ; decrement the count
.E564  10 FA    BPL $E560   ; loop if more to do
```


## Commenti

### Original Disassembly (—)
- **$E544**: get the screen memory page
- **$E547**: set the high bit, flag every line is a logical line start
- **$E549**: copy to Y
- **$E54A**: clear the line start low byte
- **$E54C**: clear the index
- **$E54D**: save the start of line X pointer high byte
- **$E54F**: clear carry for add
- **$E550**: add the line length to the low byte
- **$E552**: if no rollover skip the high byte increment
- **$E554**: else increment the high byte
- **$E555**: increment the line index
- **$E556**: compare it with the number of lines + 1
- **$E558**: loop if not all done
- **$E55A**: set the end of table marker
- **$E55C**: mark the end of the table
- **$E55E**: set the line count, 25 lines to do, 0 to 24
- **$E560**: clear screen line X
- **$E563**: decrement the count
- **$E564**: loop if more to do

### Commodore-64-intern-Buch (Commodore)
- **$E544**: Speicherseite für Bildschirm-RAM
- **$E547**: Adressen
- **$E549**: der
- **$E54A**: Bild-
- **$E54C**: schirm-
- **$E54D**: zeilen
- **$E54F**: 40 addieren
- **$E550**: (eine Zeile)
- **$E552**: kein Übertrag, dann HIGH-Byte nicht erhöhen
- **$E554**: HIGH-Byte erhöhen
- **$E555**: LOW-Byte erhöhen
- **$E556**: 26, alle Zeilen ?
- **$E558**: nein, dann weiter
- **$E55A**: Kennzeichnung der
- **$E55C**: 26, Zeile
- **$E55E**: 24, Anzahl der Zeilen minus 1
- **$E560**: Bildschirmzeile löschen
- **$E563**: Zähler erniedrigen
- **$E564**: schon alle?

### Magnus Nyman (Magnus Nyman)
- **$E544**: get HIBASE, top of screen memory
- **$E547**: fool around
- **$E54D**: store in screen line link table, LDTB1
- **$E550**: add #40 to next line
- **$E554**: inc page number
- **$E555**: next
- **$E556**: till all 26?? is done
- **$E55C**: last pointer is $ff
- **$E55E**: start clear screen with line $18 (bottom line)
- **$E560**: erase line (X)
- **$E563**: next
- **$E564**: till screen is empty

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*