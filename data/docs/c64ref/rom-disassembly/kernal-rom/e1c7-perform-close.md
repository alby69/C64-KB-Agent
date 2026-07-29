---
title: perform CLOSE
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
- close
- e1c7-basic-befehl-close
- f34a-open
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E1C7
  address_end: $E1D1
  symbol: perform-close
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E1C7**: get parameters for OPEN/CLOSE'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E1C7**: Parameter holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E1C7**: get parameters from text'
---

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