---
id: src-ac0f-perform-get
type: source
title: 'Source Summary: perform GET'
aliases:
- perform GET
- ac0f-perform-get.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/ac0f-perform-get.md
  sha256: 782dd3af461ee1e30fa4090f2ea60bd8cce7601e0022c38dbd3e979baa48a62b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform GET

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/ac0f-perform-get.md`
**SHA256**: `782dd3af461ee1e30fa4090f2ea60bd8cce7601e0022c38dbd3e979baa48a62b`

## Summary



# $AC0F — perform GET

## Disassemblatura
```assembly
.AC0F  85 11    STA $11   ; set input mode flag, $00 = INPUT, $40 = GET, $98 = READ
.AC11  86 43    STX $43   ; save READ pointer low byte
.AC13  84 44    STY $44   ; save READ pointer high byte READ, GET or INPUT next variable from list
.AC15  20 8B B0 JSR $B08B   ; get variable address
.AC18  85 49    STA $49   ; save address low byte
.AC1A  84 4A    STY $4A   ; save address high byte
.AC1C  A5 7A    LDA $7A   ; get BASIC execute pointer ...
