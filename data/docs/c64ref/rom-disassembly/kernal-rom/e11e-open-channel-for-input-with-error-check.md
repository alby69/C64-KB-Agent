---
title: open channel for input with error check
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
- e11e-basic-chkin
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E11E
  address_end: $E123
  symbol: open-channel-for-input-with-error-check
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E11E**: open channel for input'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E11E**: Eingabegerät setzen'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E11E**: open input channel via CHKIN'
---

# $E11E — open channel for input with error check

## Disassemblatura
```assembly
.E11E  20 C6 FF JSR $FFC6   ; open channel for input
.E121  B0 D6    BCS $E0F9   ; if error go handle BASIC I/O error
.E123  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E11E**: open channel for input
- **$E121**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E11E**: Eingabegerät setzen
- **$E121**: Fehler ?
- **$E123**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E11E**: open input channel via CHKIN
- **$E121**: if carry set, handle I/O error
- **$E123**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*