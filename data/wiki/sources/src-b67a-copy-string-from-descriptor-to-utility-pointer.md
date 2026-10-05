---
id: src-b67a-copy-string-from-descriptor-to-utility-pointer
type: source
title: 'Source Summary: copy string from descriptor to utility pointer'
aliases:
- copy string from descriptor to utility pointer
- b67a-copy-string-from-descriptor-to-utility-pointer.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b67a-copy-string-from-descriptor-to-utility-pointer.md
  sha256: 54b38d2fa09b9cd91e770f78f8a33929d359af3ce34f6871558f78adf6d33817
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: copy string from descriptor to utility pointer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b67a-copy-string-from-descriptor-to-utility-pointer.md`
**SHA256**: `54b38d2fa09b9cd91e770f78f8a33929d359af3ce34f6871558f78adf6d33817`

## Summary



# $B67A — copy string from descriptor to utility pointer

## Disassemblatura
```assembly
.B67A  A0 00    LDY #$00   ; clear index
.B67C  B1 6F    LDA ($6F),Y   ; get string length
.B67E  48       PHA   ; save it
.B67F  C8       INY   ; increment index
.B680  B1 6F    LDA ($6F),Y   ; get string pointer low byte
.B682  AA       TAX   ; copy to X
.B683  C8       INY   ; increment index
.B684  B1 6F    LDA ($6F),Y   ; get string pointer high byte
.B686  A8       TAY   ; copy to Y
.B687  68       P...
