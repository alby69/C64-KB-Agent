---
id: f6ed
type: entity
title: ;
aliases:
- or STOP Key F6ED/F770-F6FA/F77D
tags:
- jumps
- system-routines
- kernal-api
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/kernal-api/f6ed.md
  sha256: 1b8c7af96a66b208175aa224863c7ebec9e4b7c4243952ae57d4c5d4d9665c5e
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6ed.md
  sha256: a5fa84ff62ab750834addd9fc91a0a3a2e3aa5aefdacfc9507c95da9c46f5613
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f6ed
---

# ;



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

## References
- Source: [[src-f6ed]]
