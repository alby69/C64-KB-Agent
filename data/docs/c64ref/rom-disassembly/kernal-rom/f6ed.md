---
title: ;
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
- 0091-stkey
- 00c6-ndx
- bne
- check
- clear
- clrch
- cmp
- f6ed-stop-taste-abfragen
- jsr
- lda
- php
- plp
- rts
- sta
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F6ED
  address_end: $F6FA
  sources:
  - name: Original Disassembly
    author: Commodore
    description: '- **$F6ED**: NSTOP  LDA STKEY       ;VALUE OF LAST ROW'
  - name: Original Disassembly
    author: —
    description: '- **$F6ED**: read the stop key column'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F6ED**: STOP-Flag laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F6ED**: STKEY'
---

# $F6ED — ;

## Disassemblatura
```assembly
.F6ED  A5 91    LDA $91   ; NSTOP  LDA STKEY       ;VALUE OF LAST ROW
.F6EF  C9 7F    CMP #$7F   ; CMP    #$7F            ;CHECK STOP KEY POSITION
.F6F1  D0 07    BNE $F6FA   ; BNE    STOP2           ;NOT DOWN
.F6F3  08       PHP   ; PHP
.F6F4  20 CC FF JSR $FFCC   ; JSR    CLRCH           ;CLEAR CHANNELS
.F6F7  85 C6    STA $C6   ; STA    NDX             ;FLUSH QUEUE
.F6F9  28       PLP   ; PLP
.F6FA  60       RTS   ; STOP2  RTS
```


## Commenti

### Original Disassembly (Commodore)
- **$F6ED**: NSTOP  LDA STKEY       ;VALUE OF LAST ROW
- **$F6EF**: CMP    #$7F            ;CHECK STOP KEY POSITION
- **$F6F1**: BNE    STOP2           ;NOT DOWN
- **$F6F3**: PHP
- **$F6F4**: JSR    CLRCH           ;CLEAR CHANNELS
- **$F6F7**: STA    NDX             ;FLUSH QUEUE
- **$F6F9**: PLP
- **$F6FA**: STOP2  RTS

### Original Disassembly (—)
- **$F6ED**: read the stop key column
- **$F6EF**: compare with [STP] down
- **$F6F1**: if not [STP] or not just [STP] exit just [STP] was pressed
- **$F6F3**: save status
- **$F6F4**: close input and output channels
- **$F6F7**: save the keyboard buffer index
- **$F6F9**: restore status

### Commodore-64-intern-Buch (Commodore)
- **$F6ED**: STOP-Flag laden
- **$F6EF**: auf Code für STOP testen
- **$F6F1**: verzweige falls nicht
- **$F6F3**: Statusregister retten
- **$F6F4**: Ein-Ausgabe zurücksetzen CLRCH
- **$F6F7**: Anzahl der gedrückten Tasten
- **$F6F9**: Statusregister holen
- **$F6FA**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F6ED**: STKEY
- **$F6EF**: <STOP> ?
- **$F6F1**: nope
- **$F6F4**: CLRCHN, close all I/O channels
- **$F6F7**: NDX, number of characters in keyboard buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*