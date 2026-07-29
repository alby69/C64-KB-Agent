---
title: '"STEP" PHRASE OF "FOR" STATEMENT'
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
- a78b-step-phrase-of-for-statement
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  address: $A78B
  address_end: $A7AD
  symbol: step-phrase-of-for-statement
  sources:
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A78B**: STEP DEFAULT=1'
---

# $A78B — "STEP" PHRASE OF "FOR" STATEMENT

## Disassemblatura
```assembly
.A78B  A9 BC    LDA #$BC   ; STEP DEFAULT=1
.A78D  A0 B9    LDY #$B9
.A78F  20 A2 BB JSR $BBA2
.A792  20 79 00 JSR $0079
.A795  C9 A9    CMP #$A9
.A797  D0 06    BNE $A79F   ; USE DEFAULT VALUE OF 1.0
.A799  20 73 00 JSR $0073   ; STEP SPECIFIED, GET IT
.A79C  20 8A AD JSR $AD8A
.A79F  20 2B BC JSR $BC2B
.A7A2  20 38 AE JSR $AE38
.A7A5  A5 4A    LDA $4A
.A7A7  48       PHA
.A7A8  A5 49    LDA $49
.A7AA  48       PHA
.A7AB  A9 81    LDA #$81
.A7AD  48       PHA
```


## Commenti

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A78B**: STEP DEFAULT=1
- **$A797**: USE DEFAULT VALUE OF 1.0
- **$A799**: STEP SPECIFIED, GET IT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*