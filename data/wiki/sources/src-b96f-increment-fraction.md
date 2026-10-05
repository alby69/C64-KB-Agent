---
id: src-b96f-increment-fraction
type: source
title: 'Source Summary: increment fraction'
aliases:
- increment fraction
- b96f-increment-fraction.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b96f-increment-fraction.md
  sha256: be3c6ccfc5f4e27979315b55d53e9bbe04a6c7789dd8caa09d4dd9067f300bad
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: increment fraction

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b96f-increment-fraction.md`
**SHA256**: `be3c6ccfc5f4e27979315b55d53e9bbe04a6c7789dd8caa09d4dd9067f300bad`

## Summary



# $B96F — increment fraction

## Disassemblatura
```assembly
.B96F  E6 65    INC $65
.B971  D0 0A    BNE $B97D
.B973  E6 64    INC $64
.B975  D0 06    BNE $B97D
.B977  E6 63    INC $63
.B979  D0 02    BNE $B97D
.B97B  E6 62    INC $62
.B97D  60       RTS
.B97E  A2 0F    LDX #$0F   ; error number
.B980  4C 37 A4 JMP $A437
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
- **$B97E**: error number

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B96F**: ADD CARRY FROM EXTRA

---
*Fonte: [c64...
