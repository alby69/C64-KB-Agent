---
title: DIM command
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  address: $B07E
  address_end: $B08A
  symbol: dim-command
  sources:
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B07E**: SEPARATED BY COMMAS'
---

# $B07E — DIM command

## Disassemblatura
```assembly
.B07E  20 FD AE JSR $AEFD
.B081  AA       TAX
.B082  20 90 B0 JSR $B090
.B085  20 79 00 JSR $0079
.B088  D0 F4    BNE $B07E
.B08A  60       RTS
```


## Commenti

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B07E**: SEPARATED BY COMMAS
- **$B081**: NON-ZERO, FLAGS PTRGET DIM CALLED
- **$B082**: ALLOCATE THE ARRAY
- **$B085**: NEXT CHAR
- **$B088**: NOT END OF STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*