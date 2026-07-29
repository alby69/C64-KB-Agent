---
title: setup next RS232 Tx byte
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
- ef06-send-new-rs232-byte
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  - magnus_nyman.txt
  address: $EF06
  address_end: $EF2D
  symbol: setup-next-rs232-tx-byte
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF06**: read the 6551 pseudo command register'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EF06**: M51CDR, 6551 command register'
---

# $EF06 — setup next RS232 Tx byte

## Disassemblatura
```assembly
.EF06  AD 94 02 LDA $0294   ; read the 6551 pseudo command register
.EF09  4A       LSR   ; handshake bit into Cb
.EF0A  90 07    BCC $EF13   ; if 3 line interface go ??
.EF0C  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.EF0F  10 1D    BPL $EF2E   ; if DSR = 0 set DSR signal not present and exit
.EF11  50 1E    BVC $EF31   ; if CTS = 0 set CTS signal not present and exit was 3 line interface
.EF13  A9 00    LDA #$00   ; clear A
.EF15  85 BD    STA $BD   ; clear the RS232 parity byte
.EF17  85 B5    STA $B5   ; clear the RS232 next bit to send
.EF19  AE 98 02 LDX $0298   ; get the number of bits to be sent/received
.EF1C  86 B4    STX $B4   ; set the RS232 bit count
.EF1E  AC 9D 02 LDY $029D   ; get the index to the Tx buffer start
.EF21  CC 9E 02 CPY $029E   ; compare it with the index to the Tx buffer end
.EF24  F0 13    BEQ $EF39   ; if all done go disable T?? interrupt and return
.EF26  B1 F9    LDA ($F9),Y   ; else get a byte from the buffer
.EF28  85 B6    STA $B6   ; save it to the RS232 output byte buffer
.EF2A  EE 9D 02 INC $029D   ; increment the index to the Tx buffer start
.EF2D  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EF06**: read the 6551 pseudo command register
- **$EF09**: handshake bit into Cb
- **$EF0A**: if 3 line interface go ??
- **$EF0C**: test VIA 2 DRB, RS232 port
- **$EF0F**: if DSR = 0 set DSR signal not present and exit
- **$EF11**: if CTS = 0 set CTS signal not present and exit was 3 line interface
- **$EF13**: clear A
- **$EF15**: clear the RS232 parity byte
- **$EF17**: clear the RS232 next bit to send
- **$EF19**: get the number of bits to be sent/received
- **$EF1C**: set the RS232 bit count
- **$EF1E**: get the index to the Tx buffer start
- **$EF21**: compare it with the index to the Tx buffer end
- **$EF24**: if all done go disable T?? interrupt and return
- **$EF26**: else get a byte from the buffer
- **$EF28**: save it to the RS232 output byte buffer
- **$EF2A**: increment the index to the Tx buffer start

### Magnus Nyman (Magnus Nyman)
- **$EF06**: M51CDR, 6551 command register
- **$EF09**: test handshake mode
- **$EF0A**: 3-line mode (no handshake)
- **$EF0C**: RS232 port
- **$EF0F**: no DSR, error
- **$EF11**: no CTS, error
- **$EF15**: ROPRTY, RS232 out parity
- **$EF17**: NXTBIT, next bit to send
- **$EF19**: BITNUM, number of bits left to send
- **$EF1C**: BITTS, RS232 out bit count
- **$EF1E**: RODBS, start page of out buffer
- **$EF21**: RODBE, index to end if out buffer
- **$EF24**: disable timer
- **$EF26**: RS232 out buffer
- **$EF28**: RODATA, RS232 out byte buffer
- **$EF2A**: RODBS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*