---
id: src-f32f
type: source
title: 'Source Summary: ;*'
aliases:
- ;*
- f32f.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f32f.md
  sha256: d0d614f53a829bede861a76b7ec570bfc011c157060f333e7a6822ab0d6cd07d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ;*

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f32f.md`
**SHA256**: `d0d614f53a829bede861a76b7ec570bfc011c157060f333e7a6822ab0d6cd07d`

## Summary



# $F32F — ;*

## Disassemblatura
```assembly
.F32F  A9 00    LDA #$00   ; NCLALL LDA #0
.F331  85 98    STA $98   ; STA    LDTND           ;FORGET ALL FILES
```


## Commenti

### Original Disassembly (Commodore)
- **$F32F**: NCLALL LDA #0
- **$F331**: STA    LDTND           ;FORGET ALL FILES

### Original Disassembly (—)
- **$F32F**: clear A
- **$F331**: clear the open file count

### Commodore-64-intern-Buch (Commodore)
- **$F32F**: Anzahl der offenen Files
- **$F331**: auf Null stellen

###...
