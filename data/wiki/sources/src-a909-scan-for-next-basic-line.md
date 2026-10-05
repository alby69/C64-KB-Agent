---
id: src-a909-scan-for-next-basic-line
type: source
title: 'Source Summary: scan for next BASIC line'
aliases:
- scan for next BASIC line
- a909-scan-for-next-basic-line.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a909-scan-for-next-basic-line.md
  sha256: d87a2fa6c0824db75aa27ce22b6f6f9e52935c0a85c3bb3a2cc8323749f9ad63
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan for next BASIC line

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a909-scan-for-next-basic-line.md`
**SHA256**: `d87a2fa6c0824db75aa27ce22b6f6f9e52935c0a85c3bb3a2cc8323749f9ad63`

## Summary



# $A909 — scan for next BASIC line

## Disassemblatura
```assembly
.A909  A2 00    LDX #$00   ; set alternate search character = [EOL]
.A90B  86 07    STX $07   ; store alternate search character
.A90D  A0 00    LDY #$00   ; set search character = [EOL]
.A90F  84 08    STY $08   ; save the search character
.A911  A5 08    LDA $08   ; get search character
.A913  A6 07    LDX $07   ; get alternate search character
.A915  85 07    STA $07   ; make search character = alternate search character
.A9...
