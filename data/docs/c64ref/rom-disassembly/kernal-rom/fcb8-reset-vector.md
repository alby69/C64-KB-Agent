---
title: reset vector
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
- fcb8-x-indiziert
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FCB8
  address_end: $FCBB
  symbol: reset-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FCB8**: restore everything for STOP'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FCB8**: IRQ auf Standard'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $FCB8 — reset vector

## Disassemblatura
```assembly
.FCB8  20 93 FC JSR $FC93   ; restore everything for STOP
.FCBB  F0 97    BEQ $FC54   ; restore registers and exit interrupt, branch always
```


## Commenti

### Original Disassembly (—)
- **$FCB8**: restore everything for STOP
- **$FCBB**: restore registers and exit interrupt, branch always

### Commodore-64-intern-Buch (Commodore)
- **$FCB8**: IRQ auf Standard
- **$FCBB**: Abschluß IRQ
- **$FCBD**: IRQ-Vektor
- **$FCC0**: aus Tabelle setzen
- **$FCC3**: lRQ-Vektor
- **$FCC6**: aus Tabelle setzen
- **$FCC9**: Rücksprung
- **$FCCA**: Rekorder-
- **$FCCC**: motor
- **$FCCE**: ausschalten
- **$FCD0**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*