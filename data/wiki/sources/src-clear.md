---
id: src-clear
type: source
title: 'Source Summary: Serial Channels and Reset Default Devices F333/F3F3-F349/F409'
aliases:
- Serial Channels and Reset Default Devices F333/F3F3-F349/F409
- clear.md
tags:
- kernal-api
- system-routines
- jumps
sources:
- path: data/docs/c64ref/kernal-api/clear.md
  sha256: 1c7763737d0d70bc566cebaaf955f849397314b290bd9b97d367bc1a3860997e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Serial Channels and Reset Default Devices F333/F3F3-F349/F409

**Raw Source File**: `data/docs/c64ref/kernal-api/clear.md`
**SHA256**: `1c7763737d0d70bc566cebaaf955f849397314b290bd9b97d367bc1a3860997e`

## Summary



# Clear — Serial Channels and Reset Default Devices F333/F3F3-F349/F409 ($F333)

## Panoramica
La routine KERNAL `Clear` viene descritta di seguito con le relative note e dettagli tecnici.

## Dettagli Tecnici
- **Indirizzo**: `$F333`
- **Chiamata**: `JSR Clear` o `SYS 62259`


## Note per Fonte

### COMPUTE!'s Tool Kit: Kernal (Dan Heeb)
ed by**: Indirect JMP through (0322) from Kernal CLRCHN vector at
fall through from F331/F3F1 in Reset to No Open Files.

ation**:

the current output device...
