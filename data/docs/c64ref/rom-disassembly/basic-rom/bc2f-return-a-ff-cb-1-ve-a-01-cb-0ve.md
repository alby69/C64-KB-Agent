---
title: return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/original_disassembly.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc2f-return-a-ff-cb-1-ve-a-01-cb-0ve
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $BC2F
  address_end: $BC2F
  symbol: return-a-ff-cb-1-ve-a-01-cb-0ve
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC2F**: else get FAC1 sign (b7)'
---

# $BC2F — return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve

## Disassemblatura
```assembly
.BC2F  A5 66    LDA $66   ; else get FAC1 sign (b7)
```


## Commenti

### Original Disassembly (—)
- **$BC2F**: else get FAC1 sign (b7)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*