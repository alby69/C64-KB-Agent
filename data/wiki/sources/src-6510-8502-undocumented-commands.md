---
id: src-6510-8502-undocumented-commands
type: source
title: 'Source Summary: 6510/8502 Undocumented Commands'
aliases:
- 6510/8502 Undocumented Commands
- 6510_8502_undocumented_commands.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/6510_8502_undocumented_commands.md
  sha256: d6b00989a09baa2c3d7ae2ece3da0bf6eee16779f9bb398edd368cbdd1b14a5e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: 6510/8502 Undocumented Commands

**Raw Source File**: `data/docs/codebase_c64_org/base/6510_8502_undocumented_commands.md`
**SHA256**: `d6b00989a09baa2c3d7ae2ece3da0bf6eee16779f9bb398edd368cbdd1b14a5e`

## Summary



# 6510/8502 Undocumented Commands

base:6510_8502_undocumented_commands

                # 6510/8502 Undocumented Commands

```````````````
         -- A brief explanation about what may happen while
                using don't care states.
        ANE $8B         A = (A | #$EE) & X & #byte
                        same as
                        A = ((A & #$11 & X) | ( #$EE & X)) & #byte
                        In real 6510/8502 the internal parameter #$11
                        may occasiona...
