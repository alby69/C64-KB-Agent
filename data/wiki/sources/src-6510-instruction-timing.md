---
id: src-6510-instruction-timing
type: source
title: 'Source Summary: 6510 Instruction Timing'
aliases:
- 6510 Instruction Timing
- 6510_instruction_timing.md
tags:
- raster interrupts
- assembly
- sprite programming
- memory management
sources:
- path: data/docs/codebase_c64_org/base/6510_instruction_timing.md
  sha256: 7b2ab8df057fddcc72669c5bd3fe1174710c5695bc12054f18c37c478a88c101
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 6510 Instruction Timing

**Raw Source File**: `data/docs/codebase_c64_org/base/6510_instruction_timing.md`
**SHA256**: `7b2ab8df057fddcc72669c5bd3fe1174710c5695bc12054f18c37c478a88c101`

## Summary



# 6510 Instruction Timing

# 6510 Instruction Timing

The NMOS 6500 series processors always perform at least two reads for each instruction. In addition to the operation code (opcode), they fetch the next byte. This is quite efficient, as most instructions are two or three bytes long.

The processors also use a sort of pipelining. If an instruction does not store data in memory on its last cycle, the processor can fetch the opcode of the next instruction while executing the last cycle. For in...
