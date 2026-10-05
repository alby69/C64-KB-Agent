---
id: src-e891-output-cr
type: source
title: 'Source Summary: output [CR]'
aliases:
- output [CR]
- e891-output-cr.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e891-output-cr.md
  sha256: 34afcce73e674a43a51701c836c9ec06307e0b218741b9559e79308fcc378acc
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: output [CR]

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e891-output-cr.md`
**SHA256**: `34afcce73e674a43a51701c836c9ec06307e0b218741b9559e79308fcc378acc`

## Summary



# $E891 — output [CR]

## Disassemblatura
```assembly
.E891  A2 00    LDX #$00   ; clear X
.E893  86 D8    STX $D8   ; clear the insert count
.E895  86 C7    STX $C7   ; clear the reverse flag
.E897  86 D4    STX $D4   ; clear the cursor quote flag, $xx = quote, $00 = no quote
.E899  86 D3    STX $D3   ; save the cursor column
.E89B  20 7C E8 JSR $E87C   ; do newline
.E89E  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
```


## Commenti

### Original Disassembly (—)...
