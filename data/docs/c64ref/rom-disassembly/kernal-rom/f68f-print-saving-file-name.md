---
title: print saving <file name>
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
- f68f-saving-ausgeben
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F68F
  address_end: $F698
  symbol: print-saving-file-name
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F68F**: get message mode flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F68F**: Flag für Direktmodus laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F68F**: MSGFLG'
---

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