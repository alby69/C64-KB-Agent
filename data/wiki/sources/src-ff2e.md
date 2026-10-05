---
id: src-ff2e
type: source
title: 'Source Summary: ??'
aliases:
- ??
- ff2e.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff2e.md
  sha256: 5674a582784acc1860971cb05c93b0a42499d10b4fb04192cfb476d949256659
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ??

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff2e.md`
**SHA256**: `5674a582784acc1860971cb05c93b0a42499d10b4fb04192cfb476d949256659`

## Summary



# $FF2E — ??

## Disassemblatura
```assembly
.FF2E  AA       TAX
.FF2F  AD 96 02 LDA $0296   ; nonstandard bit timing high byte
.FF32  2A       ROL
.FF33  A8       TAY
.FF34  8A       TXA
.FF35  69 C8    ADC #$C8
.FF37  8D 99 02 STA $0299
.FF3A  98       TYA
.FF3B  69 00    ADC #$00   ; add any carry
.FF3D  8D 9A 02 STA $029A
.FF40  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FF2F**: nonstandard bit timing high byte
- **$FF3B**: add any carry

### Commodore-64-intern-Buch...
