---
id: src-common-pitfalls
type: source
title: 'Source Summary: Common Coding Pitfalls'
aliases:
- Common Coding Pitfalls
- common_pitfalls.md
tags:
- raster interrupts
- sprite programming
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/common_pitfalls.md
  sha256: 4f773736c48ec8df72d30e651af794b46c0bb0e5902d635aa3b2fdadddb2e0b0
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Common Coding Pitfalls

**Raw Source File**: `data/docs/codebase_c64_org/base/common_pitfalls.md`
**SHA256**: `4f773736c48ec8df72d30e651af794b46c0bb0e5902d635aa3b2fdadddb2e0b0`

## Summary




# Common Coding Pitfalls

### Table of Contents

# Common Coding Pitfalls

There are many Coding Pitfalls, each coder has its own (as well as its own style). This Page is meant as a Collection about many Errors, feel free to add your own.

Please note that we have separate Articles about various Initialisation Issues.

## The DOKE-Dilemma

To put an “immediate” 16bit value into two adjacent Memory-Addresses is a common task. We 6502 Coders agree to store all 16bit values low-byte-first, msb-b...
