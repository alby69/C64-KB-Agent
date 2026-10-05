---
id: src-fdf9-set-filename
type: source
title: 'Source Summary: set filename'
aliases:
- set filename
- fdf9-set-filename.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fdf9-set-filename.md
  sha256: d8b86ddb6d06394154fb62981098549c905da8715c08d3e1f774a341d505ef59
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set filename

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fdf9-set-filename.md`
**SHA256**: `d8b86ddb6d06394154fb62981098549c905da8715c08d3e1f774a341d505ef59`

## Summary



# $FDF9 — set filename

## Disassemblatura
```assembly
.FDF9  85 B7    STA $B7   ; set file name length
.FDFB  86 BB    STX $BB   ; set file name pointer low byte
.FDFD  84 BC    STY $BC   ; set file name pointer high byte
.FDFF  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FDF9**: set file name length
- **$FDFB**: set file name pointer low byte
- **$FDFD**: set file name pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$FDF9**: Länge speichern
- **$FDFB**: ...
