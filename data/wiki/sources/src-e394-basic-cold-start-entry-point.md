---
id: src-e394-basic-cold-start-entry-point
type: source
title: 'Source Summary: BASIC cold start entry point'
aliases:
- BASIC cold start entry point
- e394-basic-cold-start-entry-point.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e394-basic-cold-start-entry-point.md
  sha256: c372f103f2e436539c06cee261c56d64d1cd36e4956efbc3c57c1d0ab267a9f4
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BASIC cold start entry point

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e394-basic-cold-start-entry-point.md`
**SHA256**: `c372f103f2e436539c06cee261c56d64d1cd36e4956efbc3c57c1d0ab267a9f4`

## Summary



# $E394 — BASIC cold start entry point

## Disassemblatura
```assembly
.E394  20 53 E4 JSR $E453   ; initialise the BASIC vector table
.E397  20 BF E3 JSR $E3BF   ; initialise the BASIC RAM locations
.E39A  20 22 E4 JSR $E422   ; print the start up message and initialise the memory pointers not ok ??
.E39D  A2 FB    LDX #$FB   ; value for start stack
.E39F  9A       TXS   ; set stack pointer
.E3A0  D0 E4    BNE $E386   ; do "READY." warm start, branch always
```


## Commenti

### Original Dis...
