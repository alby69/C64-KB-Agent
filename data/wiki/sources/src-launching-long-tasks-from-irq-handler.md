---
id: src-launching-long-tasks-from-irq-handler
type: source
title: 'Source Summary: Launching long tasks from inside a IRQ handler'
aliases:
- Launching long tasks from inside a IRQ handler
- launching_long_tasks_from_irq_handler.md
tags:
- raster interrupts
- basic
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/launching_long_tasks_from_irq_handler.md
  sha256: be0641d7a1a6bde469ec6ff92914aa85502d71302b541bcdeae82e4701b2d7f2
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Launching long tasks from inside a IRQ handler

**Raw Source File**: `data/docs/codebase_c64_org/base/launching_long_tasks_from_irq_handler.md`
**SHA256**: `be0641d7a1a6bde469ec6ff92914aa85502d71302b541bcdeae82e4701b2d7f2`

## Summary




# Launching long tasks from inside a IRQ handler

# Launching long tasks from inside a IRQ handler

by Bitbreaker/Oxyron/*

When executing code within an IRQ handler you have to finish things before the next IRQ occurs. But sometimes tasks just take some more time, for that you can spin off those tasks from inside the handler, and allow then upcoming IRQs to happen.

Basically there is two scenarios that we can handle in an easy and an more sophisticated way. The first scenario is, if you hav...
