---
id: src-4-ways-scroll-part-2
type: source
title: 'Source Summary: 4 ways scroll part 2'
aliases:
- 4 ways scroll part 2
- 4_ways_scroll_part_2.md
tags:
- sprite programming
- input handling
- basic
- graphics
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/4_ways_scroll_part_2.md
  sha256: 603f9a7ca90c9b7925b2ad0385d53f8ae1b3c222eada2f113bf8197c9535c5da
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 4 ways scroll part 2

**Raw Source File**: `data/docs/codebase_c64_org/base/4_ways_scroll_part_2.md`
**SHA256**: `603f9a7ca90c9b7925b2ad0385d53f8ae1b3c222eada2f113bf8197c9535c5da`

## Summary




# 4 ways scroll part 2

base:4_ways_scroll_part_2

                # 4 ways scroll part 2

```
 
;  4 Ways Scroll
;  by malcolm bamber
;  http://www.dark-well.pwp.blueyonder.co.uk/
;  Assembler Used C64ASM.EXE
; part 2
;***********
;** SETUP ** 
;***********  					     				
setup				
lda #<55296			; store colour map address
sta Ptrcolour
lda #>55296
sta Ptrcolour+1
					
lda #<sparecolour		; store spare colour map address
sta PtrSparecolour
lda #>sparecolour
sta PtrSparecolour+1
										
ld...
