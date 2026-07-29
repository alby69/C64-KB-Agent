---
title: read real time clock into FAC1 mantissa, 0HML
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
- af84-zeit-holen
- af92-continue-of-get-value-of-variable
- afa0-real-variable-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AF84
  address_end: $AFA4
  symbol: read-real-time-clock-into-fac1-mantissa-0hml
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AF84**: read real time clock'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AF84**: TIME holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AF84 — read real time clock into FAC1 mantissa, 0HML

## Disassemblatura
```assembly
.AF84  20 DE FF JSR $FFDE   ; read real time clock
.AF87  86 64    STX $64   ; save jiffy clock mid byte as  FAC1 mantissa 3
.AF89  84 63    STY $63   ; save jiffy clock high byte as  FAC1 mantissa 2
.AF8B  85 65    STA $65   ; save jiffy clock low byte as  FAC1 mantissa 4
.AF8D  A0 00    LDY #$00   ; clear Y
.AF8F  84 62    STY $62   ; clear FAC1 mantissa 1
.AF91  60       RTS   ; variable name set-up, variable is float and not "Tx"
.AF92  E0 53    CPX #$53   ; compare variable name first character with "S"
.AF94  D0 0A    BNE $AFA0   ; if not "S" go do normal floating variable
.AF96  C0 54    CPY #$54   ; compare variable name second character with "
.AF98  D0 06    BNE $AFA0   ; if not "T" go do normal floating variable variable name was "ST"
.AF9A  20 B7 FF JSR $FFB7   ; read I/O status word
.AF9D  4C 3C BC JMP $BC3C   ; save A as integer byte and return variable is float
.AFA0  A5 64    LDA $64   ; get variable pointer low byte
.AFA2  A4 65    LDY $65   ; get variable pointer high byte
.AFA4  4C A2 BB JMP $BBA2   ; unpack memory (AY) into FAC1
```


## Commenti

### Original Disassembly (—)
- **$AF84**: read real time clock
- **$AF87**: save jiffy clock mid byte as  FAC1 mantissa 3
- **$AF89**: save jiffy clock high byte as  FAC1 mantissa 2
- **$AF8B**: save jiffy clock low byte as  FAC1 mantissa 4
- **$AF8D**: clear Y
- **$AF8F**: clear FAC1 mantissa 1
- **$AF91**: variable name set-up, variable is float and not "Tx"
- **$AF92**: compare variable name first character with "S"
- **$AF94**: if not "S" go do normal floating variable
- **$AF96**: compare variable name second character with "
- **$AF98**: if not "T" go do normal floating variable variable name was "ST"
- **$AF9A**: read I/O status word
- **$AF9D**: save A as integer byte and return variable is float
- **$AFA0**: get variable pointer low byte
- **$AFA2**: get variable pointer high byte
- **$AFA4**: unpack memory (AY) into FAC1

### Commodore-64-intern-Buch (Commodore)
- **$AF84**: TIME holen
- **$AF87**: 1. Byte nach FAC
- **$AF89**: 2. Byte nach FAC
- **$AF8B**: 3. Byte nach FAC
- **$AF8D**: Wert laden (0) und
- **$AF8F**: als 4. Byte nach FAC
- **$AF91**: Rücksprung
- **$AF92**: 'S'?
- **$AF94**: nein: $AFA0
- **$AF96**: 'T'?
- **$AF98**: nein: $AFA0
- **$AF9A**: Status holen
- **$AF9D**: Byte in Fließkommaformat

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*