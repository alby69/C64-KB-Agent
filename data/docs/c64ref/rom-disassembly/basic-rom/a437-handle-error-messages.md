---
title: handle error messages
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
- a437-fehlereinsprung
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - commodore-64-intern-buch.txt
  address: $A437
  address_end: $A437
  symbol: handle-error-messages
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A437**: Zum BASIC-Warmstart ($E38B)'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A437**: normally A43A'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A483**: READ A LINE'
---

# $A437 — handle error messages

## Disassemblatura
```assembly
.A437  6C 00 03 JMP ($0300)   ; normally A43A
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A437**: Zum BASIC-Warmstart ($E38B)

### Marko Mäkelä (Marko Mäkelä)
- **$A437**: normally A43A

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A483**: READ A LINE
- **$A486**: SET UP CHRGET TO SCAN THE LINE
- **$A48E**: EMPTY LINE
- **$A490**: $FF IN HI-BYTE OF CURLIN MEANS
- **$A492**: WE ARE IN DIRECT MODE
- **$A494**: CHRGET SAW DIGIT, NUMBERED LINE
- **$A496**: NO NUMBER, SO PARSE IT
- **$A499**: AND TRY EXECUTING IT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*