---
id: src-ff6e
type: source
title: 'Source Summary: ??'
aliases:
- ??
- ff6e.md
tags:
- rom-disassembly
- kernal-rom
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/ff6e.md
  sha256: 630c1916d77046496e3a4c7f3155d24cb8aa7ac51865a35835bd79fd56df22a5
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out: []
---

# Source Summary: ??

**Raw Source File**: `data/docs/c64ref/rom-disassembly/kernal-rom/ff6e.md`
**SHA256**: `630c1916d77046496e3a4c7f3155d24cb8aa7ac51865a35835bd79fd56df22a5`

## Summary



# $FF6E — ??

## Disassemblatura
```assembly
.FF6E  A9 81    LDA #$81   ; enable timer A interrupt
.FF70  8D 0D DC STA $DC0D   ; save VIA 1 ICR
.FF73  AD 0E DC LDA $DC0E   ; read VIA 1 CRA
.FF76  29 80    AND #$80   ; mask x000 0000, TOD clock
.FF78  09 11    ORA #$11   ; mask xxx1 xxx1, load timer A, start timer A
.FF7A  8D 0E DC STA $DC0E   ; save VIA 1 CRA
.FF7D  4C 8E EE JMP $EE8E   ; set the serial clock out low and return
```


## Commenti

### Original Disassembly (—)
- **$FF6E**: enabl...
