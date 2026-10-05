---
id: src-ef90-no-rs232-start-bit-received
type: source
title: 'Source Summary: no RS232 start bit received'
aliases:
- no RS232 start bit received
- ef90-no-rs232-start-bit-received.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef90-no-rs232-start-bit-received.md
  sha256: 98cbcaf76a7ae6377c2374d942b470c47329550c76d2856e757382e228e17e36
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: no RS232 start bit received

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef90-no-rs232-start-bit-received.md`
**SHA256**: `98cbcaf76a7ae6377c2374d942b470c47329550c76d2856e757382e228e17e36`

## Summary



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

...
