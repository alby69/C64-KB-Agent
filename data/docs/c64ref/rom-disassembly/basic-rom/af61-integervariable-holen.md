---
title: Integervariable holen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- af61-integervariable-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $AF61
  address_end: $AF6B
  symbol: integervariable-holen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AF61**: Zeiger setzen'
---

# $AF61 — Integervariable holen

## Disassemblatura
```assembly
.AF61  A0 00    LDY #$00   ; Zeiger setzen
.AF63  B1 64    LDA ($64),Y   ; Intgerzahl holen (1. Byte)
.AF65  AA       TAX   ; ins X-Reg.
.AF66  C8       INY   ; Zeiger erhöhen
.AF67  B1 64    LDA ($64),Y   ; 2. Byte holen
.AF69  A8       TAY   ; ins Y-Register
.AF6A  8A       TXA   ; 1. Byte in Akku holen
.AF6B  4C 91 B3 JMP $B391   ; und nach Fließkomma wandeln
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$AF61**: Zeiger setzen
- **$AF63**: Intgerzahl holen (1. Byte)
- **$AF65**: ins X-Reg.
- **$AF66**: Zeiger erhöhen
- **$AF67**: 2. Byte holen
- **$AF69**: ins Y-Register
- **$AF6A**: 1. Byte in Akku holen
- **$AF6B**: und nach Fließkomma wandeln

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*