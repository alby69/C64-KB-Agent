---
title: Eingabe-Warteschleife
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
- 0073-chrget
- a480-eingabe-warteschleife
- a483-standard-warm-start-routine
- jmp
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - commodore-64-intern-buch.txt
  address: $A480
  address_end: $A499
  symbol: eingabe-warteschleife
  sources:
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A480**: JMP $A483'
---

# $A480 — Eingabe-Warteschleife

## Disassemblatura
```assembly
.A480  6C 02 03 JMP ($0302)   ; JMP $A483
.A483  20 60 A5 JSR $A560   ; BASIC-Zeile nach Eingabepuffer
.A486  86 7A    STX $7A   ; CHRGET Zeiger auf
.A488  84 7B    STY $7B   ; Eingabepuffer
.A48A  20 73 00 JSR $0073   ; nächstes Zeichen holen
.A48D  AA       TAX   ; Puffer leer?
.A48E  F0 F0    BEQ $A480   ; Ja: dann weiter warten
.A490  A2 FF    LDX #$FF   ; Wert für
.A492  86 3A    STX $3A   ; Kennzeichen für Direktmodus
.A494  90 06    BCC $A49C   ; Ziffer? als Zeile einfügen
.A496  20 79 A5 JSR $A579   ; BASIC-Zeile in Code wandeln
.A499  4C E1 A7 JMP $A7E1   ; Befehl ausführen
```


## Commenti

### Commodore-64-intern-Buch (Commodore)
- **$A480**: JMP $A483
- **$A483**: BASIC-Zeile nach Eingabepuffer
- **$A486**: CHRGET Zeiger auf
- **$A488**: Eingabepuffer
- **$A48A**: nächstes Zeichen holen
- **$A48D**: Puffer leer?
- **$A48E**: Ja: dann weiter warten
- **$A490**: Wert für
- **$A492**: Kennzeichen für Direktmodus
- **$A494**: Ziffer? als Zeile einfügen
- **$A496**: BASIC-Zeile in Code wandeln
- **$A499**: Befehl ausführen

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*