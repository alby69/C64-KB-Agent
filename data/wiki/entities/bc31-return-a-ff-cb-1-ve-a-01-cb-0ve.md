---
id: bc31-return-a-ff-cb-1-ve-a-01-cb-0ve
type: entity
title: return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
aliases:
- return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bc31-return-a-ff-cb-1-ve-a-01-cb-0ve.md
  sha256: d047ff15a13d0e3d51f997d763475d560c0821f1987d2bcc722eaea7c7b48358
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bc31-return-a-ff-cb-1-ve-a-01-cb-0ve
---

# return A = $FF, Cb = 1/-ve A = $01, Cb = 0/+ve



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

## References
- Source: [[src-bc31-return-a-ff-cb-1-ve-a-01-cb-0ve]]
