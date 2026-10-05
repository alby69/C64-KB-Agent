---
id: e211-scan-for-valid-byte-not-eol-or-else-do-syntax-error-then-warm-start
type: entity
title: scan for valid byte, not [EOL] or ":", else do syntax error then warm start
aliases:
- scan for valid byte, not [EOL] or ":", else do syntax error then warm start
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e211-scan-for-valid-byte-not-eol-or-else-do-syntax-error-then-warm-start.md
  sha256: f6c8be15488efa15b1698b5b8f33847d14263e5f2a5071766fbed793bb9df1b0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e211-scan-for-valid-byte-not-eol-or-else-do-syntax-error-then-warm-start
---

# scan for valid byte, not [EOL] or ":", else do syntax error then warm start



# $E211 — scan for valid byte, not [EOL] or ":", else do syntax error then warm start

## Disassemblatura
```assembly
.E211  20 79 00 JSR $0079   ; scan memory
.E214  D0 F7    BNE $E20D   ; exit if following byte
.E216  4C 08 AF JMP $AF08   ; else do syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$E211**: scan memory
- **$E214**: exit if following byte
- **$E216**: else do syntax error then warm start

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e211-scan-for-valid-byte-not-eol-or-else-do-syntax-error-then-warm-start]]
