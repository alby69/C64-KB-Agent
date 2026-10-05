---
id: src-a906-scan-for-next-basic-statement-or-eol
type: source
title: 'Source Summary: scan for next BASIC statement ([:] or [EOL])'
aliases:
- scan for next BASIC statement ([:] or [EOL])
- a906-scan-for-next-basic-statement-or-eol.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a906-scan-for-next-basic-statement-or-eol.md
  sha256: d17f58f488e7219a125f4161822bf8e15504059e820a47676d3ff51347be5ce5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan for next BASIC statement ([:] or [EOL])

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a906-scan-for-next-basic-statement-or-eol.md`
**SHA256**: `d17f58f488e7219a125f4161822bf8e15504059e820a47676d3ff51347be5ce5`

## Summary



# $A906 — scan for next BASIC statement ([:] or [EOL])

## Disassemblatura
```assembly
.A906  A2 3A    LDX #$3A   ; set look for character = ":"
.A908  2C       .BYTE $2C   ; makes next line BIT $00A2
```


## Commenti

### Original Disassembly (—)
- **$A906**: set look for character = ":"
- **$A908**: makes next line BIT $00A2

### Commodore-64-intern-Buch (Commodore)
- **$A906**: ':' Doppelpunkt
- **$A909**: $0 Zeilenende
- **$A90B**: als Suchzeichen
- **$A90D**: Zähler
- **$A90F**: initiali...
