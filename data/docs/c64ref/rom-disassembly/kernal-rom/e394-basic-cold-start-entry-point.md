---
title: BASIC cold start entry point
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
- e394-basic-kaltstart
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E394
  address_end: $E3A0
  symbol: basic-cold-start-entry-point
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E394**: initialise the BASIC vector table'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E394**: BASIC-Vektoren setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E397**: Initialize BASIC'
---

# $E394 — BASIC cold start entry point

## Disassemblatura
```assembly
.E394  20 53 E4 JSR $E453   ; initialise the BASIC vector table
.E397  20 BF E3 JSR $E3BF   ; initialise the BASIC RAM locations
.E39A  20 22 E4 JSR $E422   ; print the start up message and initialise the memory pointers not ok ??
.E39D  A2 FB    LDX #$FB   ; value for start stack
.E39F  9A       TXS   ; set stack pointer
.E3A0  D0 E4    BNE $E386   ; do "READY." warm start, branch always
```


## Commenti

### Original Disassembly (—)
- **$E394**: initialise the BASIC vector table
- **$E397**: initialise the BASIC RAM locations
- **$E39A**: print the start up message and initialise the memory pointers not ok ??
- **$E39D**: value for start stack
- **$E39F**: set stack pointer
- **$E3A0**: do "READY." warm start, branch always

### Commodore-64-intern-Buch (Commodore)
- **$E394**: BASIC-Vektoren setzen
- **$E397**: RAM initialisieren
- **$E39A**: Einschaltmeldung ausgeben
- **$E39D**: Stackzeiger
- **$E39F**: setzen
- **$E3A0**: zum Warmstart

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E397**: Initialize BASIC
- **$E39A**: output power-up message
- **$E39D**: reset stack
- **$E3A0**: output READY, and restart BASIC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*