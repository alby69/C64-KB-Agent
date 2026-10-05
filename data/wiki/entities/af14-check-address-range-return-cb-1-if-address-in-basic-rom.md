---
id: af14-check-address-range-return-cb-1-if-address-in-basic-rom
type: entity
title: check address range, return Cb = 1 if address in BASIC ROM
aliases:
- check address range, return Cb = 1 if address in BASIC ROM
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/af14-check-address-range-return-cb-1-if-address-in-basic-rom.md
  sha256: aa689133ccdcb23e96775997a91529b1bd82e9aa9cded8bb6b39882390641282
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-af14-check-address-range-return-cb-1-if-address-in-basic-rom
---

# check address range, return Cb = 1 if address in BASIC ROM



# $AF14 — check address range, return Cb = 1 if address in BASIC ROM

## Disassemblatura
```assembly
.AF14  38       SEC   ; set carry for subtract
.AF15  A5 64    LDA $64   ; get variable address low byte
.AF17  E9 00    SBC #$00   ; subtract $A000 low byte
.AF19  A5 65    LDA $65   ; get variable address high byte
.AF1B  E9 A0    SBC #$A0   ; subtract $A000 high byte
.AF1D  90 08    BCC $AF27   ; exit if address < $A000
.AF1F  A9 A2    LDA #$A2   ; get end of BASIC marker low byte
.AF21  E5 64    SBC $64   ; subtract variable address low byte
.AF23  A9 E3    LDA #$E3   ; get end of BASIC marker high byte
.AF25  E5 65    SBC $65   ; subtract variable address high byte
.AF27  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AF14**: set carry for subtract
- **$AF15**: get variable address low byte
- **$AF17**: subtract $A000 low byte
- **$AF19**: get variable address high byte
- **$AF1B**: subtract $A000 high byte
- **$AF1D**: exit if address < $A000
- **$AF1F**: get end of BASIC marker low byte
- **$AF21**: subtract variable address low byte
- **$AF23**: get end of BASIC marker high byte
- **$AF25**: subtract variable address high byte

### Commodore-64-intern-Buch (Commodore)
- **$AF14**: innerhalb des BASICs
- **$AF15**: Carry setzen (Subtr.)
- **$AF17**: Descriptor holen
- **$AF19**: liegt Descriptor ($64/$65)
- **$AF1B**: zwischen $A000 und $E32A?
- **$AF1D**: ja: dann C=1, sonst RTS
- **$AF1F**: 1. Wert laden
- **$AF21**: 1. Descriptorbyte abziehen
- **$AF23**: 2. Wert laden
- **$AF25**: und Descriptorwert abziehen
- **$AF27**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*

## References
- Source: [[src-af14-check-address-range-return-cb-1-if-address-in-basic-rom]]
