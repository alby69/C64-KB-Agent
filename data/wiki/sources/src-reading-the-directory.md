---
id: src-reading-the-directory
type: source
title: 'Source Summary: Reading the directory'
aliases:
- Reading the directory
- reading_the_directory.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/reading_the_directory.md
  sha256: 9e193c5ac2b4f9108ee9638bcff7441dbdf95be617b76a9f7da9f1740cc75917
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Reading the directory

**Raw Source File**: `data/docs/codebase_c64_org/base/reading_the_directory.md`
**SHA256**: `9e193c5ac2b4f9108ee9638bcff7441dbdf95be617b76a9f7da9f1740cc75917`

## Summary




# Reading the directory

base:reading_the_directory

                # Reading the directory

Just a simple routine which reads the directory file from a device and prints it to screen.

```
        LDA #dirname_end-dirname
        LDX #<dirname
        LDY #>dirname
        JSR $FFBD      ; call SETNAM
        LDA #$02       ; filenumber 2
        LDX $BA
        BNE .skip
        LDX #$08       ; default to device number 8
.skip   LDY #$00       ; secondary address 0 (required for dir readi...
