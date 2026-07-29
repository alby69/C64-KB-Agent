---
title: NMI vector
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
- fe43-nmi-einsprung
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE43
  address_end: $FE44
  symbol: nmi-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE43**: disable the interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE43**: Interrupt setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FE44**: normally FE47'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE43**: disable interrupts'
---

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