---
id: src-e200-scan-and-get-byte-else-do-syntax-error-then-warm-start
type: source
title: 'Source Summary: scan and get byte, else do syntax error then warm start'
aliases:
- scan and get byte, else do syntax error then warm start
- e200-scan-and-get-byte-else-do-syntax-error-then-warm-start.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e200-scan-and-get-byte-else-do-syntax-error-then-warm-start.md
  sha256: 9db0271d31e402815f4fbc01f1f42ce8ceba39c864d1c87467041f7289f01066
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: scan and get byte, else do syntax error then warm start

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e200-scan-and-get-byte-else-do-syntax-error-then-warm-start.md`
**SHA256**: `9db0271d31e402815f4fbc01f1f42ce8ceba39c864d1c87467041f7289f01066`

## Summary



# $E200 — scan and get byte, else do syntax error then warm start

## Disassemblatura
```assembly
.E200  20 0E E2 JSR $E20E   ; scan for ",byte", else do syntax error then warm start
.E203  4C 9E B7 JMP $B79E   ; get byte parameter and return exit function if [EOT] or ":"
.E206  20 79 00 JSR $0079   ; scan memory
.E209  D0 02    BNE $E20D   ; branch if not [EOL] or ":"
.E20B  68       PLA   ; dump return address low byte
.E20C  68       PLA   ; dump return address high byte
.E20D  60       RTS...
