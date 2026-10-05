---
id: bf11-constants
type: entity
title: constants
aliases:
- constants
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/bf11-constants.md
  sha256: 21e469b638942d6bb895e8a334a21a21254f23cf1f93f30e47ae53ce4967efde
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-bf11-constants
---

# constants



# $BF11 — constants

## Disassemblatura
```assembly
.BF11  80 00   ; 0.5, first two bytes
.BF13  00 00 00   ; null return for undefined variables
.BF16  FA 0A 1F 00   ; -100 000 000
.BF1A  00 98 96 80   ; +10 000 000
.BF1E  FF F0 BD C0   ; -1 000 000
.BF22  00 01 86 A0   ; +100 000
.BF26  FF FF D8 F0   ; -10 000
.BF2A  00 00 03 E8   ; +1 000
.BF2E  FF FF FF 9C   ; - 100
.BF32  00 00 00 0A   ; +10
.BF36  FF FF FF FF   ; -1
```


## Commenti

### Original Disassembly (—)
- **$BF11**: 0.5, first two bytes
- **$BF13**: null return for undefined variables
- **$BF16**: -100 000 000
- **$BF1A**: +10 000 000
- **$BF1E**: -1 000 000
- **$BF22**: +100 000
- **$BF26**: -10 000
- **$BF2A**: +1 000
- **$BF2E**: - 100
- **$BF32**: +10
- **$BF36**: -1

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-bf11-constants]]
