---
id: f68f-print-saving-file-name
type: entity
title: print saving <file name>
aliases:
- print saving <file name>
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f68f-print-saving-file-name.md
  sha256: 91142a6e275e6fd5584ac6c89b0120982bac559ab995c6f14e2615ebf536a294
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f68f-print-saving-file-name
---

# print saving <file name>



# $F68F — print saving <file name>

## Disassemblatura
```assembly
.F68F  A5 9D    LDA $9D   ; get message mode flag
.F691  10 FB    BPL $F68E   ; exit if control messages off
.F693  A0 51    LDY #$51   ; index to "SAVING "
.F695  20 2F F1 JSR $F12F   ; display kernel I/O message
.F698  4C C1 F5 JMP $F5C1   ; print file name and return
```


## Commenti

### Original Disassembly (—)
- **$F68F**: get message mode flag
- **$F691**: exit if control messages off
- **$F693**: index to "SAVING "
- **$F695**: display kernel I/O message
- **$F698**: print file name and return

### Commodore-64-intern-Buch (Commodore)
- **$F68F**: Flag für Direktmodus laden
- **$F691**: Bit 7 gelöscht, dann Programm-Mode
- **$F693**: Offset für 'SAVING'
- **$F695**: Meldung ausgeben
- **$F698**: Filenamen ausgeben, Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F68F**: MSGFLG
- **$F691**: not in direct mode, exit
- **$F693**: offset to message in table
- **$F695**: output 'SAVING'
- **$F698**: output filename

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f68f-print-saving-file-name]]
