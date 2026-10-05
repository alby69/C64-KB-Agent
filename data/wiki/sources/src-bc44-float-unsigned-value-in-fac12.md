---
id: src-bc44-float-unsigned-value-in-fac12
type: source
title: 'Source Summary: FLOAT UNSIGNED VALUE IN FAC+1,2'
aliases:
- FLOAT UNSIGNED VALUE IN FAC+1,2
- bc44-float-unsigned-value-in-fac12.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc44-float-unsigned-value-in-fac12.md
  sha256: 31c54e1f54658f1225f938f28db475d8fdb5c1e26b2c7a3e5ae20c2738cca6a0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: FLOAT UNSIGNED VALUE IN FAC+1,2

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/bc44-float-unsigned-value-in-fac12.md`
**SHA256**: `31c54e1f54658f1225f938f28db475d8fdb5c1e26b2c7a3e5ae20c2738cca6a0`

## Summary



# $BC44 — FLOAT UNSIGNED VALUE IN FAC+1,2

## Disassemblatura
```assembly
.BC44  A5 62    LDA $62   ; MSBIT=0, SET CARRY; =1, CLEAR CARRY
.BC46  49 FF    EOR #$FF
.BC48  2A       ROL
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC44**: MSBIT=0, SET CARRY; =1, CLEAR CARRY

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
