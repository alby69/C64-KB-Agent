---
id: src-edfe-command-serial-bus-to-unlisten
type: source
title: 'Source Summary: command serial bus to UNLISTEN'
aliases:
- command serial bus to UNLISTEN
- edfe-command-serial-bus-to-unlisten.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/edfe-command-serial-bus-to-unlisten.md
  sha256: b46a4271a324f85e7b6d77d73ea26d923b3e0d2c3a543997ccd73469e7bb29da
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: command serial bus to UNLISTEN

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/edfe-command-serial-bus-to-unlisten.md`
**SHA256**: `b46a4271a324f85e7b6d77d73ea26d923b3e0d2c3a543997ccd73469e7bb29da`

## Summary



# $EDFE — command serial bus to UNLISTEN

## Disassemblatura
```assembly
.EDFE  A9 3F    LDA #$3F   ; set the UNLISTEN command
.EE00  20 11 ED JSR $ED11   ; send a control character
.EE03  20 BE ED JSR $EDBE   ; set serial ATN high 1ms delay, clock high then data high
.EE06  8A       TXA   ; save the device number
.EE07  A2 0A    LDX #$0A   ; short delay
.EE09  CA       DEX   ; decrement the count
.EE0A  D0 FD    BNE $EE09   ; loop if not all done
.EE0C  AA       TAX   ; restore the device num...
