---
title: input character from channel with error check
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
- e112-basic-basin
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E112
  address_end: $E117
  symbol: input-character-from-channel-with-error-check
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E112**: input character from channel'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E112**: ein Zeichen holen'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E112**: input character from CHRIN'
---

# $E112 — input character from channel with error check

## Disassemblatura
```assembly
.E112  20 CF FF JSR $FFCF   ; input character from channel
.E115  B0 E2    BCS $E0F9   ; if error go handle BASIC I/O error
.E117  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E112**: input character from channel
- **$E115**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E112**: ein Zeichen holen
- **$E115**: Fehler ?
- **$E117**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E112**: input character from CHRIN
- **$E115**: if carry set, handle I/O error
- **$E117**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*