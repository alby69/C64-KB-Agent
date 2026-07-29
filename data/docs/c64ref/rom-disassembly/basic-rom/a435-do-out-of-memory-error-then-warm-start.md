---
title: do out of memory error then warm start
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
- a435-out-of-memory-error
- a437-fehlereinsprung
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $A435
  address_end: $A437
  symbol: do-out-of-memory-error-then-warm-start
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A435**: error code $10, out of memory error do error #X then
      warm start'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A435**: error number'
---

# $A435 — do out of memory error then warm start

## Disassemblatura
```assembly
.A435  A2 10    LDX #$10   ; error code $10, out of memory error do error #X then warm start
.A437  6C 00 03 JMP ($0300)   ; do error message
```


## Commenti

### Original Disassembly (—)
- **$A435**: error code $10, out of memory error do error #X then warm start
- **$A437**: do error message

### Marko Mäkelä (Marko Mäkelä)
- **$A435**: error number

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*