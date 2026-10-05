---
id: src-saving-a-file
type: source
title: 'Source Summary: Saving a memory range to a file'
aliases:
- Saving a memory range to a file
- saving_a_file.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/saving_a_file.md
  sha256: ebf661b61e458171cfe90499f6c90f7911a016f4ceb6dbe28756cbb575a629d9
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Saving a memory range to a file

**Raw Source File**: `data/docs/codebase_c64_org/base/saving_a_file.md`
**SHA256**: `ebf661b61e458171cfe90499f6c90f7911a016f4ceb6dbe28756cbb575a629d9`

## Summary



# Saving a memory range to a file

base:saving_a_file

                # Saving a memory range to a file

```
file_start = $2000    ; example addresses
file_end   = $4000
        LDA #fname_end-fname
        LDX #<fname
        LDY #>fname
        JSR $FFBD     ; call SETNAM
        LDA #$00
        LDX $BA       ; last used device number
        BNE .skip
        LDX #$08      ; default to device 8
.skip   LDY #$00
        JSR $FFBA     ; call SETLFS
        LDA #<file_start
        STA $C1
 ...
