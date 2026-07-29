---
title: Handshake
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f07d-handshake
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F07D
  address_end: $F085
  symbol: handshake
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F07D**: RS-232 NMI Status laden'
---

# $F07D — Handshake

## Disassemblatura
```assembly
.F07D  AD A1 02 LDA $02A1   ; RS-232 NMI Status laden
.F080  29 12    AND #$12   ; wenn RS-232 nicht aktiv
.F082  F0 F3    BEQ $F077   ; dann starten
.F084  18       CLC   ; Carry löschen (ok Kenneichen)
.F085  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F07D**: RS-232 NMI Status laden
- **$F080**: wenn RS-232 nicht aktiv
- **$F082**: dann starten
- **$F084**: Carry löschen (ok Kenneichen)
- **$F085**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*