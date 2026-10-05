---
id: src-e206-get-character-and-check-for-end-of-line
type: source
title: 'Source Summary: get character and check for end of line'
aliases:
- get character and check for end of line
- e206-get-character-and-check-for-end-of-line.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e206-get-character-and-check-for-end-of-line.md
  sha256: 79e3cb70585af699589198ce10bc3509dab950163a98bf9ecbceb06288c0c9d6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get character and check for end of line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e206-get-character-and-check-for-end-of-line.md`
**SHA256**: `79e3cb70585af699589198ce10bc3509dab950163a98bf9ecbceb06288c0c9d6`

## Summary



# $E206 — get character and check for end of line

## Disassemblatura
```assembly
.E206  20 79 00 JSR $0079
.E209  D0 02    BNE $E20D
.E20B  68       PLA
.E20C  68       PLA
.E20D  60       RTS
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$E206**: CHRGOT letztes Zeichen
- **$E209**: weiteres Zeichen, dann Rückkehr
- **$E20B**: sonst Rückkehr zur
- **$E20C**: übergeordneten Routine
- **$E20D**: Rücksprung
- **$E20E**: prüft auf Komma
- **$E211**: CHRGOT letztes Zeichen holen
...
