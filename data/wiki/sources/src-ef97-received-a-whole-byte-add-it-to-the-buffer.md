---
id: src-ef97-received-a-whole-byte-add-it-to-the-buffer
type: source
title: 'Source Summary: received a whole byte, add it to the buffer'
aliases:
- received a whole byte, add it to the buffer
- ef97-received-a-whole-byte-add-it-to-the-buffer.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ef97-received-a-whole-byte-add-it-to-the-buffer.md
  sha256: a48e18dba36c468d6651383293db18f6c5083402fc670cc445c89232b81c6431
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: received a whole byte, add it to the buffer

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ef97-received-a-whole-byte-add-it-to-the-buffer.md`
**SHA256**: `a48e18dba36c468d6651383293db18f6c5083402fc670cc445c89232b81c6431`

## Summary



# $EF97 — received a whole byte, add it to the buffer

## Disassemblatura
```assembly
.EF97  AC 9B 02 LDY $029B   ; get index to Rx buffer end
.EF9A  C8       INY   ; increment index
.EF9B  CC 9C 02 CPY $029C   ; compare with index to Rx buffer start
.EF9E  F0 2A    BEQ $EFCA   ; if buffer full go do Rx overrun error
.EFA0  8C 9B 02 STY $029B   ; save index to Rx buffer end
.EFA3  88       DEY   ; decrement index
.EFA4  A5 AA    LDA $AA   ; get assembled byte
.EFA6  AE 98 02 LDX $0298   ; get ...
