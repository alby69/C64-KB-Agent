---
id: src-f5af-print-searching
type: source
title: 'Source Summary: print "Searching..."'
aliases:
- print "Searching..."
- f5af-print-searching.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f5af-print-searching.md
  sha256: 346bc5682394ffba1b22be0775471b5606c5458fbc0db122401df1bec0033c90
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: print "Searching..."

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/f5af-print-searching.md`
**SHA256**: `346bc5682394ffba1b22be0775471b5606c5458fbc0db122401df1bec0033c90`

## Summary



# $F5AF — print "Searching..."

## Disassemblatura
```assembly
.F5AF  A5 9D    LDA $9D   ; get message mode flag
.F5B1  10 1E    BPL $F5D1   ; exit if control messages off
.F5B3  A0 0C    LDY #$0C   ; index to "SEARCHING "
.F5B5  20 2F F1 JSR $F12F   ; display kernel I/O message
.F5B8  A5 B7    LDA $B7   ; get file name length
.F5BA  F0 15    BEQ $F5D1   ; exit if null name
.F5BC  A0 17    LDY #$17   ; else index to "FOR "
.F5BE  20 2F F1 JSR $F12F   ; display kernel I/O message
```


## Comme...
