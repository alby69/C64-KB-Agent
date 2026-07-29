---
title: get arithmetic element, the get arithmetic element vector is initialised to
  point here
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
- ae86-standard-arithmetic-element
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $AE86
  address_end: $AEA5
  symbol: get-arithmetic-element-the-get-arithmetic-element-vector-is-initialised-to-point-here
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AE86**: clear byte'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AE9A**: PI'
---

# $AE86 — get arithmetic element, the get arithmetic element vector is initialised to point here

## Disassemblatura
```assembly
.AE86  A9 00    LDA #$00   ; clear byte
.AE88  85 0D    STA $0D   ; clear data type flag, $FF = string, $00 = numeric
.AE8A  20 73 00 JSR $0073   ; increment and scan memory
.AE8D  B0 03    BCS $AE92   ; branch if not numeric character else numeric string found (e.g. 123)
.AE8F  4C F3 BC JMP $BCF3   ; get FAC1 from string and return get value from line .. continued wasn't a number so ...
.AE92  20 13 B1 JSR $B113   ; check byte, return Cb = 0 if<"A" or >"Z"
.AE95  90 03    BCC $AE9A   ; branch if not variable name
.AE97  4C 28 AF JMP $AF28   ; variable name set-up and return
.AE9A  C9 FF    CMP #$FF   ; compare with token for PI
.AE9C  D0 0F    BNE $AEAD   ; branch if not PI
.AE9E  A9 A8    LDA #$A8   ; get PI pointer low byte
.AEA0  A0 AE    LDY #$AE   ; get PI pointer high byte
.AEA2  20 A2 BB JSR $BBA2   ; unpack memory (AY) into FAC1
.AEA5  4C 73 00 JMP $0073   ; increment and scan memory and return
```


## Commenti

### Original Disassembly (—)
- **$AE86**: clear byte
- **$AE88**: clear data type flag, $FF = string, $00 = numeric
- **$AE8A**: increment and scan memory
- **$AE8D**: branch if not numeric character else numeric string found (e.g. 123)
- **$AE8F**: get FAC1 from string and return get value from line .. continued wasn't a number so ...
- **$AE92**: check byte, return Cb = 0 if<"A" or >"Z"
- **$AE95**: branch if not variable name
- **$AE97**: variable name set-up and return
- **$AE9A**: compare with token for PI
- **$AE9C**: branch if not PI
- **$AE9E**: get PI pointer low byte
- **$AEA0**: get PI pointer high byte
- **$AEA2**: unpack memory (AY) into FAC1
- **$AEA5**: increment and scan memory and return

### Marko Mäkelä (Marko Mäkelä)
- **$AE9A**: PI
- **$AE9E**: low  AEA8
- **$AEA0**: high AEA8

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*