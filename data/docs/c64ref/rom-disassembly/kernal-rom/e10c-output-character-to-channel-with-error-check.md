---
title: output character to channel with error check
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
- e10c-basic-bsout
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E10C
  address_end: $E111
  symbol: output-character-to-channel-with-error-check
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E10C**: output character to channel'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E10C**: ein Zeichen ausgeben'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E10C**: output character in (A)'
---

# $E10C — output character to channel with error check

## Disassemblatura
```assembly
.E10C  20 D2 FF JSR $FFD2   ; output character to channel
.E10F  B0 E8    BCS $E0F9   ; if error go handle BASIC I/O error
.E111  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E10C**: output character to channel
- **$E10F**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E10C**: ein Zeichen ausgeben
- **$E10F**: Fehler ?
- **$E111**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E10C**: output character in (A)
- **$E10F**: if carry set, handle I/O error
- **$E111**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*