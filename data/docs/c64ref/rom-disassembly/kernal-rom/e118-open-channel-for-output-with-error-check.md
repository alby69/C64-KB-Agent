---
title: open channel for output with error check
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
- e118-basic-ckout
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E118
  address_end: $E11D
  symbol: open-channel-for-output-with-error-check
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E118**: open channel for output'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E118**: Ausgabegerät setzen'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E118**: open output channel via CHKOUT'
---

# $E118 — open channel for output with error check

## Disassemblatura
```assembly
.E118  20 AD E4 JSR $E4AD   ; open channel for output
.E11B  B0 DC    BCS $E0F9   ; if error go handle BASIC I/O error
.E11D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E118**: open channel for output
- **$E11B**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E118**: Ausgabegerät setzen
- **$E11B**: Fehler ?
- **$E11D**: Rücksprung

### Magnus Nyman (Magnus Nyman)
- **$E118**: open output channel via CHKOUT
- **$E11B**: if carry set, handle I/O error
- **$E11D**: else return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*