---
id: src-e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards
type: source
title: 'Source Summary: BASIC vectors, these are copied to RAM from $0300 onwards'
aliases:
- BASIC vectors, these are copied to RAM from $0300 onwards
- e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards.md
  sha256: 612bde02f858903e0886a5c95897a373825fa2e19f4aa5153dad246c79e4f2b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: BASIC vectors, these are copied to RAM from $0300 onwards

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards.md`
**SHA256**: `612bde02f858903e0886a5c95897a373825fa2e19f4aa5153dad246c79e4f2b3`

## Summary



# $E447 — BASIC vectors, these are copied to RAM from $0300 onwards

## Disassemblatura
```assembly
.E447  8B E3   ; error message          $0300
.E449  83 A4   ; BASIC warm start       $0302
.E44B  7C A5   ; crunch BASIC tokens    $0304
.E44D  1A A7   ; uncrunch BASIC tokens  $0306
.E44F  E4 A7   ; start new BASIC code   $0308
.E451  86 AE   ; get arithmetic element $030A
```


## Commenti

### Original Disassembly (—)
- **$E447**: error message          $0300
- **$E449**: BASIC warm start   ...
