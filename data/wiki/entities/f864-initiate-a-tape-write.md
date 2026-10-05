---
id: f864-initiate-a-tape-write
type: entity
title: initiate a tape write
aliases:
- initiate a tape write
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/f864-initiate-a-tape-write.md
  sha256: 1b86618a949bedcc58c87fbe47b1e5de59793abf4f109a58756ea31835e0516c
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-f864-initiate-a-tape-write
---

# initiate a tape write



# $F864 — initiate a tape write

## Disassemblatura
```assembly
.F864  20 D7 F7 JSR $F7D7   ; set tape buffer start and end pointers do tape write, 20 cycle count
.F867  A9 14    LDA #$14   ; set write lead cycle count
.F869  85 AB    STA $AB   ; save write lead cycle count do tape write, no cycle count set
.F86B  20 38 F8 JSR $F838   ; wait for PLAY/RECORD
.F86E  B0 6C    BCS $F8DC   ; if STOPped clear save IRQ address and exit
.F870  78       SEI   ; disable interrupts
.F871  A9 82    LDA #$82   ; enable ?? interrupt
.F873  A2 08    LDX #$08   ; set index for tape write tape leader vector
```


## Commenti

### Original Disassembly (—)
- **$F864**: set tape buffer start and end pointers do tape write, 20 cycle count
- **$F867**: set write lead cycle count
- **$F869**: save write lead cycle count do tape write, no cycle count set
- **$F86B**: wait for PLAY/RECORD
- **$F86E**: if STOPped clear save IRQ address and exit
- **$F870**: disable interrupts
- **$F871**: enable ?? interrupt
- **$F873**: set index for tape write tape leader vector

### Commodore-64-intern-Buch (Commodore)
- **$F864**: Bandpufferadresse holen
- **$F867**: Länge des Vorspanns vor WRITE
- **$F869**: speichern

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-f864-initiate-a-tape-write]]
