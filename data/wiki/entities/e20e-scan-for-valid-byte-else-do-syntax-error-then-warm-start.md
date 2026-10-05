---
id: e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start
type: entity
title: scan for ",valid byte", else do syntax error then warm start
aliases:
- scan for ",valid byte", else do syntax error then warm start
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start.md
  sha256: e9e2be661cf2ba83bc7c913aca570eca8ba5aa3236924b999ca2a10d0d535367
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start
---

# scan for ",valid byte", else do syntax error then warm start



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
- **$E216**: execute SYNTAX error

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e20e-scan-for-valid-byte-else-do-syntax-error-then-warm-start]]
