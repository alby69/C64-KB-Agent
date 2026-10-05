---
id: eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0
type: entity
title: do RS232 parity bit, enters with RS232 bit count = 0
aliases:
- do RS232 parity bit, enters with RS232 bit count = 0
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0.md
  sha256: 99afb076267701c80bae0d3fbee3a081a8a08c0cbae08f186fe9d7e704d35297
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0
---

# do RS232 parity bit, enters with RS232 bit count = 0



# $EED7 — do RS232 parity bit, enters with RS232 bit count = 0

## Disassemblatura
```assembly
.EED7  A9 20    LDA #$20   ; mask 00x0 0000, parity enable bit
.EED9  2C 94 02 BIT $0294   ; test the pseudo 6551 command register
.EEDC  F0 14    BEQ $EEF2   ; if parity disabled go ??
.EEDE  30 1C    BMI $EEFC   ; if fixed mark or space parity go ??
.EEE0  70 14    BVS $EEF6   ; if even parity go ?? else odd parity
.EEE2  A5 BD    LDA $BD   ; get RS232 parity byte
.EEE4  D0 01    BNE $EEE7   ; if parity not zero leave parity bit = 0
.EEE6  CA       DEX   ; make parity bit = 1
.EEE7  C6 B4    DEC $B4   ; decrement RS232 bit count, 1 stop bit
.EEE9  AD 93 02 LDA $0293   ; get pseudo 6551 control register
.EEEC  10 E3    BPL $EED1   ; if 1 stop bit save parity bit and exit else two stop bits ..
.EEEE  C6 B4    DEC $B4   ; decrement RS232 bit count, 2 stop bits
.EEF0  D0 DF    BNE $EED1   ; save bit and exit, branch always parity is disabled so the parity bit becomes the first, and possibly only, stop bit. to do this increment the bit count which effectively decrements the stop bit count.
.EEF2  E6 B4    INC $B4   ; increment RS232 bit count, = -1 stop bit
.EEF4  D0 F0    BNE $EEE6   ; set stop bit = 1 and exit do even parity
.EEF6  A5 BD    LDA $BD   ; get RS232 parity byte
.EEF8  F0 ED    BEQ $EEE7   ; if parity zero leave parity bit = 0
.EEFA  D0 EA    BNE $EEE6   ; else make parity bit = 1, branch always fixed mark or space parity
.EEFC  70 E9    BVS $EEE7   ; if fixed space parity leave parity bit = 0
.EEFE  50 E6    BVC $EEE6   ; else fixed mark parity make parity bit = 1, branch always decrement stop bit count, set stop bit = 1 and exit. $FF is one stop bit, $FE is two stop bits
.EF00  E6 B4    INC $B4   ; decrement RS232 bit count
.EF02  A2 FF    LDX #$FF   ; set stop bit = 1
.EF04  D0 CB    BNE $EED1   ; save stop bit and exit, branch always
```


## Commenti

### Original Disassembly (—)
- **$EED7**: mask 00x0 0000, parity enable bit
- **$EED9**: test the pseudo 6551 command register
- **$EEDC**: if parity disabled go ??
- **$EEDE**: if fixed mark or space parity go ??
- **$EEE0**: if even parity go ?? else odd parity
- **$EEE2**: get RS232 parity byte
- **$EEE4**: if parity not zero leave parity bit = 0
- **$EEE6**: make parity bit = 1
- **$EEE7**: decrement RS232 bit count, 1 stop bit
- **$EEE9**: get pseudo 6551 control register
- **$EEEC**: if 1 stop bit save parity bit and exit else two stop bits ..
- **$EEEE**: decrement RS232 bit count, 2 stop bits
- **$EEF0**: save bit and exit, branch always parity is disabled so the parity bit becomes the first, and possibly only, stop bit. to do this increment the bit count which effectively decrements the stop bit count.
- **$EEF2**: increment RS232 bit count, = -1 stop bit
- **$EEF4**: set stop bit = 1 and exit do even parity
- **$EEF6**: get RS232 parity byte
- **$EEF8**: if parity zero leave parity bit = 0
- **$EEFA**: else make parity bit = 1, branch always fixed mark or space parity
- **$EEFC**: if fixed space parity leave parity bit = 0
- **$EEFE**: else fixed mark parity make parity bit = 1, branch always decrement stop bit count, set stop bit = 1 and exit. $FF is one stop bit, $FE is two stop bits
- **$EF00**: decrement RS232 bit count
- **$EF02**: set stop bit = 1
- **$EF04**: save stop bit and exit, branch always

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-eed7-do-rs232-parity-bit-enters-with-rs232-bit-count-0]]
