---
title: defer a command
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- ed21-defer-a-command
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $ED21
  address_end: $ED3D
  symbol: defer-a-command
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ED21**: save as serial deferred character'
---

# $ED21 — defer a command

## Disassemblatura
```assembly
.ED21  85 95    STA $95   ; save as serial deferred character
.ED23  78       SEI   ; disable the interrupts
.ED24  20 97 EE JSR $EE97   ; set the serial data out high
.ED27  C9 3F    CMP #$3F   ; compare read byte with $3F
.ED29  D0 03    BNE $ED2E   ; branch if not $3F, this branch will always be taken as after VIA 2's PCR is read it is ANDed with $DF, so the result can never be $3F ??
.ED2B  20 85 EE JSR $EE85   ; set the serial clock out high
.ED2E  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.ED31  09 08    ORA #$08   ; mask xxxx 1xxx, set serial ATN low
.ED33  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address if the code drops through to here the serial clock is low and the serial data has been released so the following code will have no effect apart from delaying the first byte by 1ms set the serial clk/data, wait and Tx byte on the serial bus
.ED36  78       SEI   ; disable the interrupts
.ED37  20 8E EE JSR $EE8E   ; set the serial clock out low
.ED3A  20 97 EE JSR $EE97   ; set the serial data out high
.ED3D  20 B3 EE JSR $EEB3   ; 1ms delay
```


## Commenti

### Original Disassembly (—)
- **$ED21**: save as serial deferred character
- **$ED23**: disable the interrupts
- **$ED24**: set the serial data out high
- **$ED27**: compare read byte with $3F
- **$ED29**: branch if not $3F, this branch will always be taken as after VIA 2's PCR is read it is ANDed with $DF, so the result can never be $3F ??
- **$ED2B**: set the serial clock out high
- **$ED2E**: read VIA 2 DRA, serial port and video address
- **$ED31**: mask xxxx 1xxx, set serial ATN low
- **$ED33**: save VIA 2 DRA, serial port and video address if the code drops through to here the serial clock is low and the serial data has been released so the following code will have no effect apart from delaying the first byte by 1ms set the serial clk/data, wait and Tx byte on the serial bus
- **$ED36**: disable the interrupts
- **$ED37**: set the serial clock out low
- **$ED3A**: set the serial data out high
- **$ED3D**: 1ms delay

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*