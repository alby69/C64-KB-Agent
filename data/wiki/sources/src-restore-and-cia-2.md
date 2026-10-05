---
id: src-restore-and-cia-2
type: source
title: 'Source Summary: Surviving Restore key presses while using CIA 2 timer NMIs'
aliases:
- Surviving Restore key presses while using CIA 2 timer NMIs
- restore_and_cia_2.md
tags:
- raster interrupts
- assembly
sources:
- path: data/docs/codebase_c64_org/base/restore_and_cia_2.md
  sha256: 897de39b849815e5ecaa917b6818b4a29fcb7b5d6c5aebe5296f93a3aedfda21
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Surviving Restore key presses while using CIA 2 timer NMIs

**Raw Source File**: `data/docs/codebase_c64_org/base/restore_and_cia_2.md`
**SHA256**: `897de39b849815e5ecaa917b6818b4a29fcb7b5d6c5aebe5296f93a3aedfda21`

## Summary



# Surviving Restore key presses while using CIA 2 timer NMIs

# Surviving Restore key presses while using CIA 2 timer NMIs

by White Flame

The /NMI pulse from the restore key seems to be longer than 1 frame. When this happens, the CIA 2 interrupt source doesn't cause the NMI to trigger, so the timer never gets ACKed, and NMIs appear to stop as /NMI is locked low, even though the timer is still running.

```
Restore   _______________2                          ____________________
key          ...
