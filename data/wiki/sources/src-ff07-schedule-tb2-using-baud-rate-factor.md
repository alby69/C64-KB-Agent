---
id: src-ff07-schedule-tb2-using-baud-rate-factor
type: source
title: 'Source Summary: schedule TB2 using baud rate factor'
aliases:
- schedule TB2 using baud rate factor
- ff07-schedule-tb2-using-baud-rate-factor.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff07-schedule-tb2-using-baud-rate-factor.md
  sha256: 9c128d92053b55165d7d2b6b3707c54727e4f9e3c919f3acbd960e30143dda8f
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: schedule TB2 using baud rate factor

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff07-schedule-tb2-using-baud-rate-factor.md`
**SHA256**: `9c128d92053b55165d7d2b6b3707c54727e4f9e3c919f3acbd960e30143dda8f`

## Summary



# $FF07 — schedule TB2 using baud rate factor

## Disassemblatura
```assembly
.FF07  AD 95 02 LDA $0295
.FF0A  8D 06 DD STA $DD06
.FF0D  AD 96 02 LDA $0296
.FF10  8D 07 DD STA $DD07
.FF13  A9 11    LDA #$11
.FF15  8D 0F DD STA $DD0F
.FF18  A9 12    LDA #$12
.FF1A  4D A1 02 EOR $02A1
.FF1D  8D A1 02 STA $02A1
.FF20  A9 FF    LDA #$FF
.FF22  8D 06 DD STA $DD06
.FF25  8D 07 DD STA $DD07
.FF28  AE 98 02 LDX $0298
.FF2B  86 A8    STX $A8
.FF2D  60       RTS
```


## Commenti

### Commodore-64-inter...
