---
id: src-e50a-readset-the-xy-cursor-position
type: source
title: 'Source Summary: read/set the x,y cursor position'
aliases:
- read/set the x,y cursor position
- e50a-readset-the-xy-cursor-position.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e50a-readset-the-xy-cursor-position.md
  sha256: 1682401b3b219f7f5f04990fd9dba04a5a3e47a92dd39b246a9f2e03110a12cb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: read/set the x,y cursor position

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e50a-readset-the-xy-cursor-position.md`
**SHA256**: `1682401b3b219f7f5f04990fd9dba04a5a3e47a92dd39b246a9f2e03110a12cb`

## Summary



# $E50A — read/set the x,y cursor position

## Disassemblatura
```assembly
.E50A  B0 07    BCS $E513   ; if read cursor go do read
.E50C  86 D6    STX $D6   ; save the cursor row
.E50E  84 D3    STY $D3   ; save the cursor column
.E510  20 6C E5 JSR $E56C   ; set the screen pointers for the cursor row, column
.E513  A6 D6    LDX $D6   ; get the cursor row
.E515  A4 D3    LDY $D3   ; get the cursor column
.E517  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E50A**: if read c...
