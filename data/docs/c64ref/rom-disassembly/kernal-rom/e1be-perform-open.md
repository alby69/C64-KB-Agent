---
title: perform OPEN
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
- e1be-basic-befehl-open
- f34a-open
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E1BE
  address_end: $E1C6
  symbol: perform-open
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E1BE**: get parameters for OPEN/CLOSE'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E1BE**: Parameter holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E1BE**: get parameters from text'
---

# $E1BE — perform OPEN

## Disassemblatura
```assembly
.E1BE  20 19 E2 JSR $E219   ; get parameters for OPEN/CLOSE
.E1C1  20 C0 FF JSR $FFC0   ; open a logical file
.E1C4  B0 0B    BCS $E1D1   ; branch if error
.E1C6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E1BE**: get parameters for OPEN/CLOSE
- **$E1C1**: open a logical file
- **$E1C4**: branch if error

### Commodore-64-intern-Buch (Commodore)
- **$E1BE**: Parameter holen
- **$E1C1**: OPEN-Routine
- **$E1C4**: Fehler ?
- **$E1C6**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E1BE**: get parameters from text
- **$E1C1**: execute OPEN
- **$E1C4**: if carry set, handle error

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*