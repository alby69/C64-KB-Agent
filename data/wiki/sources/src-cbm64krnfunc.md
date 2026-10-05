---
id: src-cbm64krnfunc
type: source
title: 'Source Summary: Commodore 64 standard KERNAL functions'
aliases:
- Commodore 64 standard KERNAL functions
- cbm64krnfunc.md
tags:
- memory management
- graphics
- basic
- input handling
- sprite programming
- assembly
sources:
- path: data/docs/sta_c64_org/cbm64krnfunc.md
  sha256: dc68d866e676c203678b7c78c373105b4eb7b0d20cbd6acbd458a76bbfeb4ac8
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Commodore 64 standard KERNAL functions

**Raw Source File**: `data/docs/sta_c64_org/cbm64krnfunc.md`
**SHA256**: `dc68d866e676c203678b7c78c373105b4eb7b0d20cbd6acbd458a76bbfeb4ac8`

## Summary




# Commodore 64 standard KERNAL functions

| **Address** | Function | 
|---|---|
| $FF81 | SCINIT. Initialize   VIC; restore default input/output to keyboard/screen; clear screen; set   PAL/NTSC switch and interrupt timer. Input: – Output: – Used registers: A, X, Y. Real address: $FF5B. | 
| $FF84 | IOINIT. Initialize CIA's, SID volume;   setup memory configuration; set and start interrupt timer. Input: – Output: – Used registers: A, X. Real address: $FDA3. | 
| $FF87 | RAMTAS. Clear memory ad...
