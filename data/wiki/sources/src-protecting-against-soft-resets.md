---
id: src-protecting-against-soft-resets
type: source
title: 'Source Summary: Protecting against soft-resets'
aliases:
- Protecting against soft-resets
- protecting_against_soft-resets.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/protecting_against_soft-resets.md
  sha256: e6916baa160c38e7fa616c4f3e1aa1fdbb3dc93bd887f5cf67adbd042fb927be
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Protecting against soft-resets

**Raw Source File**: `data/docs/codebase_c64_org/base/protecting_against_soft-resets.md`
**SHA256**: `e6916baa160c38e7fa616c4f3e1aa1fdbb3dc93bd887f5cf67adbd042fb927be`

## Summary




# Protecting against soft-resets

base:protecting_against_soft-resets

                # Protecting against soft-resets

When the C64 gets a soft-reset signal, the first thing it does is check for an EPROM at $8000 (kernal routine [$FD02](http://unusedino.de/ec64/technical/aay/c64/romfd02.htm)). We can take advantage of this routine to redirect resets to our own code.

  * = $0900
  sei
  lda #$c3 ;the string "CBM80" at $8004 is used to check 8-ROM
  sta $8004
  lda #$c2
  sta $8005
  lda #$c...
