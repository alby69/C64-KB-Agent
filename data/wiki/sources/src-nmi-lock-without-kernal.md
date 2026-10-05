---
id: src-nmi-lock-without-kernal
type: source
title: 'Source Summary: NMI Lock Without Kernal'
aliases:
- NMI Lock Without Kernal
- nmi_lock_without_kernal.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/nmi_lock_without_kernal.md
  sha256: e0604ab4caf391b6a46edf78dc98345545d618554e697d58fcc54fc1303bccfb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: NMI Lock Without Kernal

**Raw Source File**: `data/docs/codebase_c64_org/base/nmi_lock_without_kernal.md`
**SHA256**: `e0604ab4caf391b6a46edf78dc98345545d618554e697d58fcc54fc1303bccfb`

## Summary



# NMI Lock Without Kernal

base:nmi_lock_without_kernal

                # NMI Lock Without Kernal

Modification of the example given at [NMI lock](https://codebase.c64.org/doku.php?id=base:nmi_lock). The NMI is locked without using kernal routines and without using RAM at $0318/$0319.

  ; 'Disable NMI' without using kernal and $0318/$0319 by Sokrates
  sei  ;; switch off interrupt
  lda #$35 ;; all RAM except D000-Dfff 
  sta $01  ;; write to $FFFA/$FFFB now possible
  lda #<nmiRoutine ;; ch...
