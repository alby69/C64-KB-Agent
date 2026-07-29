---
title: do bad subscript error
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
- b245-error-bad-subscripts
- bit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B245
  address_end: $B247
  symbol: do-bad-subscript-error
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B245**: error $12, bad subscript error'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B247**: TRICK TO SKIP NEXT LINE'
---

# $B245 — do bad subscript error

## Disassemblatura
```assembly
.B245  A2 12    LDX #$12   ; error $12, bad subscript error
.B247  2C       .BYTE $2C   ; makes next line BIT $0EA2
```


## Commenti

### Original Disassembly (—)
- **$B245**: error $12, bad subscript error
- **$B247**: makes next line BIT $0EA2

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B247**: TRICK TO SKIP NEXT LINE

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*