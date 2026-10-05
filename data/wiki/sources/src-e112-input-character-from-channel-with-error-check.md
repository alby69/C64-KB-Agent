---
id: src-e112-input-character-from-channel-with-error-check
type: source
title: 'Source Summary: input character from channel with error check'
aliases:
- input character from channel with error check
- e112-input-character-from-channel-with-error-check.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e112-input-character-from-channel-with-error-check.md
  sha256: a5e8ccb37e4235a29dcdbad84ee085af0295c21017fbdacc9d44939917ac69f7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: input character from channel with error check

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e112-input-character-from-channel-with-error-check.md`
**SHA256**: `a5e8ccb37e4235a29dcdbad84ee085af0295c21017fbdacc9d44939917ac69f7`

## Summary



# $E112 — input character from channel with error check

## Disassemblatura
```assembly
.E112  20 CF FF JSR $FFCF   ; input character from channel
.E115  B0 E2    BCS $E0F9   ; if error go handle BASIC I/O error
.E117  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E112**: input character from channel
- **$E115**: if error go handle BASIC I/O error

### Commodore-64-intern-Buch (Commodore)
- **$E112**: ein Zeichen holen
- **$E115**: Fehler ?
- **$E117**: Rücksprung

### Magn...
