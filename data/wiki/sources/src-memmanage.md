---
id: src-memmanage
type: source
title: 'Source Summary: Memory Management'
aliases:
- Memory Management
- memmanage.md
tags:
- sprite programming
- input handling
- basic
- graphics
- assembly
- raster interrupts
- sound generation
- memory management
sources:
- path: data/docs/codebase_c64_org/base/memmanage.md
  sha256: 4dcdb45fb9f72452ccebb3b2f9bb8abcd682ffafe00863d7fe41ecbb59379597
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Memory Management

**Raw Source File**: `data/docs/codebase_c64_org/base/memmanage.md`
**SHA256**: `4dcdb45fb9f72452ccebb3b2f9bb8abcd682ffafe00863d7fe41ecbb59379597`

## Summary




# Memory Management

### Table of Contents

# Memory Management

## The processor's point of view

The Commodore 64 has access to more memory than its processor can directly handle. This is possible by banking the memory. There are five user configurable inputs that affect the banking. Three of them can be controlled by program, and the rest two serve as control lines on the memory expansion port.

The 6510 MPU has an integrated I/O port with six I/O lines. This port is accessed through the m...
