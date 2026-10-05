---
id: e701-back-onto-the-previous-line-if-possible
type: entity
title: back onto the previous line if possible
aliases:
- back onto the previous line if possible
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e701-back-onto-the-previous-line-if-possible.md
  sha256: a55a0c1294a9153a5895484c1558d68ce2af96941ade27b05f88a47ed86f4210
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e701-back-onto-the-previous-line-if-possible
---

# back onto the previous line if possible



# $E701 — back onto the previous line if possible

## Disassemblatura
```assembly
.E701  A6 D6    LDX $D6   ; get the cursor row
.E703  D0 06    BNE $E70B   ; branch if not top row
.E705  86 D3    STX $D3   ; clear cursor column
.E707  68       PLA   ; dump return address low byte
.E708  68       PLA   ; dump return address high byte
.E709  D0 9D    BNE $E6A8   ; restore registers, set quote flag and exit, branch always
.E70B  CA       DEX   ; decrement the cursor row
.E70C  86 D6    STX $D6   ; save the cursor row
.E70E  20 6C E5 JSR $E56C   ; set the screen pointers for cursor row, column
.E711  A4 D5    LDY $D5   ; get current screen line length
.E713  84 D3    STY $D3   ; save the cursor column
.E715  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$E701**: get the cursor row
- **$E703**: branch if not top row
- **$E705**: clear cursor column
- **$E707**: dump return address low byte
- **$E708**: dump return address high byte
- **$E709**: restore registers, set quote flag and exit, branch always
- **$E70B**: decrement the cursor row
- **$E70C**: save the cursor row
- **$E70E**: set the screen pointers for cursor row, column
- **$E711**: get current screen line length
- **$E713**: save the cursor column

### Commodore-64-intern-Buch (Commodore)
- **$E701**: Cursorzeile
- **$E703**: wenn null, dann zu $E70B
- **$E705**: Cursorspalte
- **$E707**: Sprungadresse
- **$E708**: aus Stack holen
- **$E709**: unbedingter Sprung
- **$E70B**: Zeilennummer
- **$E70C**: erniedrigen
- **$E70E**: Cursorposition berechnen
- **$E711**: Zeilenlänge
- **$E713**: speichern
- **$E715**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E701**: test TBLX, physical line number
- **$E703**: if not on top line, branch
- **$E705**: set PNTR to zero as well
- **$E709**: always jump
- **$E70B**: decrement TBLX
- **$E70C**: and store
- **$E70E**: set screen pointers
- **$E711**: get LNMX
- **$E713**: and store in PNTR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-e701-back-onto-the-previous-line-if-possible]]
