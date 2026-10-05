---
id: src-e4ad-open-channel-for-output
type: source
title: 'Source Summary: open channel for output'
aliases:
- open channel for output
- e4ad-open-channel-for-output.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4ad-open-channel-for-output.md
  sha256: 7f261316100a449ef7657ed2de32942129231e7bd25f8cab200aff92b471747d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: open channel for output

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e4ad-open-channel-for-output.md`
**SHA256**: `7f261316100a449ef7657ed2de32942129231e7bd25f8cab200aff92b471747d`

## Summary



# $E4AD — open channel for output

## Disassemblatura
```assembly
.E4AD  48       PHA   ; save the flag byte
.E4AE  20 C9 FF JSR $FFC9   ; open channel for output
.E4B1  AA       TAX   ; copy the returned flag byte
.E4B2  68       PLA   ; restore the calling flag byte
.E4B3  90 01    BCC $E4B6   ; if there is no error skip copying the error flag
.E4B5  8A       TXA   ; else copy the error flag
.E4B6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E4AD**: save the flag byte
-...
