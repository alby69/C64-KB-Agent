---
id: e200-scan-and-get-byte-else-do-syntax-error-then-warm-start
type: entity
title: scan and get byte, else do syntax error then warm start
aliases:
- scan and get byte, else do syntax error then warm start
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e200-scan-and-get-byte-else-do-syntax-error-then-warm-start.md
  sha256: 9db0271d31e402815f4fbc01f1f42ce8ceba39c864d1c87467041f7289f01066
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e200-scan-and-get-byte-else-do-syntax-error-then-warm-start
---

# scan and get byte, else do syntax error then warm start



# $E200 — scan and get byte, else do syntax error then warm start

## Disassemblatura
```assembly
.E200  20 0E E2 JSR $E20E   ; scan for ",byte", else do syntax error then warm start
.E203  4C 9E B7 JMP $B79E   ; get byte parameter and return exit function if [EOT] or ":"
.E206  20 79 00 JSR $0079   ; scan memory
.E209  D0 02    BNE $E20D   ; branch if not [EOL] or ":"
.E20B  68       PLA   ; dump return address low byte
.E20C  68       PLA   ; dump return address high byte
.E20D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E200**: scan for ",byte", else do syntax error then warm start
- **$E203**: get byte parameter and return exit function if [EOT] or ":"
- **$E206**: scan memory
- **$E209**: branch if not [EOL] or ":"
- **$E20B**: dump return address low byte
- **$E20C**: dump return address high byte

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E200**: check for comma
- **$E203**: input one byte parameter to (X)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e200-scan-and-get-byte-else-do-syntax-error-then-warm-start]]
