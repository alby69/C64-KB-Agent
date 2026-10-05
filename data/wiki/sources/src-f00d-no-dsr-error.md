---
id: src-f00d-no-dsr-error
type: source
title: 'Source Summary: NO DSR ERROR'
aliases:
- NO DSR ERROR
- f00d-no-dsr-error.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f00d-no-dsr-error.md
  sha256: 817960d151ac6d8c8bf4473b77139b72a07598531d853194f8f04d775aaedfa7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NO DSR ERROR

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f00d-no-dsr-error.md`
**SHA256**: `817960d151ac6d8c8bf4473b77139b72a07598531d853194f8f04d775aaedfa7`

## Summary



# $F00D — NO DSR ERROR

## Disassemblatura
```assembly
.F00D  A9 40    LDA #$40
.F00F  8D 97 02 STA $0297   ; RSSTAT, 6551 status register image
.F012  18       CLC
.F013  60       RTS
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$F00F**: RSSTAT, 6551 status register image

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
