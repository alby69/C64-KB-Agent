---
id: src-b7a1-evaluate-byte-expression-result-in-x
type: source
title: 'Source Summary: evaluate byte expression, result in X'
aliases:
- evaluate byte expression, result in X
- b7a1-evaluate-byte-expression-result-in-x.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b7a1-evaluate-byte-expression-result-in-x.md
  sha256: c960120b1a2c2f6cc294394e823e162239c76d23f89b9283198a313af220a7c1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate byte expression, result in X

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b7a1-evaluate-byte-expression-result-in-x.md`
**SHA256**: `c960120b1a2c2f6cc294394e823e162239c76d23f89b9283198a313af220a7c1`

## Summary



# $B7A1 — evaluate byte expression, result in X

## Disassemblatura
```assembly
.B7A1  20 B8 B1 JSR $B1B8   ; evaluate integer expression, sign check
.B7A4  A6 64    LDX $64   ; get FAC1 mantissa 3
.B7A6  D0 F0    BNE $B798   ; if not null do illegal quantity error then warm start
.B7A8  A6 65    LDX $65   ; get FAC1 mantissa 4
.B7AA  4C 79 00 JMP $0079   ; scan memory and return
```


## Commenti

### Original Disassembly (—)
- **$B7A1**: evaluate integer expression, sign check
- **$B7A4**: g...
