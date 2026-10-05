---
id: src-fd50-test-ram-and-find-ram-end
type: source
title: 'Source Summary: test RAM and find RAM end'
aliases:
- test RAM and find RAM end
- fd50-test-ram-and-find-ram-end.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd50-test-ram-and-find-ram-end.md
  sha256: 4372b7b890a368f35d4158c50f18ce640e05a85a234375d28f8ef646b16cba25
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: test RAM and find RAM end

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fd50-test-ram-and-find-ram-end.md`
**SHA256**: `4372b7b890a368f35d4158c50f18ce640e05a85a234375d28f8ef646b16cba25`

## Summary



# $FD50 — test RAM and find RAM end

## Disassemblatura
```assembly
.FD50  A9 00    LDA #$00   ; clear A
.FD52  A8       TAY   ; clear index
.FD53  99 02 00 STA $0002,Y   ; clear page 0, don't do $0000 or $0001
.FD56  99 00 02 STA $0200,Y   ; clear page 2
.FD59  99 00 03 STA $0300,Y   ; clear page 3
.FD5C  C8       INY   ; increment index
.FD5D  D0 F4    BNE $FD53   ; loop if more to do
.FD5F  A2 3C    LDX #$3C   ; set cassette buffer pointer low byte
.FD61  A0 03    LDY #$03   ; set cassette ...
