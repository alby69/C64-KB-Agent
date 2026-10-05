---
id: src-sprite-data-and-kickassembler
type: source
title: 'Source Summary: Using KickAss to include .gif sprite data'
aliases:
- Using KickAss to include .gif sprite data
- sprite_data_and_kickassembler.md
tags:
- sprite programming
- graphics
- assembly
sources:
- path: data/docs/codebase_c64_org/base/sprite_data_and_kickassembler.md
  sha256: 61fd0c3475081fdbe52c91ba33b5e32c697404fae6947986ca6be8dfa4f4a249
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Using KickAss to include .gif sprite data

**Raw Source File**: `data/docs/codebase_c64_org/base/sprite_data_and_kickassembler.md`
**SHA256**: `61fd0c3475081fdbe52c91ba33b5e32c697404fae6947986ca6be8dfa4f4a249`

## Summary



# Using KickAss to include .gif sprite data

base:sprite_data_and_kickassembler

                # Using KickAss to include .gif sprite data

[KickAssembler](http://www.theweb.dk/KickAssembler/Main.php) aka KickAss is a multi platform crossassembler written in Java with some nice features when it comes to handling graphics data. The author of KickAss (Slammer) provided the following example on how to easily make sprite data out of .gif images just by using a rather simple macro:

```
.pc = $30...
