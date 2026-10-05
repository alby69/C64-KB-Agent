---
id: src-scpu-setscrncol
type: source
title: 'Source Summary: PSEUDOCOMMAND'
aliases:
- PSEUDOCOMMAND
- scpu_setscrncol.md
tags:
- basic
- assembly
sources:
- path: data/docs/codebase_c64_org/base/scpu_setscrncol.md
  sha256: ef85e0aa432718359edd01af5408b1a10a25034888683617db59bfb62254b93d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: PSEUDOCOMMAND

**Raw Source File**: `data/docs/codebase_c64_org/base/scpu_setscrncol.md`
**SHA256**: `ef85e0aa432718359edd01af5408b1a10a25034888683617db59bfb62254b93d`

## Summary




# PSEUDOCOMMAND

base:scpu_setscrncol

                # PSEUDOCOMMAND

Sets $d020 and $d021 to value passed to pseudocommand. Lowbyte of val sets $d020 and highbyte sets $d021

| SYNTAX: | :ScreenColor val |  |  | 
| EXAMPLE: | :ScreenColor #$0201 |  |  | 
| PARAMETERS: | Type | Minimum | Maximum | 
|  | U16 | #$0000 | #$ffff | 

Can with good advantage be improved to take advantage of the nativly defined color constants in Kickassembler allowing :ScreenColor BLUE : RED

```
    .pseudocomma...
