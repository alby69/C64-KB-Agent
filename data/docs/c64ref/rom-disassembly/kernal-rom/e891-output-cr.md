---
title: output [CR]
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- e891-output-carriage-return
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $E891
  address_end: $E89E
  symbol: output-cr
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E891**: clear X'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E893**: INSRT, disable insert mode'
---

# $E891 — output [CR]

## Disassemblatura
```assembly
.E891  A2 00    LDX #$00   ; clear X
.E893  86 D8    STX $D8   ; clear the insert count
.E895  86 C7    STX $C7   ; clear the reverse flag
.E897  86 D4    STX $D4   ; clear the cursor quote flag, $xx = quote, $00 = no quote
.E899  86 D3    STX $D3   ; save the cursor column
.E89B  20 7C E8 JSR $E87C   ; do newline
.E89E  4C A8 E6 JMP $E6A8   ; restore the registers, set the quote flag and exit
```


## Commenti

### Original Disassembly (—)
- **$E891**: clear X
- **$E893**: clear the insert count
- **$E895**: clear the reverse flag
- **$E897**: clear the cursor quote flag, $xx = quote, $00 = no quote
- **$E899**: save the cursor column
- **$E89B**: do newline
- **$E89E**: restore the registers, set the quote flag and exit

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E893**: INSRT, disable insert mode
- **$E895**: RVS, disable reversed mode
- **$E897**: QTSW, disable quotes mode
- **$E899**: PNTR, put cursor at first column
- **$E89B**: go to next line
- **$E89E**: finish screen print

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*