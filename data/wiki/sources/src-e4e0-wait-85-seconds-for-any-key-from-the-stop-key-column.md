---
id: src-e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column
type: source
title: 'Source Summary: wait ~8.5 seconds for any key from the STOP key column'
aliases:
- wait ~8.5 seconds for any key from the STOP key column
- e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column.md
  sha256: 421ca4c8287418719c407807487659a6e5ebe8f1f837bb20adcb45a9b8c48471
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: wait ~8.5 seconds for any key from the STOP key column

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/e4e0-wait-85-seconds-for-any-key-from-the-stop-key-column.md`
**SHA256**: `421ca4c8287418719c407807487659a6e5ebe8f1f837bb20adcb45a9b8c48471`

## Summary



# $E4E0 — wait ~8.5 seconds for any key from the STOP key column

## Disassemblatura
```assembly
.E4E0  69 02    ADC #$02   ; set the number of jiffies to wait
.E4E2  A4 91    LDY $91   ; read the stop key column
.E4E4  C8       INY   ; test for $FF, no keys pressed
.E4E5  D0 04    BNE $E4EB   ; if any keys were pressed just exit
.E4E7  C5 A1    CMP $A1   ; compare the wait time with the jiffy clock mid byte
.E4E9  D0 F7    BNE $E4E2   ; if not there yet go wait some more
.E4EB  60       RTS
`...
