---
title: ??
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related: []
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $FF2E
  address_end: $FF40
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FF2F**: nonstandard bit timing high byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FF2E**: Baudrate aus Tabelle nach X'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

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

### Commodore-64-intern-Buch (Commodore)
- **$FF2E**: Baudrate aus Tabelle nach X
- **$FF2F**: HIGH-Byte holen
- **$FF32**: mal 2
- **$FF33**: nach Y retten
- **$FF34**: LOW-Byte holen
- **$FF35**: plus 200
- **$FF37**: nach Timerwert LOW
- **$FF3A**: HIGH-Byte zurückholen
- **$FF3B**: Übertrag addieren
- **$FF3D**: nach Timerwert HIGH
- **$FF40**: Rücksprung
- **$FF41**: No OPeration
- **$FF42**: No OPeration

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*