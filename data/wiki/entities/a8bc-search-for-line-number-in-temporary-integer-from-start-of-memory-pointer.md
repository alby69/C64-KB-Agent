---
id: a8bc-search-for-line-number-in-temporary-integer-from-start-of-memory-pointer
type: entity
title: search for line number in temporary integer from start of memory pointer
aliases:
- search for line number in temporary integer from start of memory pointer
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a8bc-search-for-line-number-in-temporary-integer-from-start-of-memory-pointer.md
  sha256: dce74b40681949ec4efd159d12e51fb1ba5b2e2ba9e56bf8a5249c2a987c1963
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-a8bc-search-for-line-number-in-temporary-integer-from-start-of-memory-pointer
---

# search for line number in temporary integer from start of memory pointer



# $A8BC — search for line number in temporary integer from start of memory pointer

## Disassemblatura
```assembly
.A8BC  A5 2B    LDA $2B   ; get start of memory low byte
.A8BE  A6 2C    LDX $2C   ; get start of memory high byte
```


## Commenti

### Original Disassembly (—)
- **$A8BC**: get start of memory low byte
- **$A8BE**: get start of memory high byte

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a8bc-search-for-line-number-in-temporary-integer-from-start-of-memory-pointer]]
