---
id: src-e264-perform-cos
type: source
title: 'Source Summary: perform COS()'
aliases:
- perform COS()
- e264-perform-cos.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e264-perform-cos.md
  sha256: 4662386667c2309c537e95ac9126929a38516702534adf83712938dc4b25357e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform COS()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e264-perform-cos.md`
**SHA256**: `4662386667c2309c537e95ac9126929a38516702534adf83712938dc4b25357e`

## Summary



# $E264 — perform COS()

## Disassemblatura
```assembly
.E264  A9 E0    LDA #$E0   ; set pi/2 pointer low byte
.E266  A0 E2    LDY #$E2   ; set pi/2 pointer high byte
.E268  20 67 B8 JSR $B867   ; add (AY) to FAC1
```


## Commenti

### Original Disassembly (—)
- **$E264**: set pi/2 pointer low byte
- **$E266**: set pi/2 pointer high byte
- **$E268**: add (AY) to FAC1

### Commodore-64-intern-Buch (Commodore)
- **$E264**: Zeiger auf
- **$E266**: Konstante Pi/2
- **$E268**: zu FAC addieren

###...
