---
title: perform POKE
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
- b824-basic-befehl-poke
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B824
  address_end: $B82C
  symbol: perform-poke
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B824**: get parameters for POKE/WAIT'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B824**: Poke-Adrefcse und Wert holen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B824**: GET THE ADDRESS AND VALUE'
---

# $B824 — perform POKE

## Disassemblatura
```assembly
.B824  20 EB B7 JSR $B7EB   ; get parameters for POKE/WAIT
.B827  8A       TXA   ; copy byte to A
.B828  A0 00    LDY #$00   ; clear index
.B82A  91 14    STA ($14),Y   ; write byte
.B82C  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$B824**: get parameters for POKE/WAIT
- **$B827**: copy byte to A
- **$B828**: clear index
- **$B82A**: write byte

### Commodore-64-intern-Buch (Commodore)
- **$B824**: Poke-Adrefcse und Wert holen
- **$B827**: Poke-Wert in Akku
- **$B828**: Zähler auf Null
- **$B82A**: und in Speicher schreiben
- **$B82C**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B824**: GET THE ADDRESS AND VALUE
- **$B827**: VALUE IN A,
- **$B82A**: STORE IT AWAY,
- **$B82C**: AND THAT'S ALL FOR TODAY

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*