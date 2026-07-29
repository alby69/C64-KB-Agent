---
title: home the cursor
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e566-cursor-home
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E566
  address_end: $E56A
  symbol: home-the-cursor
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E566**: clear Y'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E566**: Löschen der'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E568**: write to PNTR, cursor column'
---

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