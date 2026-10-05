---
id: src-b606-continuation-of-garbage-clean-up
type: source
title: 'Source Summary: continuation of garbage clean up'
aliases:
- continuation of garbage clean up
- b606-continuation-of-garbage-clean-up.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b606-continuation-of-garbage-clean-up.md
  sha256: 8f36b64b25e8e73c16728a7663827fe9d2e4c99dec7a9e61227ece6c263b33b8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: continuation of garbage clean up

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b606-continuation-of-garbage-clean-up.md`
**SHA256**: `8f36b64b25e8e73c16728a7663827fe9d2e4c99dec7a9e61227ece6c263b33b8`

## Summary



# $B606 — continuation of garbage clean up

## Disassemblatura
```assembly
.B606  A5 4F    LDA $4F
.B608  05 4E    ORA $4E
.B60A  F0 F5    BEQ $B601
.B60C  A5 55    LDA $55
.B60E  29 04    AND #$04
.B610  4A       LSR
.B611  A8       TAY
.B612  85 55    STA $55
.B614  B1 4E    LDA ($4E),Y
.B616  65 5F    ADC $5F
.B618  85 5A    STA $5A
.B61A  A5 60    LDA $60
.B61C  69 00    ADC #$00
.B61E  85 5B    STA $5B
.B620  A5 33    LDA $33
.B622  A6 34    LDX $34
.B624  85 58    STA $58
.B626  86 59   ...
