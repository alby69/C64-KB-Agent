---
id: src-swapping-zp-data
type: source
title: 'Source Summary: Swapping ZeroPage data'
aliases:
- Swapping ZeroPage data
- swapping_zp_data.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/swapping_zp_data.md
  sha256: e7dbcced7cd59e5a9201ebba8483a28246e3360bc703a8e2b37b3bbe97ee3321
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Swapping ZeroPage data

**Raw Source File**: `data/docs/codebase_c64_org/base/swapping_zp_data.md`
**SHA256**: `e7dbcced7cd59e5a9201ebba8483a28246e3360bc703a8e2b37b3bbe97ee3321`

## Summary



# Swapping ZeroPage data

base:swapping_zp_data

                # Swapping ZeroPage data

On some occasions you might want to save and restore ZP data. I.e. you have no time to patch a SID player, or the speedup you gain by giving several routines full ZP access is worth it. The small snippet below swaps 10 bytes from $00 on with memory in $10. It clutters X,Y and A though. Enjoy, enthusi.

   ldx #10 
loop 
   ldy $00,x 
   lda $10,x 
   sta $00,x 
   sty $10,x 
   dex 
   bpl loop

base/swa...
