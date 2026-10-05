---
id: src-sign-extension
type: source
title: 'Source Summary: base:sign_extension [Codebase64 wiki]'
aliases:
- base:sign_extension [Codebase64 wiki]
- sign_extension.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sign_extension.md
  sha256: f3626a2b506643481bd2d5e9898a8bea04cfc01c2aea7af285486d691d24cfa9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:sign_extension [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/sign_extension.md`
**SHA256**: `f3626a2b506643481bd2d5e9898a8bea04cfc01c2aea7af285486d691d24cfa9`

## Summary



# base:sign_extension [Codebase64 wiki]

Convert a signed 8-bit number to a signed 16-bit number, with .Y holding the high byte:

ldy #$00 lda value bpl :+ dey :

## Codice Estratto

### Snippet Codice (Dialetto: Generic Assembly)

```assembly
ldy #$00
 lda value
 bpl :+
  dey
:
```



---
*Fonte originale: [https://codebase.c64.org/doku.php?id=base%3Asign_extension](https://codebase.c64.org/doku.php?id=base%3Asign_extension)*
...
