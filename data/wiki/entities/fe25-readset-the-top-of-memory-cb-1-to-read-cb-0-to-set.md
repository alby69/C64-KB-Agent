---
id: fe25-readset-the-top-of-memory-cb-1-to-read-cb-0-to-set
type: entity
title: read/set the top of memory, Cb = 1 to read, Cb = 0 to set
aliases:
- read/set the top of memory, Cb = 1 to read, Cb = 0 to set
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe25-readset-the-top-of-memory-cb-1-to-read-cb-0-to-set.md
  sha256: a6c2c225fe85a56a70a7bd95b9b4a8a3f974ab9f12acc253403528e0c309ab78
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe25-readset-the-top-of-memory-cb-1-to-read-cb-0-to-set
---

# read/set the top of memory, Cb = 1 to read, Cb = 0 to set



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

## References
- Source: [[src-fe25-readset-the-top-of-memory-cb-1-to-read-cb-0-to-set]]
