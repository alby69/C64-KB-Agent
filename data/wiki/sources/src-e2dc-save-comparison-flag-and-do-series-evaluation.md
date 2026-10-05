---
id: src-e2dc-save-comparison-flag-and-do-series-evaluation
type: source
title: 'Source Summary: save comparison flag and do series evaluation'
aliases:
- save comparison flag and do series evaluation
- e2dc-save-comparison-flag-and-do-series-evaluation.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e2dc-save-comparison-flag-and-do-series-evaluation.md
  sha256: 3150820988c8e3942526c7ff207756e86f30771aaa47a6bbd6630c01192976c3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: save comparison flag and do series evaluation

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e2dc-save-comparison-flag-and-do-series-evaluation.md`
**SHA256**: `3150820988c8e3942526c7ff207756e86f30771aaa47a6bbd6630c01192976c3`

## Summary



# $E2DC — save comparison flag and do series evaluation

## Disassemblatura
```assembly
.E2DC  48       PHA   ; save comparison flag
.E2DD  4C 9D E2 JMP $E29D   ; add 0.25, ^2 then series evaluation
```


## Commenti

### Original Disassembly (—)
- **$E2DC**: save comparison flag
- **$E2DD**: add 0.25, ^2 then series evaluation

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
