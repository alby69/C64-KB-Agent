---
title: get character and check for end of line
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E206
  address_end: $E20D
  symbol: get-character-and-check-for-end-of-line
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E206**: CHRGOT letztes Zeichen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E206**: get CHRGOT'
---

# $E206 — get character and check for end of line

## Disassemblatura
```assembly
.E206  20 79 00 JSR $0079
.E209  D0 02    BNE $E20D
.E20B  68       PLA
.E20C  68       PLA
.E20D  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$E206**: CHRGOT letztes Zeichen
- **$E209**: weiteres Zeichen, dann Rückkehr
- **$E20B**: sonst Rückkehr zur
- **$E20C**: übergeordneten Routine
- **$E20D**: Rücksprung
- **$E20E**: prüft auf Komma
- **$E211**: CHRGOT letztes Zeichen holen
- **$E214**: weitere Zeichen, dann Rückkehr
- **$E216**: 'SYNTAX ERROR'

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E206**: get CHRGOT
- **$E209**: if last character is a character, do normal exit
- **$E20B**: else, remove return address
- **$E20C**: to exit this AND the calling routine.
- **$E20D**: exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*