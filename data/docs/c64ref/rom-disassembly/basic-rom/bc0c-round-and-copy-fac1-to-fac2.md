---
title: round and copy FAC1 to FAC2
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/bob_sander-cederlof.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- bc0c-fac-nach-arg-bertragen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BC0C
  address_end: $BC1A
  symbol: round-and-copy-fac1-to-fac2
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BC0C**: round FAC1 copy FAC1 to FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BC0C**: FAC runden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$BC0C**: ROUND FAC USING EXTENSION'
---

# $BC0C — round and copy FAC1 to FAC2

## Disassemblatura
```assembly
.BC0C  20 1B BC JSR $BC1B   ; round FAC1 copy FAC1 to FAC2
.BC0F  A2 06    LDX #$06   ; 6 bytes to copy
.BC11  B5 60    LDA $60,X   ; get byte from FAC1,X
.BC13  95 68    STA $68,X   ; save byte at FAC2,X
.BC15  CA       DEX   ; decrement count
.BC16  D0 F9    BNE $BC11   ; loop if not all done
.BC18  86 70    STX $70   ; clear FAC1 rounding byte
.BC1A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$BC0C**: round FAC1 copy FAC1 to FAC2
- **$BC0F**: 6 bytes to copy
- **$BC11**: get byte from FAC1,X
- **$BC13**: save byte at FAC2,X
- **$BC15**: decrement count
- **$BC16**: loop if not all done
- **$BC18**: clear FAC1 rounding byte

### Commodore-64-intern-Buch (Commodore)
- **$BC0C**: FAC runden
- **$BC0F**: 6 Zeichen
- **$BC11**: FAC in
- **$BC13**: ARG
- **$BC15**: übertragen
- **$BC16**: schon alle Zeichen ?
- **$BC18**: FAC-Rundungsstelle löschen
- **$BC1A**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$BC0C**: ROUND FAC USING EXTENSION
- **$BC0F**: COPY 6 BYTES, INCLUDES SIGN
- **$BC18**: ZERO FAC EXTENSION

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*