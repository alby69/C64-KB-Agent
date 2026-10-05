---
id: ef90-no-rs232-start-bit-received
type: entity
title: no RS232 start bit received
aliases:
- no RS232 start bit received
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef90-no-rs232-start-bit-received.md
  sha256: 98cbcaf76a7ae6377c2374d942b470c47329550c76d2856e757382e228e17e36
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-ef90-no-rs232-start-bit-received
---

# no RS232 start bit received



# $EF90 — no RS232 start bit received

## Disassemblatura
```assembly
.EF90  A5 A7    LDA $A7   ; get the RS232 received data bit
.EF92  D0 EA    BNE $EF7E   ; if ?? go setup to receive an RS232 bit and return
.EF94  4C D3 E4 JMP $E4D3   ; flag the RS232 start bit and set the parity
```


## Commenti

### Original Disassembly (—)
- **$EF90**: get the RS232 received data bit
- **$EF92**: if ?? go setup to receive an RS232 bit and return
- **$EF94**: flag the RS232 start bit and set the parity

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EF90**: INBIT, RS232 in bits
- **$EF92**: set up to receive
- **$EF94**: patch, init parity byte
- **$EF97**: RIDBE, index to the end of in buffer
- **$EF9B**: RIDBS, start page of in buffer
- **$EF9E**: receive overflow error
- **$EFA0**: RIDBE
- **$EFA4**: RIDATA, RS232 in byte buffer
- **$EFA6**: BITNUM, number of bits left to send
- **$EFA9**: full word to come?
- **$EFAB**: yes
- **$EFB1**: RIBUF, RS232 in buffer
- **$EFB5**: M51CDR, 6551 command register image
- **$EFB8**: parity disabled
- **$EFBA**: parity check disabled, TRS
- **$EFBC**: INBIT, parity check
- **$EFBE**: RIPRTY, RS232 in parity
- **$EFC0**: receive parity error
- **$EFC4**: mask
- **$EFC7**: receive parity error
- **$EFC9**: mask
- **$EFCA**: receive overflow
- **$EFCC**: mask
- **$EFCD**: framing break
- **$EFCF**: mask
- **$EFD0**: framing error
- **$EFD2**: RSSTAT, 6551 status register image
- **$EFD8**: set up to receive
- **$EFDB**: RIDATA
- **$EFDD**: framing error
- **$EFDF**: receive break

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-ef90-no-rs232-start-bit-received]]
