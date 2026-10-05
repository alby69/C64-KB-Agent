---
id: src-reu-detect
type: source
title: 'Source Summary: REU Detect'
aliases:
- REU Detect
- reu_detect.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/reu_detect.md
  sha256: 04d10d9926331edcb813f55a07706058c8c52e42c7734bbc99a2b2df93ab2c01
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: REU Detect

**Raw Source File**: `data/docs/codebase_c64_org/base/reu_detect.md`
**SHA256**: `04d10d9926331edcb813f55a07706058c8c52e42c7734bbc99a2b2df93ab2c01`

## Summary



# REU Detect

base:reu_detect

                # REU Detect

```
;ACME 0.97
 
!addr   reu_command     = $df01
    REUCOMMAND_STASH    = $90   ; immediately, no reload
    REUCOMMAND_FETCH    = $91   ; immediately, no reload
!addr {
    reu_c64addr_lo      = $df02
    reu_c64addr_hi      = $df03
    reu_extaddr_lo      = $df04
    reu_extaddr_hi      = $df05
    reu_extaddr_bank    = $df06
    reu_len_lo      = $df07
    reu_len_hi      = $df08
}
; returns:
;   Carry = 0, A = 0    NO REU detect...
