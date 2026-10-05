---
id: src-asm-include-file-for-basic-routines
type: source
title: 'Source Summary: base:asm_include_file_for_basic_routines [Codebase64 wiki]'
aliases:
- base:asm_include_file_for_basic_routines [Codebase64 wiki]
- asm_include_file_for_basic_routines.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/asm_include_file_for_basic_routines.md
  sha256: 86471ad02af03400621fb5b26da7cc9bce97d3e4c27356198fff243a4381aec7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:asm_include_file_for_basic_routines [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/asm_include_file_for_basic_routines.md`
**SHA256**: `86471ad02af03400621fb5b26da7cc9bce97d3e4c27356198fff243a4381aec7`

## Summary



# base:asm_include_file_for_basic_routines [Codebase64 wiki]

base:asm_include_file_for_basic_routines

                ; C64 BASIC ROM vectors
; by White Flame
;---------
; Input
; get next byte of BASIC text
chrget          = $0073
; chrget uint8 to .X (range checking)
getbytc         = $b79b
; chrget uint16 (0-63999) to $14-$15
linget          = $a96b
; chrget a float to fac1
fin             = $bcf3
; check for and skip open paren (syntax error otherwise)
chkopn          = $aefa
; check for...
