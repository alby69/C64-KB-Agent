---
id: src-e1c7-perform-close
type: source
title: 'Source Summary: perform CLOSE'
aliases:
- perform CLOSE
- e1c7-perform-close.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e1c7-perform-close.md
  sha256: 00996d22173c53f7b8c6b26898fba66482ab7df5f50917d6dadb600f1d6513d7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform CLOSE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e1c7-perform-close.md`
**SHA256**: `00996d22173c53f7b8c6b26898fba66482ab7df5f50917d6dadb600f1d6513d7`

## Summary



# $E1C7 — perform CLOSE

## Disassemblatura
```assembly
.E1C7  20 19 E2 JSR $E219   ; get parameters for OPEN/CLOSE
.E1CA  A5 49    LDA $49   ; get logical file number
.E1CC  20 C3 FF JSR $FFC3   ; close a specified logical file
.E1CF  90 C3    BCC $E194   ; exit if no error
.E1D1  4C F9 E0 JMP $E0F9   ; go handle BASIC I/O error
```


## Commenti

### Original Disassembly (—)
- **$E1C7**: get parameters for OPEN/CLOSE
- **$E1CA**: get logical file number
- **$E1CC**: close a specified logical...
