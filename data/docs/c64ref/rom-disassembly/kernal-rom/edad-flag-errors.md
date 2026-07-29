---
title: FLAG ERRORS
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- edad-flag-errors
- lda
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  address: $EDAD
  address_end: $EDB7
  symbol: flag-errors
  sources:
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EDAD**: flag ?DEVICE NOT PRESENT'
---

# $EDAD — FLAG ERRORS

## Disassemblatura
```assembly
.EDAD  A9 80    LDA #$80   ; flag ?DEVICE NOT PRESENT
.EDAF  2C       .BYTE $2C   ; mask LDA #$03
.EDB0  A9 03    LDA #$03   ; flag write timeout
.EDB2  20 1C FE JSR $FE1C   ; set I/O status word
.EDB5  58       CLI
.EDB6  18       CLC
.EDB7  90 4A    BCC $EE03   ; always jump, do final handshake
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$EDAD**: flag ?DEVICE NOT PRESENT
- **$EDAF**: mask LDA #$03
- **$EDB0**: flag write timeout
- **$EDB2**: set I/O status word
- **$EDB7**: always jump, do final handshake

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*