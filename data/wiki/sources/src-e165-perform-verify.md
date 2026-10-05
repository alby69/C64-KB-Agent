---
id: src-e165-perform-verify
type: source
title: 'Source Summary: perform VERIFY'
aliases:
- perform VERIFY
- e165-perform-verify.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e165-perform-verify.md
  sha256: 2dd9d874487670198dc432ff84997978c97b21b3dbe84d73428500e47b0146a4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform VERIFY

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e165-perform-verify.md`
**SHA256**: `2dd9d874487670198dc432ff84997978c97b21b3dbe84d73428500e47b0146a4`

## Summary



# $E165 — perform VERIFY

## Disassemblatura
```assembly
.E165  A9 01    LDA #$01   ; flag verify
.E167  2C       .BYTE $2C   ; makes next line BIT $00A9
```


## Commenti

### Original Disassembly (—)
- **$E165**: flag verify
- **$E167**: makes next line BIT $00A9

### Commodore-64-intern-Buch (Commodore)
- **$E165**: Verify-
- **$E167**: Flag

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E165**: flag verify
- **$E167**: mask
- **$E16A**: ...
