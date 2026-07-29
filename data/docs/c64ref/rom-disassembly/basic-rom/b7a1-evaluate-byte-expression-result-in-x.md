---
title: evaluate byte expression, result in X
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
- b7a1-convert-fac-to-single-byte-integer-in-x-reg
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - original_disassembly.txt
  address: $B7A1
  address_end: $B7AA
  symbol: evaluate-byte-expression-result-in-x
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B7A1**: evaluate integer expression, sign check'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B7A1**: CONVERT IF IN RANGE -32767 TO +32767'
---

# $B7A1 — evaluate byte expression, result in X

## Disassemblatura
```assembly
.B7A1  20 B8 B1 JSR $B1B8   ; evaluate integer expression, sign check
.B7A4  A6 64    LDX $64   ; get FAC1 mantissa 3
.B7A6  D0 F0    BNE $B798   ; if not null do illegal quantity error then warm start
.B7A8  A6 65    LDX $65   ; get FAC1 mantissa 4
.B7AA  4C 79 00 JMP $0079   ; scan memory and return
```


## Commenti

### Original Disassembly (—)
- **$B7A1**: evaluate integer expression, sign check
- **$B7A4**: get FAC1 mantissa 3
- **$B7A6**: if not null do illegal quantity error then warm start
- **$B7A8**: get FAC1 mantissa 4
- **$B7AA**: scan memory and return

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B7A1**: CONVERT IF IN RANGE -32767 TO +32767
- **$B7A4**: HI-BYTE MUST BE ZERO
- **$B7A6**: VALUE > 255, ERROR
- **$B7A8**: VALUE IN X-REG
- **$B7AA**: GET NEXT CHAR IN A-REG

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*