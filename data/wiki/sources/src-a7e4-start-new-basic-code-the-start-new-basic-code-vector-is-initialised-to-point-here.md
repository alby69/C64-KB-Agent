---
id: src-a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here
type: source
title: 'Source Summary: start new BASIC code, the start new BASIC code vector is initialised
  to point here'
aliases:
- start new BASIC code, the start new BASIC code vector is initialised to point here
- a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here.md
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here.md
  sha256: 42962d341811e726ebcfb707aeda1f35e200c3e3db29a746c54455de6212169d
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: start new BASIC code, the start new BASIC code vector is initialised to point here

**Raw Source File**: `data/docs/c64ref/rom-disassembly/basic-rom/a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here.md`
**SHA256**: `42962d341811e726ebcfb707aeda1f35e200c3e3db29a746c54455de6212169d`

## Summary



# $A7E4 — start new BASIC code, the start new BASIC code vector is initialised to point here

## Disassemblatura
```assembly
.A7E4  20 73 00 JSR $0073   ; increment and scan memory
.A7E7  20 ED A7 JSR $A7ED   ; go interpret BASIC code from BASIC execute pointer
.A7EA  4C AE A7 JMP $A7AE   ; loop
```


## Commenti

### Original Disassembly (—)
- **$A7E4**: increment and scan memory
- **$A7E7**: go interpret BASIC code from BASIC execute pointer
- **$A7EA**: loop

### Marko Mäkelä (Marko Mäkelä)...
