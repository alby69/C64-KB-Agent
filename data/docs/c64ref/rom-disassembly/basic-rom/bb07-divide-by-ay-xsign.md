---
title: divide by (AY) (X=sign)
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
- bb07-fac-arg-ya
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $BB07
  address_end: $BB0C
  symbol: divide-by-ay-xsign
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BB07**: save sign compare (FAC1 EOR FAC2)'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BB0C**: DIVIDE ARG BY FAC'
---

# $BB07 — divide by (AY) (X=sign)

## Disassemblatura
```assembly
.BB07  86 6F    STX $6F   ; save sign compare (FAC1 EOR FAC2)
.BB09  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.BB0C  4C 12 BB JMP $BB12   ; do FAC2/FAC1 Perform divide-by
```


## Commenti

### Original Disassembly (—)
- **$BB07**: save sign compare (FAC1 EOR FAC2)
- **$BB09**: unpack memory (AY) into FAC1
- **$BB0C**: do FAC2/FAC1 Perform divide-by

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BB0C**: DIVIDE ARG BY FAC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*