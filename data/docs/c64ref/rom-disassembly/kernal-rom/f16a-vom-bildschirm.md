---
title: vom Bildschirm
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
- f16a-vom-bildschirm
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $F16A
  address_end: $F177
  symbol: vom-bildschirm
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F16A**: Flag auf Eingabe von Bild- schimrstelle'
---

# $F16A — vom Bildschirm

## Disassemblatura
```assembly
.F16A  85 D0    STA $D0   ; Flag auf Eingabe von Bild- schimrstelle
.F16C  A5 D5    LDA $D5   ; Cursorzeile laden
.F16E  85 C8    STA $C8   ; als Pointer für Ende der Zeile speichern
.F170  4C 32 E6 JMP $E632   ; zu Eingabe vom Bildschirm
.F173  B0 38    BCS $F1AD   ; verzweige zu Eingabe vom IEC-Bus
.F175  C9 02    CMP #$02   ; Eingabe von RS-232 ?
.F177  F0 3F    BEQ $F1B8   ; ja, so verzweige
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$F16A**: Flag auf Eingabe von Bild- schimrstelle
- **$F16C**: Cursorzeile laden
- **$F16E**: als Pointer für Ende der Zeile speichern
- **$F170**: zu Eingabe vom Bildschirm
- **$F173**: verzweige zu Eingabe vom IEC-Bus
- **$F175**: Eingabe von RS-232 ?
- **$F177**: ja, so verzweige

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*