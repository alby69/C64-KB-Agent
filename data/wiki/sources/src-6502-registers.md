---
id: src-6502-registers
type: source
title: 'Source Summary: 6502 Registers'
aliases:
- 6502 Registers
- 6502_registers.md
tags:
- raster interrupts
- assembly
- sprite programming
- memory management
sources:
- path: data/docs/codebase_c64_org/base/6502_registers.md
  sha256: 9dcb1cf7bd1c2204fc673824f9c0070433c58bf3b2eec12b3c78d1d6a6b1fdb5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 6502 Registers

**Raw Source File**: `data/docs/codebase_c64_org/base/6502_registers.md`
**SHA256**: `9dcb1cf7bd1c2204fc673824f9c0070433c58bf3b2eec12b3c78d1d6a6b1fdb5`

## Summary



# 6502 Registers

base:6502_registers

                # 6502 Registers

The NMOS 65xx processors are not ruined with too many registers. In addition to that, the registers are mostly 8-bit. Here is a brief description of each register:

```
       PC   Program Counter
            This register points the address from which the next
            instruction byte (opcode or parameter) will be fetched.
            Unlike other registers, this one is 16 bits in length. The
            low and high...
