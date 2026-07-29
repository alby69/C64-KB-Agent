---
title: scan for next BASIC line
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a909-get-end-of-line
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $A909
  address_end: $A926
  symbol: scan-for-next-basic-line
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A909**: set alternate search character = [EOL]'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A922**: quote mark'
---

# $A909 — scan for next BASIC line

## Disassemblatura
```assembly
.A909  A2 00    LDX #$00   ; set alternate search character = [EOL]
.A90B  86 07    STX $07   ; store alternate search character
.A90D  A0 00    LDY #$00   ; set search character = [EOL]
.A90F  84 08    STY $08   ; save the search character
.A911  A5 08    LDA $08   ; get search character
.A913  A6 07    LDX $07   ; get alternate search character
.A915  85 07    STA $07   ; make search character = alternate search character
.A917  86 08    STX $08   ; make alternate search character = search character
.A919  B1 7A    LDA ($7A),Y   ; get BASIC byte
.A91B  F0 E8    BEQ $A905   ; exit if null [EOL]
.A91D  C5 08    CMP $08   ; compare with search character
.A91F  F0 E4    BEQ $A905   ; exit if found
.A921  C8       INY   ; else increment index
.A922  C9 22    CMP #$22   ; compare current character with open quote
.A924  D0 F3    BNE $A919   ; if found go swap search character for alternate search character
.A926  F0 E9    BEQ $A911   ; loop for next character, branch always
```


## Commenti

### Original Disassembly (—)
- **$A909**: set alternate search character = [EOL]
- **$A90B**: store alternate search character
- **$A90D**: set search character = [EOL]
- **$A90F**: save the search character
- **$A911**: get search character
- **$A913**: get alternate search character
- **$A915**: make search character = alternate search character
- **$A917**: make alternate search character = search character
- **$A919**: get BASIC byte
- **$A91B**: exit if null [EOL]
- **$A91D**: compare with search character
- **$A91F**: exit if found
- **$A921**: else increment index
- **$A922**: compare current character with open quote
- **$A924**: if found go swap search character for alternate search character
- **$A926**: loop for next character, branch always

### Marko Mäkelä (Marko Mäkelä)
- **$A922**: quote mark

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*