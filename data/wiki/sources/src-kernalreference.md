---
id: src-kernalreference
type: source
title: 'Source Summary: Kernal Reference'
aliases:
- Kernal Reference
- kernalreference.md
tags:
- sprite programming
- input handling
- assembly
- raster interrupts
- memory management
sources:
- path: data/docs/codebase_c64_org/base/kernalreference.md
  sha256: 8d16b80dd9522a365563cd13f59bd9b05411a109584bd605d59a36decd0fa5bf
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: Kernal Reference

**Raw Source File**: `data/docs/codebase_c64_org/base/kernalreference.md`
**SHA256**: `8d16b80dd9522a365563cd13f59bd9b05411a109584bd605d59a36decd0fa5bf`

## Summary




# Kernal Reference

base:kernalreference

                # Kernal Reference

```
Label   Jump Vector Real  Function                           Function Input/Output                    Register Usage
        addr  addr  code  Description                        Parameters                             entry  return  used
-----------------------------------------------------------------------------------------------------------------------
CINT    FF81  ----  FF5B  init VIC & screen editor        ...
