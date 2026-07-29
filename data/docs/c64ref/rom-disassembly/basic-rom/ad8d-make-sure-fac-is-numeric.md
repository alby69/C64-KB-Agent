---
title: MAKE SURE (FAC) IS NUMERIC
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - commodore-64-intern-buch.txt
  address: $AD8D
  address_end: $AD8E
  symbol: make-sure-fac-is-numeric
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AD8D**: Flag für Test auf numerisch'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AD8E**: DUMMY FOR SKIP'
---

# $AD8D — MAKE SURE (FAC) IS NUMERIC

## Disassemblatura
```assembly
.AD8D  18       CLC
.AD8E  24       .BYTE $24   ; DUMMY FOR SKIP
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AD8D**: Flag für Test auf numerisch
- **$AD8E**: BIT-Befehl um folgenden Befehl auszulassen

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AD8E**: DUMMY FOR SKIP

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*