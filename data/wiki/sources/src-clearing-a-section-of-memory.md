---
id: src-clearing-a-section-of-memory
type: source
title: 'Source Summary: Clearing a Section of Memory'
aliases:
- Clearing a Section of Memory
- clearing_a_section_of_memory.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/clearing_a_section_of_memory.md
  sha256: 5e83f03b75777a1fbe0d6acc3759f651257c359d275860f92985a1eb3e3d7f9f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Clearing a Section of Memory

**Raw Source File**: `data/docs/codebase_c64_org/base/clearing_a_section_of_memory.md`
**SHA256**: `5e83f03b75777a1fbe0d6acc3759f651257c359d275860f92985a1eb3e3d7f9f`

## Summary



# Clearing a Section of Memory

# Clearing a Section of Memory

from 6502 Software Gourmet Guide & Cookbook

When setting up a program for entering data or storing the results of a calculation, it is often desirable to clear the memory locations to be used for storage. This operation is achieved by filling the memory locations with zeros. One way to do this is to store zero in the accumulator and perform a series of STA ADDR instructions in which the ADDR designates each memory location to be ...
