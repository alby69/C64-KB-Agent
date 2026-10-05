---
id: src-4-ways-scroll-part-1
type: source
title: 'Source Summary: 4 ways scroll part 1'
aliases:
- 4 ways scroll part 1
- 4_ways_scroll_part_1.md
tags:
- sprite programming
- input handling
- basic
- graphics
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/4_ways_scroll_part_1.md
  sha256: f50e8e4ae7d8093ef4406245ebf2ce29d2cecd618b75c4a07a819cd84fa10e4d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 4 ways scroll part 1

**Raw Source File**: `data/docs/codebase_c64_org/base/4_ways_scroll_part_1.md`
**SHA256**: `f50e8e4ae7d8093ef4406245ebf2ce29d2cecd618b75c4a07a819cd84fa10e4d`

## Summary




# 4 ways scroll part 1

base:4_ways_scroll_part_1

                # 4 ways scroll part 1

```
 
;  4 Ways Scroll
;  by malcolm bamber
;  http://www.dark-well.pwp.blueyonder.co.uk/
;  Assembler Used C64ASM.EXE
.word $0801 		; Starting address for loader
* = $0801
.word nextLine 		; Line link
.word $0 	        ; Line number
.byte 158 		; SYS
.byte '1','4','5','0','0'						
.byte 0
nextLine .byte 0,0 	; end of basic
* = 14500   
asemcode       		
     		
Ptrhiddenscreen	        = $2b		; hidden ...
