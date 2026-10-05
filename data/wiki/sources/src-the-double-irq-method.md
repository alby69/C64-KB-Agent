---
id: src-the-double-irq-method
type: source
title: 'Source Summary: The double (raster) IRQ method'
aliases:
- The double (raster) IRQ method
- the_double_irq_method.md
tags:
- raster interrupts
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/the_double_irq_method.md
  sha256: aae3afec228bab5dddfa9b57da9263b921b3ece2e886da5a2ecd8424492509c7
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: The double (raster) IRQ method

**Raw Source File**: `data/docs/codebase_c64_org/base/the_double_irq_method.md`
**SHA256**: `aae3afec228bab5dddfa9b57da9263b921b3ece2e886da5a2ecd8424492509c7`

## Summary




# The double (raster) IRQ method

# The double (raster) IRQ method

## Theory

This method is one of the more easy methods to grasp when it comes to stable timing. The following explanation of the method assumed you've accustomed yourself to the previous articles in this series.

As stated earlier a raster IRQ will trigger at cycle 0 on the chosen scanline, but due to the fact that the CPU must finish the current opcode + that the CPU needs 7 cycles to actually save the state and move the PC ...
