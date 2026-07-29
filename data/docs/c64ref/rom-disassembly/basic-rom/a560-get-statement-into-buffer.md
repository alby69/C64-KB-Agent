---
title: get statement into buffer
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
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
  - commodore-64-intern-buch.txt
  address: $A560
  address_end: $A576
  symbol: get-statement-into-buffer
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A560**: Zeiger setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A571**: error number'
---

# $A560 — get statement into buffer

## Disassemblatura
```assembly
.A560  A2 00    LDX #$00
.A562  20 12 E1 JSR $E112
.A565  C9 0D    CMP #$0D
.A567  F0 0D    BEQ $A576
.A569  9D 00 02 STA $0200,X
.A56C  E8       INX
.A56D  E0 59    CPX #$59
.A56F  90 F1    BCC $A562
.A571  A2 17    LDX #$17   ; error number
.A573  4C 37 A4 JMP $A437
.A576  4C CA AA JMP $AACA   ; goto end of line
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A560**: Zeiger setzen
- **$A562**: ein Zeichen holen
- **$A565**: RETURN-Taste ?
- **$A567**: ja, dann Eingabe beenden
- **$A569**: Zeichen nach Eingabepuffer
- **$A56C**: Zeiger um 1 erhöhen
- **$A56D**: 89. Zeichen ?
- **$A56F**: nein, weitere Zeichen holen
- **$A571**: Nummer für 'string too long'
- **$A573**: Fehlermeldung ausgeben
- **$A576**: Puffer mit $0 abschließen, CR

### Marko Mäkelä (Marko Mäkelä)
- **$A571**: error number
- **$A576**: goto end of line

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*