---
id: src-e59a-this-code-is-unused-by-kernel
type: source
title: 'Source Summary: this code is unused by kernel'
aliases:
- this code is unused by kernel
- e59a-this-code-is-unused-by-kernel.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e59a-this-code-is-unused-by-kernel.md
  sha256: e7b50ca27fc74caaa4cf8b23d7610797cddeba9e6c4980c48e92198b1f711fde
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: this code is unused by kernel

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e59a-this-code-is-unused-by-kernel.md`
**SHA256**: `e7b50ca27fc74caaa4cf8b23d7610797cddeba9e6c4980c48e92198b1f711fde`

## Summary



# $E59A — this code is unused by kernel

## Disassemblatura
```assembly
.E59A  20 A0 E5 JSR $E5A0
.E59D  4C 66 E5 JMP $E566
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E59A**: set I/O defaults
- **$E59D**: home cursor and exit routine
- **$E5A2**: DFLTO, default output device - screen
- **$E5A6**: DFLTN, default input device - keyboard
- **$E5AA**: VIC chip setup table
- **$E5AD**: VIC chip I/O registers
- **$E5B0**: nex...
