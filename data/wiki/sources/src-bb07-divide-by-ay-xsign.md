---
id: src-bb07-divide-by-ay-xsign
type: source
title: 'Source Summary: divide by (AY) (X=sign)'
aliases:
- divide by (AY) (X=sign)
- bb07-divide-by-ay-xsign.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bb07-divide-by-ay-xsign.md
  sha256: 86f3abb2048a561e70739605601f5580932134350631a4bb3d05a11ff5b4c730
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: divide by (AY) (X=sign)

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bb07-divide-by-ay-xsign.md`
**SHA256**: `86f3abb2048a561e70739605601f5580932134350631a4bb3d05a11ff5b4c730`

## Summary



# $BB07 — divide by (AY) (X=sign)

## Disassemblatura
```assembly
.BB07  86 6F    STX $6F   ; save sign compare (FAC1 EOR FAC2)
.BB09  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.BB0C  4C 12 BB JMP $BB12   ; do FAC2/FAC1 Perform divide-by
```


## Commenti

### Original Disassembly (—)
- **$BB07**: save sign compare (FAC1 EOR FAC2)
- **$BB09**: unpack memory (AY) into FAC1
- **$BB0C**: do FAC2/FAC1 Perform divide-by

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BB0C**: DIVIDE AR...
