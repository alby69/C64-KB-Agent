---
id: 00bf-mych
type: entity
title: Serial word buffer
aliases:
- Serial word buffer
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/00bf-mych.md
  sha256: da4cd9d4b211d54b6b3e9e908ab12c0f6f7a48fbbf05b363e77d779736b05d8d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-00bf-mych
---

# Serial word buffer



# MYCH — Serial word buffer ($00BF)

## Panoramica
Il registro o area di memoria MYCH è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$00BF` (`191` decimale)
- **Range**: `$00BF`
- **Dimensione**: `1 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)
Cassette: holds input byte being built

### Commodore-64-intern-Buch (Commodore)
Beim Laden eines Programms von Band
wird diese Speicherzelle dazu benutzt,
um die einzelnen Bits zu einem Byte
zusammenzusetzen.

### C64 Programmer's Reference Guide (Commodore)
Serial Word Buffer

### Memory Map (Jim Butterfield)
Serial word buffer

### Mapping the Commodore 64 (Sheldon Leemon)
This is used by the tape routines as a work area in which incoming
characters area assembled.

### Reference (Joe Forster / STA)
Unknown

### 64'er Magazin (64'er)
Diese Speicherzelle wird beim Laden eines Programms vom Band dazu benutzt, um
Zeichen aus einzelnen Bits zusammenzusetzen.

### 64map (—)
Serial Word Buffer

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-00bf-mych]]
