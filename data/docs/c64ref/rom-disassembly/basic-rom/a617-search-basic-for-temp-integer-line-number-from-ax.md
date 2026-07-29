---
title: search Basic for temp integer line number from AX
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a617-search-basic-for-temp-integer-line-number-from-ax
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $A617
  address_end: $A641
  symbol: search-basic-for-temp-integer-line-number-from-ax
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A617**: set index to next line pointer high byte'
---

# $A617 — search Basic for temp integer line number from AX

## Disassemblatura
```assembly
.A617  A0 01    LDY #$01   ; set index to next line pointer high byte
.A619  85 5F    STA $5F   ; save low byte as current
.A61B  86 60    STX $60   ; save high byte as current
.A61D  B1 5F    LDA ($5F),Y   ; get next line pointer high byte from address
.A61F  F0 1F    BEQ $A640   ; pointer was zero so done, exit
.A621  C8       INY   ; increment index ...
.A622  C8       INY   ; ... to line # high byte
.A623  A5 15    LDA $15   ; get temporary integer high byte
.A625  D1 5F    CMP ($5F),Y   ; compare with line # high byte
.A627  90 18    BCC $A641   ; exit if temp < this line, target line passed
.A629  F0 03    BEQ $A62E   ; go check low byte if =
.A62B  88       DEY   ; else decrement index
.A62C  D0 09    BNE $A637   ; branch always
.A62E  A5 14    LDA $14   ; get temporary integer low byte
.A630  88       DEY   ; decrement index to line # low byte
.A631  D1 5F    CMP ($5F),Y   ; compare with line # low byte
.A633  90 0C    BCC $A641   ; exit if temp < this line, target line passed
.A635  F0 0A    BEQ $A641   ; exit if temp = (found line#) not quite there yet
.A637  88       DEY   ; decrement index to next line pointer high byte
.A638  B1 5F    LDA ($5F),Y   ; get next line pointer high byte
.A63A  AA       TAX   ; copy to X
.A63B  88       DEY   ; decrement index to next line pointer low byte
.A63C  B1 5F    LDA ($5F),Y   ; get next line pointer low byte
.A63E  B0 D7    BCS $A617   ; go search for line # in temporary integer from AX, carry always set
.A640  18       CLC   ; clear found flag
.A641  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$A617**: set index to next line pointer high byte
- **$A619**: save low byte as current
- **$A61B**: save high byte as current
- **$A61D**: get next line pointer high byte from address
- **$A61F**: pointer was zero so done, exit
- **$A621**: increment index ...
- **$A622**: ... to line # high byte
- **$A623**: get temporary integer high byte
- **$A625**: compare with line # high byte
- **$A627**: exit if temp < this line, target line passed
- **$A629**: go check low byte if =
- **$A62B**: else decrement index
- **$A62C**: branch always
- **$A62E**: get temporary integer low byte
- **$A630**: decrement index to line # low byte
- **$A631**: compare with line # low byte
- **$A633**: exit if temp < this line, target line passed
- **$A635**: exit if temp = (found line#) not quite there yet
- **$A637**: decrement index to next line pointer high byte
- **$A638**: get next line pointer high byte
- **$A63A**: copy to X
- **$A63B**: decrement index to next line pointer low byte
- **$A63C**: get next line pointer low byte
- **$A63E**: go search for line # in temporary integer from AX, carry always set
- **$A640**: clear found flag

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*