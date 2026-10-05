---
id: src-e10c-output-character-to-channel-with-error-check
type: source
title: 'Source Summary: output character to channel with error check'
aliases:
- output character to channel with error check
- e10c-output-character-to-channel-with-error-check.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e10c-output-character-to-channel-with-error-check.md
  sha256: 788f185f7ed82f8f65094577ff967c748b8189a79e79a6d20aad53bb428e7dc6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: output character to channel with error check

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e10c-output-character-to-channel-with-error-check.md`
**SHA256**: `788f185f7ed82f8f65094577ff967c748b8189a79e79a6d20aad53bb428e7dc6`

## Summary



# $E10C — output character to channel with error check

## Disassemblatura
```assembly
.E10C  20 D2 FF JSR $FFD2   ; output character to channel
.E10F  B0 E8    BCS $E0F9   ; if error go handle BASIC I/O error
.E111  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E10C**: output character to channel
- **$E10F**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E10C**: ein Zeichen ausgeben
- **$E10F**: Fehler ?
- **$E111**: Rücksprung

### Magn...
