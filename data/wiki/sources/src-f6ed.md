---
id: src-f6ed
type: source
title: 'Source Summary: ;'
aliases:
- ;
- f6ed.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f6ed.md
  sha256: a5fa84ff62ab750834addd9fc91a0a3a2e3aa5aefdacfc9507c95da9c46f5613
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f6ed.md`
**SHA256**: `a5fa84ff62ab750834addd9fc91a0a3a2e3aa5aefdacfc9507c95da9c46f5613`

## Summary



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

#...
