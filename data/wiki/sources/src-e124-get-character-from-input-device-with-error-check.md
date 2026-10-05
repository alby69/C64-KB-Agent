---
id: src-e124-get-character-from-input-device-with-error-check
type: source
title: 'Source Summary: get character from input device with error check'
aliases:
- get character from input device with error check
- e124-get-character-from-input-device-with-error-check.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e124-get-character-from-input-device-with-error-check.md
  sha256: 140b403cb1067139b0224d652c5efb4d50869489c138935a0659df4b562af62a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get character from input device with error check

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e124-get-character-from-input-device-with-error-check.md`
**SHA256**: `140b403cb1067139b0224d652c5efb4d50869489c138935a0659df4b562af62a`

## Summary



# $E124 — get character from input device with error check

## Disassemblatura
```assembly
.E124  20 E4 FF JSR $FFE4   ; get character from input device
.E127  B0 D0    BCS $E0F9   ; if error go handle BASIC I/O error
.E129  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E124**: get character from input device
- **$E127**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E124**: ein Zeichen holen
- **$E127**: Fehler ?
- **$E129**: Rücksprung
...
