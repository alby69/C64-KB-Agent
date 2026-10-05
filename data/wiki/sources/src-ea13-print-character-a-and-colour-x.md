---
id: src-ea13-print-character-a-and-colour-x
type: source
title: 'Source Summary: print character A and colour X'
aliases:
- print character A and colour X
- ea13-print-character-a-and-colour-x.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ea13-print-character-a-and-colour-x.md
  sha256: 1da3cbf12f251804cd0122c2e4aedb62f1469f7bc7023362bb4ba24b281e5466
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print character A and colour X

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ea13-print-character-a-and-colour-x.md`
**SHA256**: `1da3cbf12f251804cd0122c2e4aedb62f1469f7bc7023362bb4ba24b281e5466`

## Summary



# $EA13 — print character A and colour X

## Disassemblatura
```assembly
.EA13  A8       TAY   ; copy the character
.EA14  A9 02    LDA #$02   ; set the count to $02, usually $14 ??
.EA16  85 CD    STA $CD   ; save the cursor countdown
.EA18  20 24 EA JSR $EA24   ; calculate the pointer to colour RAM
.EA1B  98       TYA   ; get the character back
```


## Commenti

### Original Disassembly (—)
- **$EA13**: copy the character
- **$EA14**: set the count to $02, usually $14 ??
- **$EA16**: save t...
