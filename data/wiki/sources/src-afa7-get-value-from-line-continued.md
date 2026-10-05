---
id: src-afa7-get-value-from-line-continued
type: source
title: 'Source Summary: get value from line continued'
aliases:
- get value from line continued
- afa7-get-value-from-line-continued.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/afa7-get-value-from-line-continued.md
  sha256: 10a268d880e9d2e72531b420d7cb94eb51b2d6d94f6a861573185a51499e56dc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: get value from line continued

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/afa7-get-value-from-line-continued.md`
**SHA256**: `10a268d880e9d2e72531b420d7cb94eb51b2d6d94f6a861573185a51499e56dc`

## Summary



# $AFA7 — get value from line continued

## Disassemblatura
```assembly
.AFA7  0A       ASL   ; *2 (2 bytes per function address)
.AFA8  48       PHA   ; save function offset
.AFA9  AA       TAX   ; copy function offset
.AFAA  20 73 00 JSR $0073   ; increment and scan memory
.AFAD  E0 8F    CPX #$8F   ; compare function offset to CHR$ token offset+1
.AFAF  90 20    BCC $AFD1   ; branch if < LEFT$ (can not be =) get value from line .. continued was LEFT$, RIGHT$ or MID$ so..
.AFB1  20 FA AE JSR...
