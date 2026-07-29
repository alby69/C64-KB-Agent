---
title: set file details from table,X
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
- f31f-setzt-fileparameter
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F31F
  address_end: $F32E
  symbol: set-file-details-from-tablex
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F31F**: get logical file from logical file table'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F31F**: logische Filenummer aus'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F31F**: LAT, table of active logical files'
---

# $F31F — set file details from table,X

## Disassemblatura
```assembly
.F31F  BD 59 02 LDA $0259,X   ; get logical file from logical file table
.F322  85 B8    STA $B8   ; save the logical file
.F324  BD 63 02 LDA $0263,X   ; get device number from device number table
.F327  85 BA    STA $BA   ; save the device number
.F329  BD 6D 02 LDA $026D,X   ; get secondary address from secondary address table
.F32C  85 B9    STA $B9   ; save the secondary address
.F32E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F31F**: get logical file from logical file table
- **$F322**: save the logical file
- **$F324**: get device number from device number table
- **$F327**: save the device number
- **$F329**: get secondary address from secondary address table
- **$F32C**: save the secondary address

### Commodore-64-intern-Buch (Commodore)
- **$F31F**: logische Filenummer aus
- **$F322**: Tabelle holen und speichern
- **$F324**: Geräteadresse aus Tabelle
- **$F327**: holen und speichern
- **$F329**: Sekundäradresse aus Tabelle
- **$F32C**: holen und speichern
- **$F32E**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F31F**: LAT, table of active logical files
- **$F322**: store in LA
- **$F324**: FAT, table of active device numbers
- **$F327**: store in FA
- **$F329**: SAT, table of active secondary addresses
- **$F32C**: store in SAT
- **$F32E**: return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*