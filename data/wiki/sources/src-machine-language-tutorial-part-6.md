---
id: src-machine-language-tutorial-part-6
type: source
title: 'Source Summary: Part 6 - The Stack'
aliases:
- Part 6 - The Stack
- machine_language_tutorial_part_6.md
tags:
- sprite programming
- assembly
sources:
- path: data/docs/codebase_c64_org/base/machine_language_tutorial_part_6.md
  sha256: a2090a0e0a18588e22910e581d1c068d1e54482296e1633e9227f4371e028486
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Part 6 - The Stack

**Raw Source File**: `data/docs/codebase_c64_org/base/machine_language_tutorial_part_6.md`
**SHA256**: `a2090a0e0a18588e22910e581d1c068d1e54482296e1633e9227f4371e028486`

## Summary



# Part 6 - The Stack

### Table of Contents

# Part 6 - The Stack

The stack, located at $0100-$01FF, is a helpful place to store temporary values. It can be imagined as a stack of paper, with each sheet holding one byte of information. You can push a sheet on top of the stack, or pull the topmost sheet off the stack. This principle is formally known as last-in, first-out (LIFO).

## The Stack Pointer

The stack pointer is an index from $0100 that tells the CPU where to push the next stack val...
