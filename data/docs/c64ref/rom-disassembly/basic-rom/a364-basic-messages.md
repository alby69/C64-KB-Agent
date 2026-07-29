---
title: BASIC messages
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
- a364-meldungen-des-interpreters
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A364
  address_end: $A388
  symbol: basic-messages
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A364**: OK'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A364**: OK'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A364**: ok'
---

# $A364 — BASIC messages

## Disassemblatura
```assembly
.A364  0D 4F 4B 0D   ; OK
.A368  00 20 20 45 52 52 4F 52   ; ERROR
.A370  00 20 49 4E 20 00 0D 0A   ; IN
.A378  52 45 41 44 59 2E 0D 0A   ; READY.
.A380  00 0D 0A 42 52 45 41 4B   ; BREAK
.A388  00
```


## Commenti

### Original Disassembly (—)
- **$A364**: OK
- **$A368**: ERROR
- **$A370**: IN
- **$A378**: READY.
- **$A380**: BREAK

### Commodore-64-intern-Buch (Commodore)
- **$A364**: OK
- **$A368**: ERROR
- **$A370**: IN
- **$A378**: READY.
- **$A380**: BREAK

### Marko Mäkelä (Marko Mäkelä)
- **$A364**: ok
- **$A369**: error
- **$A371**: in
- **$A376**: ready.
- **$A381**: break

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*