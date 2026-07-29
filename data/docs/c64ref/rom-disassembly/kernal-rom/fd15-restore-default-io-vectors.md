---
title: restore default I/O vectors
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
- fd15-setzenholen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FD15
  address_end: $FD19
  symbol: restore-default-io-vectors
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FD15**: pointer to vector table low byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FD15**: LOW- und HIGH-Byte des'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$FD15**: low  FD30'
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FD15**: $fd30 - table of KERNAL vectors'
---

# $FD15 — restore default I/O vectors

## Disassemblatura
```assembly
.FD15  A2 30    LDX #$30   ; pointer to vector table low byte
.FD17  A0 FD    LDY #$FD   ; pointer to vector table high byte
.FD19  18       CLC   ; flag set vectors
```


## Commenti

### Original Disassembly (—)
- **$FD15**: pointer to vector table low byte
- **$FD17**: pointer to vector table high byte
- **$FD19**: flag set vectors

### Commodore-64-intern-Buch (Commodore)
- **$FD15**: LOW- und HIGH-Byte des
- **$FD17**: Zeigers auf Tabelle $FD30
- **$FD19**: Flag für 'Vektoren setzen'
- **$FD1A**: LOW- und HIGH-Byte
- **$FD1C**: des Zeigers setzen
- **$FD1E**: Zeiger setzen (16 Vektoren)
- **$FD20**: Wert aus Tabelle holen
- **$FD23**: C=1 holen,C=0 setzen
- **$FD25**: Tabellenwert holen
- **$FD27**: Tabellenwert setzen
- **$FD29**: Wert in Tabelle ablegen
- **$FD2C**: Zähler vermindern
- **$FD2D**: Fertig? nein: nächster Wert
- **$FD2F**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
- **$FD15**: low  FD30
- **$FD17**: high FD30

### Magnus Nyman (Magnus Nyman)
- **$FD15**: $fd30 - table of KERNAL vectors
- **$FD17**: Clear carry to SET values.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*