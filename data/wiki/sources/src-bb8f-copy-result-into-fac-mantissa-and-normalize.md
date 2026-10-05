---
id: src-bb8f-copy-result-into-fac-mantissa-and-normalize
type: source
title: 'Source Summary: COPY RESULT INTO FAC MANTISSA, AND NORMALIZE'
aliases:
- COPY RESULT INTO FAC MANTISSA, AND NORMALIZE
- bb8f-copy-result-into-fac-mantissa-and-normalize.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bb8f-copy-result-into-fac-mantissa-and-normalize.md
  sha256: 51186f01c03d6d822422db8358f8d568f84ecfa7406dad7f7b4bca1baa633fd6
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: COPY RESULT INTO FAC MANTISSA, AND NORMALIZE

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bb8f-copy-result-into-fac-mantissa-and-normalize.md`
**SHA256**: `51186f01c03d6d822422db8358f8d568f84ecfa7406dad7f7b4bca1baa633fd6`

## Summary



# $BB8F — COPY RESULT INTO FAC MANTISSA, AND NORMALIZE

## Disassemblatura
```assembly
.BB8F  A5 26    LDA $26
.BB91  85 62    STA $62
.BB93  A5 27    LDA $27
.BB95  85 63    STA $63
.BB97  A5 28    LDA $28
.BB99  85 64    STA $64
.BB9B  A5 29    LDA $29
.BB9D  85 65    STA $65
.BB9F  4C D7 B8 JMP $B8D7
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
