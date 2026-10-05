---
id: f31f-set-file-details-from-tablex
type: entity
title: set file details from table,X
aliases:
- set file details from table,X
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f31f-set-file-details-from-tablex.md
  sha256: 455917e882259039e931f476c8f4a5d7f10f7a44e1db59a23efdaac3c51856aa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f31f-set-file-details-from-tablex
---

# set file details from table,X



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

## References
- Source: [[src-f31f-set-file-details-from-tablex]]
