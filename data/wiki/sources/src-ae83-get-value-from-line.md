---
id: src-ae83-get-value-from-line
type: source
title: 'Source Summary: get value from line'
aliases:
- get value from line
- ae83-get-value-from-line.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ae83-get-value-from-line.md
  sha256: d45d0ca977215d23c07c5d1cac71aaf4dbe041990df557f7dcae9a290fe1b283
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get value from line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ae83-get-value-from-line.md`
**SHA256**: `d45d0ca977215d23c07c5d1cac71aaf4dbe041990df557f7dcae9a290fe1b283`

## Summary



# $AE83 — get value from line

## Disassemblatura
```assembly
.AE83  6C 0A 03 JMP ($030A)   ; get arithmetic element
```


## Commenti

### Original Disassembly (—)
- **$AE83**: get arithmetic element

### Commodore-64-intern-Buch (Commodore)
- **$AE83**: JMP $AE86
- **$AE86**: Wert laden und damit
- **$AE88**: Typflag auf numerisch setzen
- **$AE8A**: CHRGET nächstes Zeichen holen
- **$AE8D**: Ziffer? nein: $AE92
- **$AE8F**: Variable nach FAC holen
- **$AE92**: Buchstabe?
- **$AE95**: nein: ...
