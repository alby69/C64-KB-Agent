---
id: e50a-readset-the-xy-cursor-position
type: entity
title: read/set the x,y cursor position
aliases:
- read/set the x,y cursor position
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e50a-readset-the-xy-cursor-position.md
  sha256: 1682401b3b219f7f5f04990fd9dba04a5a3e47a92dd39b246a9f2e03110a12cb
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e50a-readset-the-xy-cursor-position
---

# read/set the x,y cursor position



# $E50A — read/set the x,y cursor position

## Disassemblatura
```assembly
.E50A  B0 07    BCS $E513   ; if read cursor go do read
.E50C  86 D6    STX $D6   ; save the cursor row
.E50E  84 D3    STY $D3   ; save the cursor column
.E510  20 6C E5 JSR $E56C   ; set the screen pointers for the cursor row, column
.E513  A6 D6    LDX $D6   ; get the cursor row
.E515  A4 D3    LDY $D3   ; get the cursor column
.E517  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E50A**: if read cursor go do read
- **$E50C**: save the cursor row
- **$E50E**: save the cursor column
- **$E510**: set the screen pointers for the cursor row, column
- **$E513**: get the cursor row
- **$E515**: get the cursor column

### Commodore-64-intern-Buch (Commodore)
- **$E50A**: Carry gesetzt, dann zu $E513
- **$E50C**: Zeile
- **$E50E**: Spalte
- **$E510**: Cursor setzen
- **$E513**: Zeile
- **$E515**: Spalte
- **$E517**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E50A**: if carry set, jump
- **$E50C**: store TBLX, current row
- **$E50E**: store PNTR, current column
- **$E510**: set screen pointers
- **$E513**: read TBLX
- **$E515**: read PNTR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e50a-readset-the-xy-cursor-position]]
