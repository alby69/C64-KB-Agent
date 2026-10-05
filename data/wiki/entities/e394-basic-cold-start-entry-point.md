---
id: e394-basic-cold-start-entry-point
type: entity
title: BASIC cold start entry point
aliases:
- BASIC cold start entry point
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e394-basic-cold-start-entry-point.md
  sha256: c372f103f2e436539c06cee261c56d64d1cd36e4956efbc3c57c1d0ab267a9f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e394-basic-cold-start-entry-point
---

# BASIC cold start entry point



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

## References
- Source: [[src-e394-basic-cold-start-entry-point]]
