---
title: scan for autostart ROM at $8000, returns Zb=1 if ROM found
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- fd02-prft-auf-rom-in-8000
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FD02
  address_end: $FD0F
  symbol: scan-for-autostart-rom-at-8000-returns-zb1-if-rom-found
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD02**: five characters to test'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FD02**: Zeiger setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD02**: 5 bytes to check'
---

# $FD02 — scan for autostart ROM at $8000, returns Zb=1 if ROM found

## Disassemblatura
```assembly
.FD02  A2 05    LDX #$05   ; five characters to test
.FD04  BD 0F FD LDA $FD0F,X   ; get test character
.FD07  DD 03 80 CMP $8003,X   ; compare with byte in ROM space
.FD0A  D0 03    BNE $FD0F   ; exit if no match
.FD0C  CA       DEX   ; decrement index
.FD0D  D0 F5    BNE $FD04   ; loop if not all done
.FD0F  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$FD02**: five characters to test
- **$FD04**: get test character
- **$FD07**: compare with byte in ROM space
- **$FD0A**: exit if no match
- **$FD0C**: decrement index
- **$FD0D**: loop if not all done

### Commodore-64-intern-Buch (Commodore)
- **$FD02**: Zeiger setzen
- **$FD04**: Wert aus Tabelle holen und
- **$FD07**: ab $8000 vergleichen (CBM80)
- **$FD0A**: verzweige wenn ungleich
- **$FD0C**: Zeiger vermindern
- **$FD0D**: weiter wenn nicht 5 Bytes
- **$FD0F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FD02**: 5 bytes to check
- **$FD04**: Identifier at $fd10
- **$FD07**: Compare with $8004
- **$FD0A**: NOT equal!
- **$FD0D**: until Z=1

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*