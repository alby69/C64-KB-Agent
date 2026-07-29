---
title: start new BASIC code, the start new BASIC code vector is initialised to point
  here
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- a7e4-execute-a-statement
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $A7E4
  address_end: $A7EA
  symbol: start-new-basic-code-the-start-new-basic-code-vector-is-initialised-to-point-here
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A7E4**: increment and scan memory'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

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