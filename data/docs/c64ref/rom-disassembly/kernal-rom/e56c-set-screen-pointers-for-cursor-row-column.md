---
title: set screen pointers for cursor row, column
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
- e56c-bildschirmzeiger-setzen
- e591-this-is-a-patch-for-input-logic-901227-03
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E56C
  address_end: $E598
  symbol: set-screen-pointers-for-cursor-row-column
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E56C**: get the cursor row'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E56C**: Cursorzeile'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E56C**: read TBLX'
---

# $E56C — set screen pointers for cursor row, column

## Disassemblatura
```assembly
.E56C  A6 D6    LDX $D6   ; get the cursor row
.E56E  A5 D3    LDA $D3   ; get the cursor column
.E570  B4 D9    LDY $D9,X   ; get start of line X pointer high byte
.E572  30 08    BMI $E57C   ; if it is the logical line start continue
.E574  18       CLC   ; else clear carry for add
.E575  69 28    ADC #$28   ; add one line length
.E577  85 D3    STA $D3   ; save the cursor column
.E579  CA       DEX   ; decrement the cursor row
.E57A  10 F4    BPL $E570   ; loop, branch always
.E57C  20 F0 E9 JSR $E9F0   ; fetch a screen address
.E57F  A9 27    LDA #$27   ; set the line length
.E581  E8       INX   ; increment the cursor row
.E582  B4 D9    LDY $D9,X   ; get the start of line X pointer high byte
.E584  30 06    BMI $E58C   ; if logical line start exit
.E586  18       CLC   ; else clear carry for add
.E587  69 28    ADC #$28   ; add one line length to the current line length
.E589  E8       INX   ; increment the cursor row
.E58A  10 F6    BPL $E582   ; loop, branch always
.E58C  85 D5    STA $D5   ; save current screen line length
.E58E  4C 24 EA JMP $EA24   ; calculate the pointer to colour RAM and return
.E591  E4 C9    CPX $C9   ; compare it with the input cursor row
.E593  F0 03    BEQ $E598   ; if there just exit
.E595  4C ED E6 JMP $E6ED   ; else go ??
.E598  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E56C**: get the cursor row
- **$E56E**: get the cursor column
- **$E570**: get start of line X pointer high byte
- **$E572**: if it is the logical line start continue
- **$E574**: else clear carry for add
- **$E575**: add one line length
- **$E577**: save the cursor column
- **$E579**: decrement the cursor row
- **$E57A**: loop, branch always
- **$E57C**: fetch a screen address
- **$E57F**: set the line length
- **$E581**: increment the cursor row
- **$E582**: get the start of line X pointer high byte
- **$E584**: if logical line start exit
- **$E586**: else clear carry for add
- **$E587**: add one line length to the current line length
- **$E589**: increment the cursor row
- **$E58A**: loop, branch always
- **$E58C**: save current screen line length
- **$E58E**: calculate the pointer to colour RAM and return
- **$E591**: compare it with the input cursor row
- **$E593**: if there just exit
- **$E595**: else go ??

### Commodore-64-intern-Buch (Commodore)
- **$E56C**: Cursorzeile
- **$E56E**: Cursorspalte
- **$E570**: HIGH-Bytes für Doppelzeilen
- **$E572**: einfache Zeile, dann zu $E57C
- **$E574**: Spalte
- **$E575**: +40
- **$E577**: und speichern
- **$E579**: nächste Zeile
- **$E57A**: schon alle?
- **$E57C**: Zeiger auf Video-RAM setzen
- **$E57F**: 39 Spalten
- **$E581**: Zeiger auf Bildschirmtabelle erhöhen
- **$E582**: HIGH-Byte Startadresse der Zeile in Y-REG schreiben
- **$E584**: Verzweige falls größer, gleich 128
- **$E586**: Cursor eine Zeile
- **$E587**: tiefer setzen (+40 Spalten)
- **$E589**: Zeiger auf Bildschirmtabelle erhöhen
- **$E58A**: unbedingter Sprung
- **$E58C**: Zeilenlänge speichern
- **$E58E**: Zeiger auf Farb-RAM berechnen Rücksprung
- **$E591**: wenn Cursorzeile
- **$E593**: gleich null, dann Rücksprung
- **$E595**: Adresse für zugehörige Zeilennummer nach $D1/$D2
- **$E598**: Rücksprung
- **$E599**: no operation
- **$E59A**: Videocontroller initialisieren
- **$E59D**: Cursor Home

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E56C**: read TBLX
- **$E56E**: read PNTR
- **$E570**: read value from screen line link table, LDTB1
- **$E572**: heavy calculations??? jump when ready
- **$E577**: PNTR
- **$E57C**: set start of line (X)
- **$E582**: LDTB1
- **$E58C**: store in LMNX, physical screen line length
- **$E58E**: sync color pointer
- **$E591**: read LXSP, check cursor at start of input
- **$E595**: retreat cursor
- **$E599**: A free byte!!!

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*