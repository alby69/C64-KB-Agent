---
id: src-b1aa-convert-float-to-fixed
type: source
title: 'Source Summary: convert float to fixed'
aliases:
- convert float to fixed
- b1aa-convert-float-to-fixed.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b1aa-convert-float-to-fixed.md
  sha256: ca25819677e74261fe8cb4cd9987294774b75b67b289626af2ca6a80eb1c1ed4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: convert float to fixed

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b1aa-convert-float-to-fixed.md`
**SHA256**: `ca25819677e74261fe8cb4cd9987294774b75b67b289626af2ca6a80eb1c1ed4`

## Summary



# $B1AA — convert float to fixed

## Disassemblatura
```assembly
.B1AA  20 BF B1 JSR $B1BF   ; evaluate integer expression, no sign check
.B1AD  A5 64    LDA $64   ; get result low byte
.B1AF  A4 65    LDY $65   ; get result high byte
.B1B1  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B1AA**: evaluate integer expression, no sign check
- **$B1AD**: get result low byte
- **$B1AF**: get result high byte

### Commodore-64-intern-Buch (Commodore)
- **$B1AA**: FAC nach Integer ...
