---
id: src-detect-cpu-type
type: source
title: 'Source Summary: base:detect_cpu_type [Codebase64 wiki]'
aliases:
- base:detect_cpu_type [Codebase64 wiki]
- detect_cpu_type.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/detect_cpu_type.md
  sha256: 77cf528f79665ad5898a718125de4583dd7bbb5705de00259cce8051288b75f0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:detect_cpu_type [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/detect_cpu_type.md`
**SHA256**: `77cf528f79665ad5898a718125de4583dd7bbb5705de00259cce8051288b75f0`

## Summary



# base:detect_cpu_type [Codebase64 wiki]

base:detect_cpu_type

                ```
; ---------------------------------------------------------------------------
; Subroutine to detect an 816. Returns
;
;   - carry clear and 0 in A for a NMOS 6502 CPU
;   - carry set and 1 in A for CMOS 6502 CPUs
;   - carry set and 2 in A for a 65816
;
; This function uses a $1A opcode which is a INA on the 816 and C02, and
; ignored (interpreted as a NOP) on a NMOS 6502. Detection of the 65816 is
; done by t...
