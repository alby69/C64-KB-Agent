---
id: src-makefile-to-use-with-ca65-vice
type: source
title: 'Source Summary: base:makefile_to_use_with_ca65_vice [Codebase64 wiki]'
aliases:
- base:makefile_to_use_with_ca65_vice [Codebase64 wiki]
- makefile_to_use_with_ca65_vice.md
tags:
- raster interrupts
sources:
- path: data/docs/codebase_c64_org/base/makefile_to_use_with_ca65_vice.md
  sha256: 862924b97e78bba90be59b2bb48c65bb3a77613cc02cea81bdcad06baa10ab3b
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: base:makefile_to_use_with_ca65_vice [Codebase64 wiki]

**Raw Source File**: `data/docs/codebase_c64_org/base/makefile_to_use_with_ca65_vice.md`
**SHA256**: `862924b97e78bba90be59b2bb48c65bb3a77613cc02cea81bdcad06baa10ab3b`

## Summary



# base:makefile_to_use_with_ca65_vice [Codebase64 wiki]

base:makefile_to_use_with_ca65_vice

                Simple Makefile for ca65 projects, that puts compiled binary to .d64 files, and also shows the directory. Variation of this is used in practically all of my modern C64 projects.

“make run” also passes labels to VICE monitor for easier debugging.

Tested on Ubuntu & MorphOS.

CPU = 6502
C1541 = c1541
# Also pass symbols to VICE monitor
X64 = x64 -moncommands symbols
OUTPUT = "diskconte...
