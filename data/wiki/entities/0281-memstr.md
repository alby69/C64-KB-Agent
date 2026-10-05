---
id: 0281-memstr
type: entity
title: Start of Basic Memory
aliases:
- Start of Basic Memory
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/0281-memstr.md
  sha256: 62565003a9dcda26bb403aa9c106036092e9ba22b020aaaf7d837af209e2eec9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-0281-memstr
---

# Start of Basic Memory



# MEMSTR — Start of Basic Memory ($0281)

## Panoramica
Il registro o area di memoria MEMSTR è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$0281` (`641` decimale)
- **Range**: `$0281`-`$0282`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Start of memory

### Commodore-64-intern-Buch (Commodore)
Nach einem Reset oder einem Kaltstart
wird dieser Zeiger auf den nächsten
freien Speicherplatz gesetzt.

### C64 Programmer's Reference Guide (Commodore)
Pointer: Bottom of Memory for O.S

### Memory Map (Jim Butterfield)
Start of Basic Memory

### Mapping the Commodore 64 (Sheldon Leemon)
When the power is first turned on, or a cold start RESET is performed,
the Kernal routine RAMTAS (64848, $FD50) sets this location to point
to address 2048 ($0800).  This indicates that this is the starting
address of user RAM.  BASIC uses this location to set its own start of
memory pointer at location 43 ($002B), and thereafter uses only its own
pointer.

The Kernal routine MEMBOT (65076, $FE34) may be used to read or set
this pointer, or these locations may be directly PEEKed or POKEd from
BASIC.

### Reference (Joe Forster / STA)
Default: $0800, 2048.

### 64'er Magazin (64'er)
Wenn der Computer eingeschaltet wird oder wenn mit einer Reset-Taste
beziehungsweise mit SYS 58260 (VC 20: SYS 58232) ein Kaltstart ausgelöst wird,
setzt das Betriebssystem diesen Zeiger auf die Adresse des ersten freien RAM-
Speicherplatzes.

Beim C 64 ist dies die Adresse 2048. Beim VC 20 hängt sie von der
Speichererweiterung ab; ohne Erweiterung ist es 4096, mit einer 3-KByte-
Erweiterung dagegen 1024, mit 8 KByte oder mehr ist die Adresse 4608.

Dieser Zeiger wird vom Basic-Übersetzer in die Speicherzelle 43 übernommen und
nur von dort weiterverwendet.

### 64map (—)
Pointer: Bottom of Memory for Operating System ($0800)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-0281-memstr]]
