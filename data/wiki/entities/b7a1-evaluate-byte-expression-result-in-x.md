---
id: b7a1-evaluate-byte-expression-result-in-x
type: entity
title: evaluate byte expression, result in X
aliases:
- evaluate byte expression, result in X
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
links_out:
- src-b7a1-evaluate-byte-expression-result-in-x
---

# evaluate byte expression, result in X



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
- **$B7A4**: get FAC1 mantissa 3
- **$B7A6**: if not null do illegal quantity error then warm start
- **$B7A8**: get FAC1 mantissa 4
- **$B7AA**: scan memory and return

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B7A1**: CONVERT IF IN RANGE -32767 TO +32767
- **$B7A4**: HI-BYTE MUST BE ZERO
- **$B7A6**: VALUE > 255, ERROR
- **$B7A8**: VALUE IN X-REG
- **$B7AA**: GET NEXT CHAR IN A-REG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-b7a1-evaluate-byte-expression-result-in-x]]
