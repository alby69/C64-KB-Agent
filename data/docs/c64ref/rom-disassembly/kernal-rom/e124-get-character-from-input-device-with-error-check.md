---
title: get character from input device with error check
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
- e124-basic-getin
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E124
  address_end: $E129
  symbol: get-character-from-input-device-with-error-check
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E124**: get character from input device'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E124**: ein Zeichen holen'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E124**: GETIN, get character from keyboard buffer'
---

# $E124 — get character from input device with error check

## Disassemblatura
```assembly
.E124  20 E4 FF JSR $FFE4   ; get character from input device
.E127  B0 D0    BCS $E0F9   ; if error go handle BASIC I/O error
.E129  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E124**: get character from input device
- **$E127**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E124**: ein Zeichen holen
- **$E127**: Fehler ?
- **$E129**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E124**: GETIN, get character from keyboard buffer
- **$E127**: if carry set, handle I/O error
- **$E129**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*