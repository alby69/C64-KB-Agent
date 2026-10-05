---
id: e599-orphan-bytes
type: entity
title: orphan bytes ??
aliases:
- orphan bytes ??
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e599-orphan-bytes.md
  sha256: 6132b818d585edff6613a348e32db62b322486535f77a6987e0977073330fc1f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e599-orphan-bytes
---

# orphan bytes ??



# $E599 — orphan bytes ??

## Disassemblatura
```assembly
.E599  EA       NOP   ; huh
.E59A  20 A0 E5 JSR $E5A0   ; initialise the vic chip
.E59D  4C 66 E5 JMP $E566   ; home the cursor and return
```


## Commenti

### Original Disassembly (—)
- **$E599**: huh
- **$E59A**: initialise the vic chip
- **$E59D**: home the cursor and return

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e599-orphan-bytes]]
