---
title: do CRTL-C check vector
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
- a82c-prft-auf-stop-taste
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A82C
  address_end: $A82C
  symbol: do-crtl-c-check-vector
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A82C**: scan stop key'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A82C**: Stop-Taste abfragen'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $A82C — do CRTL-C check vector

## Disassemblatura
```assembly
.A82C  20 E1 FF JSR $FFE1   ; scan stop key
```


## Commenti

### Original Disassembly (—)
- **$A82C**: scan stop key

### Commodore-64-intern-Buch (Commodore)
- **$A82C**: Stop-Taste abfragen

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*