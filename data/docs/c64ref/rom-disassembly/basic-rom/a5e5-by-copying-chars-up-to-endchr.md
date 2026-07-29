---
title: BY COPYING CHARS UP TO ENDCHR.
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
- 0008-endchr
- input
- output
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $A5E5
  address_end: $A5F3
  symbol: by-copying-chars-up-to-endchr
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A5E8**: END OF LINE'
---

# $A5E5 — BY COPYING CHARS UP TO ENDCHR.

## Disassemblatura
```assembly
.A5E5  BD 00 02 LDA $0200,X
.A5E8  F0 DF    BEQ $A5C9   ; END OF LINE
.A5EA  C5 08    CMP $08
.A5EC  F0 DB    BEQ $A5C9   ; FOUND ENDCHR
.A5EE  C8       INY   ; NEXT OUTPUT CHAR
.A5EF  99 FB 01 STA $01FB,Y
.A5F2  E8       INX   ; NEXT INPUT CHAR
.A5F3  D0 F0    BNE $A5E5   ; ...ALWAYS
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A5E8**: END OF LINE
- **$A5EC**: FOUND ENDCHR
- **$A5EE**: NEXT OUTPUT CHAR
- **$A5F2**: NEXT INPUT CHAR
- **$A5F3**: ...ALWAYS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*