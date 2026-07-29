---
title: Band als Ausgabegerät setzen
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/commodore-64-intern-buch.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- f26f-band-als-ausgabegert-setzen
- output
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F26F
  address_end: $F278
  symbol: band-als-ausgabegert-setzen
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F26F**: Sekundäradresse laden'
---

# $F26F — Band als Ausgabegerät setzen

## Disassemblatura
```assembly
.F26F  A6 B9    LDX $B9   ; Sekundäradresse laden
.F271  E0 60    CPX #$60   ; mit 'Null' vergleichen
.F273  F0 EA    BEQ $F25F   ; Bandfile zum Lesen, 'NOT OUTPUT FILE'
.F275  85 9A    STA $9A   ; Nummer des Ausgabegeräts setzen
.F277  18       CLC   ; Carry =0 (ok Kennzeichen)
.F278  60       RTS   ; Rücksprung
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F26F**: Sekundäradresse laden
- **$F271**: mit 'Null' vergleichen
- **$F273**: Bandfile zum Lesen, 'NOT OUTPUT FILE'
- **$F275**: Nummer des Ausgabegeräts setzen
- **$F277**: Carry =0 (ok Kennzeichen)
- **$F278**: Rücksprung

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*