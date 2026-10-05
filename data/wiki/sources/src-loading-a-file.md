---
id: src-loading-a-file
type: source
title: 'Source Summary: Loading a file to memory at address stored in file'
aliases:
- Loading a file to memory at address stored in file
- loading_a_file.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/loading_a_file.md
  sha256: 668b22dcf97b4178f1e3b12e778b97ee18bea8cad9e72bd53dfae2b574eccbfa
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Loading a file to memory at address stored in file

**Raw Source File**: `data/docs/codebase_c64_org/base/loading_a_file.md`
**SHA256**: `668b22dcf97b4178f1e3b12e778b97ee18bea8cad9e72bd53dfae2b574eccbfa`

## Summary



# Loading a file to memory at address stored in file

base:loading_a_file

                # Loading a file to memory at address stored in file

BASIC code:

LOAD "JUST A FILENAME",8,1

Assembler code:

```
        LDA #fname_end-fname
        LDX #<fname
        LDY #>fname
        JSR $FFBD     ; call SETNAM
        LDA #$01
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$01      ; not $01 means: load to address stor...
