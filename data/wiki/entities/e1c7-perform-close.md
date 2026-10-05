---
id: e1c7-perform-close
type: entity
title: perform CLOSE
aliases:
- perform CLOSE
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e1c7-perform-close.md
  sha256: 00996d22173c53f7b8c6b26898fba66482ab7df5f50917d6dadb600f1d6513d7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e1c7-perform-close
---

# perform CLOSE



# $E1C7 — perform CLOSE

## Disassemblatura
```assembly
.E1C7  20 19 E2 JSR $E219   ; get parameters for OPEN/CLOSE
.E1CA  A5 49    LDA $49   ; get logical file number
.E1CC  20 C3 FF JSR $FFC3   ; close a specified logical file
.E1CF  90 C3    BCC $E194   ; exit if no error
.E1D1  4C F9 E0 JMP $E0F9   ; go handle BASIC I/O error
```


## Commenti

### Original Disassembly (—)
- **$E1C7**: get parameters for OPEN/CLOSE
- **$E1CA**: get logical file number
- **$E1CC**: close a specified logical file
- **$E1CF**: exit if no error
- **$E1D1**: go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E1C7**: Parameter holen
- **$E1CA**: Filenummer
- **$E1CC**: CLOSE-Routine
- **$E1CF**: kein Fehler, RTS
- **$E1D1**: zur Fehlerauswertung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E1C7**: get parameters from text
- **$E1CA**: logical file number
- **$E1CC**: perform CLOSE
- **$E1CF**: if carry set, handle error, else return
- **$E1D1**: jump to error routine

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e1c7-perform-close]]
