---
id: e566-home-the-cursor
type: entity
title: home the cursor
aliases:
- home the cursor
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e566-home-the-cursor.md
  sha256: e1668604191e9b9718733007f23be6cc706e47ff27716bf44755fc7df4aee203
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e566-home-the-cursor
---

# home the cursor



# $E566 — home the cursor

## Disassemblatura
```assembly
.E566  A0 00    LDY #$00   ; clear Y
.E568  84 D3    STY $D3   ; clear the cursor column
.E56A  84 D6    STY $D6   ; clear the cursor row
```


## Commenti

### Original Disassembly (—)
- **$E566**: clear Y
- **$E568**: clear the cursor column
- **$E56A**: clear the cursor row

### Commodore-64-intern-Buch (Commodore)
- **$E566**: Löschen der
- **$E568**: Cursorspalte und
- **$E56A**: Cursorzeile

### Magnus Nyman (Magnus Nyman)
- **$E568**: write to PNTR, cursor column
- **$E56A**: write to TBLX, line number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e566-home-the-cursor]]
