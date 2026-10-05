---
id: src-f68f-print-saving-file-name
type: source
title: 'Source Summary: print saving <file name>'
aliases:
- print saving <file name>
- f68f-print-saving-file-name.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f68f-print-saving-file-name.md
  sha256: 91142a6e275e6fd5584ac6c89b0120982bac559ab995c6f14e2615ebf536a294
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print saving <file name>

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f68f-print-saving-file-name.md`
**SHA256**: `91142a6e275e6fd5584ac6c89b0120982bac559ab995c6f14e2615ebf536a294`

## Summary



# $F68F — print saving <file name>

## Disassemblatura
```assembly
.F68F  A5 9D    LDA $9D   ; get message mode flag
.F691  10 FB    BPL $F68E   ; exit if control messages off
.F693  A0 51    LDY #$51   ; index to "SAVING "
.F695  20 2F F1 JSR $F12F   ; display kernel I/O message
.F698  4C C1 F5 JMP $F5C1   ; print file name and return
```


## Commenti

### Original Disassembly (—)
- **$F68F**: get message mode flag
- **$F691**: exit if control messages off
- **$F693**: index to "SAVING "
- *...
