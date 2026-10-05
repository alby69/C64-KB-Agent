---
id: src-f31f-set-file-details-from-tablex
type: source
title: 'Source Summary: set file details from table,X'
aliases:
- set file details from table,X
- f31f-set-file-details-from-tablex.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f31f-set-file-details-from-tablex.md
  sha256: 455917e882259039e931f476c8f4a5d7f10f7a44e1db59a23efdaac3c51856aa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set file details from table,X

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f31f-set-file-details-from-tablex.md`
**SHA256**: `455917e882259039e931f476c8f4a5d7f10f7a44e1db59a23efdaac3c51856aa`

## Summary



# $F31F — set file details from table,X

## Disassemblatura
```assembly
.F31F  BD 59 02 LDA $0259,X   ; get logical file from logical file table
.F322  85 B8    STA $B8   ; save the logical file
.F324  BD 63 02 LDA $0263,X   ; get device number from device number table
.F327  85 BA    STA $BA   ; save the device number
.F329  BD 6D 02 LDA $026D,X   ; get secondary address from secondary address table
.F32C  85 B9    STA $B9   ; save the secondary address
.F32E  60       RTS
```


## Commenti

...
