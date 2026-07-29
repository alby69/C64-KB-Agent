---
title: setup for RS232 transmit
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
- f028-setup-for-rs232-transmit
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $F028
  address_end: $F04C
  symbol: setup-for-rs232-transmit
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F028**: get the RS-232 interrupt enable byte'
---

# $F028 — setup for RS232 transmit

## Disassemblatura
```assembly
.F028  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F02B  4A       LSR   ; shift the enable bit to Cb
.F02C  B0 1E    BCS $F04C   ; if interrupts are enabled just exit
.F02E  A9 10    LDA #$10   ; start timer A
.F030  8D 0E DD STA $DD0E   ; save VIA 2 CRA
.F033  AD 99 02 LDA $0299   ; get the baud rate bit time low byte
.F036  8D 04 DD STA $DD04   ; save VIA 2 timer A low byte
.F039  AD 9A 02 LDA $029A   ; get the baud rate bit time high byte
.F03C  8D 05 DD STA $DD05   ; save VIA 2 timer A high byte
.F03F  A9 81    LDA #$81   ; enable timer A interrupt
.F041  20 3B EF JSR $EF3B   ; set VIA 2 ICR from A
.F044  20 06 EF JSR $EF06   ; setup next RS232 Tx byte
.F047  A9 11    LDA #$11   ; load timer A, start timer A
.F049  8D 0E DD STA $DD0E   ; save VIA 2 CRA
.F04C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F028**: get the RS-232 interrupt enable byte
- **$F02B**: shift the enable bit to Cb
- **$F02C**: if interrupts are enabled just exit
- **$F02E**: start timer A
- **$F030**: save VIA 2 CRA
- **$F033**: get the baud rate bit time low byte
- **$F036**: save VIA 2 timer A low byte
- **$F039**: get the baud rate bit time high byte
- **$F03C**: save VIA 2 timer A high byte
- **$F03F**: enable timer A interrupt
- **$F041**: set VIA 2 ICR from A
- **$F044**: setup next RS232 Tx byte
- **$F047**: load timer A, start timer A
- **$F049**: save VIA 2 CRA

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*