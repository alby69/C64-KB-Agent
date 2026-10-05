---
id: src-ef39-disable-timer-a-interrupt
type: source
title: 'Source Summary: disable timer A interrupt'
aliases:
- disable timer A interrupt
- ef39-disable-timer-a-interrupt.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef39-disable-timer-a-interrupt.md
  sha256: a612882d9b61af999b6ca938cf61deddd39083566ca9099f03b9519a3fd058d1
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: disable timer A interrupt

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef39-disable-timer-a-interrupt.md`
**SHA256**: `a612882d9b61af999b6ca938cf61deddd39083566ca9099f03b9519a3fd058d1`

## Summary



# $EF39 — disable timer A interrupt

## Disassemblatura
```assembly
.EF39  A9 01    LDA #$01   ; disable timer A interrupt
```


## Commenti

### Original Disassembly (—)
- **$EF39**: disable timer A interrupt

### Magnus Nyman (Magnus Nyman)
- **$EF39**: ; CIA#2 interrupt control register
- **$EF3B**: ; ENABL, RS232 enables
- **$EF41**: ; ENABL
- **$EF43**: ; CIA#2 interrupt control register

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*...
