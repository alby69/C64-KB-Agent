---
id: src-b79b-scan-and-get-byte-parameter
type: source
title: 'Source Summary: scan and get byte parameter'
aliases:
- scan and get byte parameter
- b79b-scan-and-get-byte-parameter.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b79b-scan-and-get-byte-parameter.md
  sha256: 1da6329cf636332224e1bbc18711f4e15728aaab1ac6f26a3ad1b8f04569a433
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan and get byte parameter

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b79b-scan-and-get-byte-parameter.md`
**SHA256**: `1da6329cf636332224e1bbc18711f4e15728aaab1ac6f26a3ad1b8f04569a433`

## Summary



# $B79B — scan and get byte parameter

## Disassemblatura
```assembly
.B79B  20 73 00 JSR $0073   ; increment and scan memory
```


## Commenti

### Original Disassembly (—)
- **$B79B**: increment and scan memory

### Commodore-64-intern-Buch (Commodore)
- **$B79B**: CHRGET nächstes Zeichen holen
- **$B79E**: FRMNUM numerischen Wert nach FAC holen
- **$B7A1**: prüft auf Bereich und wandelt nach Integer
- **$B7A4**: HIGH-Byte
- **$B7A6**: ungleich null, dann 'ILLEGAL QUANTITY'
- **$B7A8**: LOW-...
