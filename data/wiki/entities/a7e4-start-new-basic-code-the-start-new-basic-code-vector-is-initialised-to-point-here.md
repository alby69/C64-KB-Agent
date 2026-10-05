---
id: a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here
type: entity
title: start new BASIC code, the start new BASIC code vector is initialised to point
  here
aliases:
- start new BASIC code, the start new BASIC code vector is initialised to point here
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
links_out:
- src-a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here
---

# start new BASIC code, the start new BASIC code vector is initialised to point here



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

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-a7e4-start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here]]
