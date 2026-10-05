---
id: src-b47d-make-string-space-a-bytes-long
type: source
title: 'Source Summary: make string space A bytes long'
aliases:
- make string space A bytes long
- b47d-make-string-space-a-bytes-long.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b47d-make-string-space-a-bytes-long.md
  sha256: b2a2c84c0ad646cb11939737ebf9f384466905c24ad060d5890422f0989fec22
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: make string space A bytes long

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b47d-make-string-space-a-bytes-long.md`
**SHA256**: `b2a2c84c0ad646cb11939737ebf9f384466905c24ad060d5890422f0989fec22`

## Summary



# $B47D — make string space A bytes long

## Disassemblatura
```assembly
.B47D  20 F4 B4 JSR $B4F4   ; make space in string memory for string A long
.B480  86 62    STX $62   ; save string pointer low byte
.B482  84 63    STY $63   ; save string pointer high byte
.B484  85 61    STA $61   ; save length
.B486  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B47D**: make space in string memory for string A long
- **$B480**: save string pointer low byte
- **$B482**: save string ...
