---
id: 032c-iclall
type: entity
title: Abort I/o vector ($F32F)
aliases:
- Abort I/o vector ($F32F)
tags:
- rom-layout
- zero-page
- memory-map
sources:
- path: data/docs/c64ref/memory-map/032c-iclall.md
  sha256: 147c4d79e603ca6a5f148f0f6b8c2edb7af19ff01f84da7f76acd9b15d9a1db8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-032c-iclall
---

# Abort I/o vector ($F32F)



# ICLALL — Abort I/o vector ($F32F) ($032C)

## Panoramica
Il registro o area di memoria ICLALL è descritto in dettaglio di seguito.

## Dettagli Tecnici
- **Indirizzo**: `$032C` (`812` decimale)
- **Range**: `$032C`-`$032D`
- **Dimensione**: `2 byte`
- **Permessi**: `R/W`

## Descrizioni per Fonte

### Original Source Comments (Microsoft/Commodore)


### Commodore-64-intern-Buch (Commodore)
$F32F CLALL-Vektor

### C64 Programmer's Reference Guide (Commodore)
KERNAL CLALL Routine Vector

### Memory Map (Jim Butterfield)
Abort I/o vector ($F32F)

### Mapping the Commodore 64 (Sheldon Leemon)
Vector to Kernal CLALL Routine (Currently at 62255 ($F32F))

### Reference (Joe Forster / STA)
Default: $F32F.

### 64'er Magazin (64'er)
CLALL ist die Abkürzung für Close ALL (Channels and Files). Diese Routine, die
ab Adresse 62255 ($F32F) - beim VC 20 ab 62447 ($F3EF) - beginnt, setzt die
Speicherzelle 152 auf 0 und schließt so zwangsläufig alle Dateien und Kanäle.

### 64map (—)
Vector: Indirect entry to Kernal CLALL Routine ($F32F)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-032c-iclall]]
