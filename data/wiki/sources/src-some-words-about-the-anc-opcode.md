---
id: src-some-words-about-the-anc-opcode
type: source
title: 'Source Summary: Some words about the ANC opcode'
aliases:
- Some words about the ANC opcode
- some_words_about_the_anc_opcode.md
tags:
- assembly
sources:
- path: data/docs/codebase_c64_org/base/some_words_about_the_anc_opcode.md
  sha256: 1b4eaaed6f1d0a69c5bf800c5d7b4a55262486d16306b69a1f10d5f6586dbe13
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Some words about the ANC opcode

**Raw Source File**: `data/docs/codebase_c64_org/base/some_words_about_the_anc_opcode.md`
**SHA256**: `1b4eaaed6f1d0a69c5bf800c5d7b4a55262486d16306b69a1f10d5f6586dbe13`

## Summary



# Some words about the ANC opcode

# Some words about the ANC opcode

Written by FTC/HT.

Like many other illegal opcodes the ANC instruction performs “two operations in one”, and as is also often the case, one of these two operations is an AND operation. The ANC opcode only exist in the “immediate” version (ANC #$ff) and it works like this:

1. AND immediate value (#$xx) with A, and store result in A.
2. Put highest bit of the result in the carry.

## When is ANC useful?

Here are some cases ...
