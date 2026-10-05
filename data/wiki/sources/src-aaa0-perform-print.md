---
id: src-aaa0-perform-print
type: source
title: 'Source Summary: perform PRINT'
aliases:
- perform PRINT
- aaa0-perform-print.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/aaa0-perform-print.md
  sha256: 7d1c89576f4af5bf2f30f32c63e12660b21a919ef52c99b91a417969327b10c5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform PRINT

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/aaa0-perform-print.md`
**SHA256**: `7d1c89576f4af5bf2f30f32c63e12660b21a919ef52c99b91a417969327b10c5`

## Summary



# $AAA0 — perform PRINT

## Disassemblatura
```assembly
.AAA0  F0 35    BEQ $AAD7   ; if nothing following just print CR/LF
.AAA2  F0 43    BEQ $AAE7   ; exit if nothing following, end of PRINT branch
.AAA4  C9 A3    CMP #$A3   ; compare with token for TAB(
.AAA6  F0 50    BEQ $AAF8   ; if TAB( go handle it
.AAA8  C9 A6    CMP #$A6   ; compare with token for SPC(
.AAAA  18       CLC   ; flag SPC(
.AAAB  F0 4B    BEQ $AAF8   ; if SPC( go handle it
.AAAD  C9 2C    CMP #$2C   ; compare with ","
....
