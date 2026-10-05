---
id: src-dos-examples
type: source
title: 'Source Summary: High level KERNAL examples'
aliases:
- High level KERNAL examples
- dos_examples.md
tags:
- basic
sources:
- path: data/docs/codebase_c64_org/base/dos_examples.md
  sha256: e2780590631d262c89fbb3121fa671113884f6df8fc40412d98a6e15cf906e33
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: High level KERNAL examples

**Raw Source File**: `data/docs/codebase_c64_org/base/dos_examples.md`
**SHA256**: `e2780590631d262c89fbb3121fa671113884f6df8fc40412d98a6e15cf906e33`

## Summary



# High level KERNAL examples

base:dos_examples

                # High level KERNAL examples

Be aware that some of these KERNAL routines call SEI and CLI, so if you have interrupts running in your program, be sure to disable your interrupts properly (i.e. do not only do SEI) before calling these routines in case you don't want the interrupts to be re-enabled by the KERNAL code. Also note that BASIC ROM can be disabled when doing disk IO (except for the DIR routine here, which calls one of th...
