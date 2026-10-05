---
id: src-ballon-demo-from-manual
type: source
title: 'Source Summary: Balloon demo from the C64 manual'
aliases:
- Balloon demo from the C64 manual
- ballon_demo_from_manual.md
tags:
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/ballon_demo_from_manual.md
  sha256: 4cbd469fb409852b7f57bd91728d1fbdfba0ec369a6c59a2cbf48b2404a642c9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Balloon demo from the C64 manual

**Raw Source File**: `data/docs/codebase_c64_org/base/ballon_demo_from_manual.md`
**SHA256**: `4cbd469fb409852b7f57bd91728d1fbdfba0ec369a6c59a2cbf48b2404a642c9`

## Summary



# Balloon demo from the C64 manual

base:ballon_demo_from_manual

                # Balloon demo from the C64 manual

By abujok

This is the BASIC sprite example from the C64 Manual moved to machine code.

This was my first step into the world of sprites 


Have fun

;  DASM Syntax
	processor 6502
CLRSCN = $E544	; Clear Screen
VIC = $D000		; VIC Basis 53248
MIB_X2 = VIC+4		;
MIB_Y2 = VIC+5		;
MIB_Y_MSB = VIC+16
MIB_ENABLE = VIC+21 	; register Sprite Enable 53269
MIB_POINTER = $07F8	; Memory po...
