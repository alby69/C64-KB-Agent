---
title: read/set the x,y cursor position
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e50a-c1
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E50A
  address_end: $E517
  symbol: readset-the-xy-cursor-position
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E50A**: if read cursor go do read'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E50A**: Carry gesetzt, dann zu $E513'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E50A**: if carry set, jump'
---

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