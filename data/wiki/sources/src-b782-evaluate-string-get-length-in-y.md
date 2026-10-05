---
id: src-b782-evaluate-string-get-length-in-y
type: source
title: 'Source Summary: evaluate string, get length in Y'
aliases:
- evaluate string, get length in Y
- b782-evaluate-string-get-length-in-y.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b782-evaluate-string-get-length-in-y.md
  sha256: 86659891a78cb4f701d9bdc03af8212e9ce6ec288b829d33d3bd0836b7aa457a
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: evaluate string, get length in Y

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/b782-evaluate-string-get-length-in-y.md`
**SHA256**: `86659891a78cb4f701d9bdc03af8212e9ce6ec288b829d33d3bd0836b7aa457a`

## Summary



# $B782 — evaluate string, get length in Y

## Disassemblatura
```assembly
.B782  20 A3 B6 JSR $B6A3   ; evaluate string
.B785  A2 00    LDX #$00   ; set data type = numeric
.B787  86 0D    STX $0D   ; clear data type flag, $FF = string, $00 = numeric
.B789  A8       TAY   ; copy length to Y
.B78A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B782**: evaluate string
- **$B785**: set data type = numeric
- **$B787**: clear data type flag, $FF = string, $00 = numeric
- **$B78...
