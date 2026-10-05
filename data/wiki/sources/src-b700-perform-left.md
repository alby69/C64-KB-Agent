---
id: src-b700-perform-left
type: source
title: 'Source Summary: perform LEFT$()'
aliases:
- perform LEFT$()
- b700-perform-left.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b700-perform-left.md
  sha256: f380a62433b49d0f8e4b313bcbc2fa218266ecb3bdcb0cbba9ab3e1edd515787
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: perform LEFT$()

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b700-perform-left.md`
**SHA256**: `f380a62433b49d0f8e4b313bcbc2fa218266ecb3bdcb0cbba9ab3e1edd515787`

## Summary



# $B700 — perform LEFT$()

## Disassemblatura
```assembly
.B700  20 61 B7 JSR $B761   ; pull string data and byte parameter from stack return pointer in descriptor, byte in A (and X), Y=0
.B703  D1 50    CMP ($50),Y   ; compare byte parameter with string length
.B705  98       TYA   ; clear A
.B706  90 04    BCC $B70C   ; branch if string length > byte parameter
.B708  B1 50    LDA ($50),Y   ; else make parameter = length
.B70A  AA       TAX   ; copy to byte parameter copy
.B70B  98       TYA ...
