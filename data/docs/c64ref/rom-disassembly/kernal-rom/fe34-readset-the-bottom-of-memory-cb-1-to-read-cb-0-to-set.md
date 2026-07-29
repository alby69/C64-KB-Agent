---
title: read/set the bottom of memory, Cb = 1 to read, Cb = 0 to set
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
- fe34-basic-ram-holensetzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE34
  address_end: $FE42
  symbol: readset-the-bottom-of-memory-cb-1-to-read-cb-0-to-set
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE34**: if Cb clear go set the bottom of memory'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE34**: C=0: Adresse setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE34**: carry clear?'
---

# $FE34 — read/set the bottom of memory, Cb = 1 to read, Cb = 0 to set

## Disassemblatura
```assembly
.FE34  90 06    BCC $FE3C   ; if Cb clear go set the bottom of memory
.FE36  AE 81 02 LDX $0281   ; get the OS start of memory low byte
.FE39  AC 82 02 LDY $0282   ; get the OS start of memory high byte
.FE3C  8E 81 02 STX $0281   ; save the OS start of memory low byte
.FE3F  8C 82 02 STY $0282   ; save the OS start of memory high byte
.FE42  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FE34**: if Cb clear go set the bottom of memory
- **$FE36**: get the OS start of memory low byte
- **$FE39**: get the OS start of memory high byte
- **$FE3C**: save the OS start of memory low byte
- **$FE3F**: save the OS start of memory high byte

### Commodore-64-intern-Buch (Commodore)
- **$FE34**: C=0: Adresse setzen
- **$FE36**: Carry gesetzt
- **$FE39**: Adresse nach X/Y holen
- **$FE3C**: Carry gelöscht
- **$FE3F**: Adresse aus X/Y setzen
- **$FE42**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE34**: carry clear?
- **$FE36**: read membot from MEMSTR
- **$FE3C**: store membot in MEMSTR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*