---
id: fe43-nmi-vector
type: entity
title: NMI vector
aliases:
- NMI vector
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fe43-nmi-vector.md
  sha256: b9245a51b463e3808d59bf859694e3ae06b8873d49c1b1e96b97c440f8ddb89c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-fe43-nmi-vector
---

# NMI vector



# $FE43 — NMI vector

## Disassemblatura
```assembly
.FE43  78       SEI   ; disable the interrupts
.FE44  6C 18 03 JMP ($0318)   ; do NMI vector
```


## Commenti

### Original Disassembly (—)
- **$FE43**: disable the interrupts
- **$FE44**: do NMI vector

### Commodore-64-intern-Buch (Commodore)
- **$FE43**: Interrupt setzen
- **$FE44**: JMP $FE47, NMI-Vektor
- **$FE47**: Akku auf Stapel retten
- **$FE48**: X nach Akku
- **$FE49**: X retten
- **$FE4A**: Y nach Akku
- **$FE4B**: Y retten
- **$FE4C**: Wert laden
- **$FE4E**: NMI-Möglichkeiten löschen
- **$FE51**: Flags lesen und löschen
- **$FE54**: RS 232 aktiv ?
- **$FE56**: Prüft auf ROM-Modul in $8000
- **$FE59**: nein: weiter
- **$FE5B**: ja: Sprung auf Modul-NMI
- **$FE5E**: Flag für Stop-Taste setzen
- **$FE61**: Stop-Taste abfragen
- **$FE64**: nicht gedrückt ?
- **$FE66**: Standard-Vektoren für Interrupt und I/O setzen
- **$FE69**: I/O initialisieren
- **$FE6C**: Bildschirmreset
- **$FE6F**: zum BASIC-Warmstart

### Marko Mäkelä (Marko Mäkelä)
- **$FE44**: normally FE47

### Magnus Nyman (Magnus Nyman)
- **$FE43**: disable interrupts
- **$FE44**: jump to NMINV, points normally to $fe47
- **$FE47**: store (A), (X), (Y) on the stack
- **$FE4C**: CIA#2 interrupt control register
- **$FE54**: NMI caused by RS232? If so - jump
- **$FE56**: check for autostart at $8000
- **$FE5B**: Jump to warm start vector
- **$FE5E**: Scan 1 row in keymatrix and store value in $91
- **$FE61**: Check $91 to see if <STOP> was pressed
- **$FE64**: <STOP> not pressed, skip part of following routine

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-fe43-nmi-vector]]
