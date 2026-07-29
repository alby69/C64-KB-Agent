---
title: read/set the top of memory, Cb = 1 to read, Cb = 0 to set
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
- fe25-basic-ram-holensetzen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE25
  address_end: $FE25
  symbol: readset-the-top-of-memory-cb-1-to-read-cb-0-to-set
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE25**: if Cb clear go set the top of memory'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE25**: C=0: Adresse setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE25**: carry clear?'
---

# $FE25 — read/set the top of memory, Cb = 1 to read, Cb = 0 to set

## Disassemblatura
```assembly
.FE25  90 06    BCC $FE2D   ; if Cb clear go set the top of memory
```


## Commenti

### Original Disassembly (—)
- **$FE25**: if Cb clear go set the top of memory

### Commodore-64-intern-Buch (Commodore)
- **$FE25**: C=0: Adresse setzen
- **$FE27**: Carry gesetzt
- **$FE2A**: Adresse nach X/Y holen
- **$FE2D**: Carry gelöscht
- **$FE30**: X/Y nach Adresse setzen
- **$FE33**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE25**: carry clear?
- **$FE27**: read memtop from MEMSIZ
- **$FE2D**: store memtop in MEMSIZ

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*