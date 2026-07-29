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
- bc31-return-a-ff-cb-1-ve-a-01-cb-0ve
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - original_disassembly.txt
  address: $BC31
  address_end: $BC38
  symbol: return-a-ff-cb-1-ve-a-01-cb-0ve
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC31**: move sign bit to carry'
---

# $BC31 — return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve

## Disassemblatura
```assembly
.BC31  2A       ROL   ; move sign bit to carry
.BC32  A9 FF    LDA #$FF   ; set byte for -ve result
.BC34  B0 02    BCS $BC38   ; return if sign was set (-ve)
.BC36  A9 01    LDA #$01   ; else set byte for +ve result
.BC38  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BC31**: move sign bit to carry
- **$BC32**: set byte for -ve result
- **$BC34**: return if sign was set (-ve)
- **$BC36**: else set byte for +ve result

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*