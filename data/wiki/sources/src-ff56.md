---
id: src-ff56
type: source
title: 'Source Summary: X'
aliases:
- X
- ff56.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/ff56.md
  sha256: c59e0d35d990db45c50e402cfdfaa06dfd1e0aa34c5b58ce72306ac0b2529b87
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: X

**Raw Source File**: `data/docs/c64ref/kernal-api/ff56.md`
**SHA256**: `c59e0d35d990db45c50e402cfdfaa06dfd1e0aa34c5b58ce72306ac0b2529b87`

## Summary



# $FF56 — X ($FF56)

## Panoramica
La routine KERNAL `None` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$FF56`
- **Chiamata**: `JSR None` o `SYS 65366`


## Note per Fonte

### Machine Language Routines (Todd D Heimarck)
outine initializes function ROMs and attempts to boot a
rom the default drive. The presence of function ROMs in
dges or in the 128's spare ROM socket is recorded during
wer-on/reset sequence. This routine initializ...
