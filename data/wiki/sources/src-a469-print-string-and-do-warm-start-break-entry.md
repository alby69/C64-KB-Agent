---
id: src-a469-print-string-and-do-warm-start-break-entry
type: source
title: 'Source Summary: print string and do warm start, break entry'
aliases:
- print string and do warm start, break entry
- a469-print-string-and-do-warm-start-break-entry.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a469-print-string-and-do-warm-start-break-entry.md
  sha256: 2612332d97f9325023d7e83883700eefa15ff41c496f4a844b6b3ca626d309be
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print string and do warm start, break entry

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a469-print-string-and-do-warm-start-break-entry.md`
**SHA256**: `2612332d97f9325023d7e83883700eefa15ff41c496f4a844b6b3ca626d309be`

## Summary



# $A469 — print string and do warm start, break entry

## Disassemblatura
```assembly
.A469  20 1E AB JSR $AB1E   ; print null terminated string
.A46C  A4 3A    LDY $3A   ; get current line number high byte
.A46E  C8       INY   ; increment it
.A46F  F0 03    BEQ $A474   ; branch if was in immediate mode
.A471  20 C2 BD JSR $BDC2   ; do " IN " line number message
```


## Commenti

### Original Disassembly (—)
- **$A469**: print null terminated string
- **$A46C**: get current line number high ...
