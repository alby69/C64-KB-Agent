---
title: tape read/write
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
- f875-common-code-for-cassette-read-and-write
- f8be-io-abschlu-abwarten
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $F875
  address_end: $F8CD
  symbol: tape-readwrite
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F875**: disable all interrupts'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F875 — tape read/write

## Disassemblatura
```assembly
.F875  A0 7F    LDY #$7F   ; disable all interrupts
.F877  8C 0D DC STY $DC0D   ; save VIA 1 ICR, disable all interrupts
.F87A  8D 0D DC STA $DC0D   ; save VIA 1 ICR, enable interrupts according to A check RS232 bus idle
.F87D  AD 0E DC LDA $DC0E   ; read VIA 1 CRA
.F880  09 19    ORA #$19   ; load timer B, timer B single shot, start timer B
.F882  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.F885  29 91    AND #$91   ; mask x00x 000x, TOD clock, load timer A, start timer A
.F887  8D A2 02 STA $02A2   ; save VIA 1 CRB shadow copy
.F88A  20 A4 F0 JSR $F0A4
.F88D  AD 11 D0 LDA $D011   ; read the vertical fine scroll and control register
.F890  29 EF    AND #$EF   ; mask xxx0 xxxx, blank the screen
.F892  8D 11 D0 STA $D011   ; save the vertical fine scroll and control register
.F895  AD 14 03 LDA $0314   ; get IRQ vector low byte
.F898  8D 9F 02 STA $029F   ; save IRQ vector low byte
.F89B  AD 15 03 LDA $0315   ; get IRQ vector high byte
.F89E  8D A0 02 STA $02A0   ; save IRQ vector high byte
.F8A1  20 BD FC JSR $FCBD   ; set the tape vector
.F8A4  A9 02    LDA #$02   ; set copies count. the first copy is the load copy, the second copy is the verify copy
.F8A6  85 BE    STA $BE   ; save copies count
.F8A8  20 97 FB JSR $FB97   ; new tape byte setup
.F8AB  A5 01    LDA $01   ; read the 6510 I/O port
.F8AD  29 1F    AND #$1F   ; mask 000x xxxx, cassette motor on ??
.F8AF  85 01    STA $01   ; save the 6510 I/O port
.F8B1  85 C0    STA $C0   ; set the tape motor interlock 326656 cycle delay, allow tape motor speed to stabilise
.F8B3  A2 FF    LDX #$FF   ; outer loop count
.F8B5  A0 FF    LDY #$FF   ; inner loop count
.F8B7  88       DEY   ; decrement inner loop count
.F8B8  D0 FD    BNE $F8B7   ; loop if more to do
.F8BA  CA       DEX   ; decrement outer loop count
.F8BB  D0 F8    BNE $F8B5   ; loop if more to do
.F8BD  58       CLI   ; enable tape interrupts
.F8BE  AD A0 02 LDA $02A0   ; get saved IRQ high byte
.F8C1  CD 15 03 CMP $0315   ; compare with the current IRQ high byte
.F8C4  18       CLC   ; flag ok
.F8C5  F0 15    BEQ $F8DC   ; if tape write done go clear saved IRQ address and exit
.F8C7  20 D0 F8 JSR $F8D0   ; scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
.F8CA  20 BC F6 JSR $F6BC   ; increment real time clock
.F8CD  4C BE F8 JMP $F8BE   ; loop
```


## Commenti

### Original Disassembly (—)
- **$F875**: disable all interrupts
- **$F877**: save VIA 1 ICR, disable all interrupts
- **$F87A**: save VIA 1 ICR, enable interrupts according to A check RS232 bus idle
- **$F87D**: read VIA 1 CRA
- **$F880**: load timer B, timer B single shot, start timer B
- **$F882**: save VIA 1 CRB
- **$F885**: mask x00x 000x, TOD clock, load timer A, start timer A
- **$F887**: save VIA 1 CRB shadow copy
- **$F88D**: read the vertical fine scroll and control register
- **$F890**: mask xxx0 xxxx, blank the screen
- **$F892**: save the vertical fine scroll and control register
- **$F895**: get IRQ vector low byte
- **$F898**: save IRQ vector low byte
- **$F89B**: get IRQ vector high byte
- **$F89E**: save IRQ vector high byte
- **$F8A1**: set the tape vector
- **$F8A4**: set copies count. the first copy is the load copy, the second copy is the verify copy
- **$F8A6**: save copies count
- **$F8A8**: new tape byte setup
- **$F8AB**: read the 6510 I/O port
- **$F8AD**: mask 000x xxxx, cassette motor on ??
- **$F8AF**: save the 6510 I/O port
- **$F8B1**: set the tape motor interlock 326656 cycle delay, allow tape motor speed to stabilise
- **$F8B3**: outer loop count
- **$F8B5**: inner loop count
- **$F8B7**: decrement inner loop count
- **$F8B8**: loop if more to do
- **$F8BA**: decrement outer loop count
- **$F8BB**: loop if more to do
- **$F8BD**: enable tape interrupts
- **$F8BE**: get saved IRQ high byte
- **$F8C1**: compare with the current IRQ high byte
- **$F8C4**: flag ok
- **$F8C5**: if tape write done go clear saved IRQ address and exit
- **$F8C7**: scan stop key and flag abort if pressed note if STOP was pressed the return is to the routine that called this one and not here
- **$F8CA**: increment real time clock
- **$F8CD**: loop

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*