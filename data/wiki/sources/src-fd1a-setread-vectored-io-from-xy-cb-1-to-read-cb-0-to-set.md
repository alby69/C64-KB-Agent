---
id: src-fd1a-setread-vectored-io-from-xy-cb-1-to-read-cb-0-to-set
type: source
title: 'Source Summary: set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to
  set'
aliases:
- set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set
- fd1a-setread-vectored-io-from-xy-cb-1-to-read-cb-0-to-set.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/fd1a-setread-vectored-io-from-xy-cb-1-to-read-cb-0-to-set.md
  sha256: 0be140eaf2137acda37af70ec04a993dba3045cf1f8a6a39bfd1fac0aceb861c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/fd1a-setread-vectored-io-from-xy-cb-1-to-read-cb-0-to-set.md`
**SHA256**: `0be140eaf2137acda37af70ec04a993dba3045cf1f8a6a39bfd1fac0aceb861c`

## Summary



# $FD1A — set/read vectored I/O from (XY), Cb = 1 to read, Cb = 0 to set

## Disassemblatura
```assembly
.FD1A  86 C3    STX $C3   ; save pointer low byte
.FD1C  84 C4    STY $C4   ; save pointer high byte
.FD1E  A0 1F    LDY #$1F   ; set byte count
.FD20  B9 14 03 LDA $0314,Y   ; read vector byte from vectors
.FD23  B0 02    BCS $FD27   ; branch if read vectors
.FD25  B1 C3    LDA ($C3),Y   ; read vector byte from (XY)
.FD27  91 C3    STA ($C3),Y   ; save byte to (XY)
.FD29  99 14 03 STA $031...
