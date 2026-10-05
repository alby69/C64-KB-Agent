---
id: src-e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start
type: source
title: 'Source Summary: scan for ",valid byte", else do syntax error then warm start'
aliases:
- scan for ",valid byte", else do syntax error then warm start
- e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start.md
  sha256: e9e2be661cf2ba83bc7c913aca570eca8ba5aa3236924b999ca2a10d0d535367
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan for ",valid byte", else do syntax error then warm start

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start.md`
**SHA256**: `e9e2be661cf2ba83bc7c913aca570eca8ba5aa3236924b999ca2a10d0d535367`

## Summary



# $E20E — scan for ",valid byte", else do syntax error then warm start

## Disassemblatura
```assembly
.E20E  20 FD AE JSR $AEFD   ; scan for ",", else do syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$E20E**: scan for ",", else do syntax error then warm start

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E20E**: confirm comma
- **$E211**: get CHRGOT
- **$E214**: else than null
- **$E216**: execute SYNTAX ...
