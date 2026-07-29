---
title: BASIC vectors, these are copied to RAM from $0300 onwards
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
- 0300-ierror
- 0302-imain
- 0304-icrnch
- 0306-iqplop
- 0308-igone
- 030a-ieval
- e447-tabelle-der-basic-vektoren
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E447
  address_end: $E451
  symbol: basic-vectors-these-are-copied-to-ram-from-0300-onwards
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E447**: error message          $0300'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E453**: Die'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E447**: IERROR VEC, print basic error message ($e38b)'
---

# $E447 — BASIC vectors, these are copied to RAM from $0300 onwards

## Disassemblatura
```assembly
.E447  8B E3   ; error message          $0300
.E449  83 A4   ; BASIC warm start       $0302
.E44B  7C A5   ; crunch BASIC tokens    $0304
.E44D  1A A7   ; uncrunch BASIC tokens  $0306
.E44F  E4 A7   ; start new BASIC code   $0308
.E451  86 AE   ; get arithmetic element $030A
```


## Commenti

### Original Disassembly (—)
- **$E447**: error message          $0300
- **$E449**: BASIC warm start       $0302
- **$E44B**: crunch BASIC tokens    $0304
- **$E44D**: uncrunch BASIC tokens  $0306
- **$E44F**: start new BASIC code   $0308
- **$E451**: get arithmetic element $030A

### Commodore-64-intern-Buch (Commodore)
- **$E453**: Die
- **$E455**: BASIC-
- **$E458**: Vektoren
- **$E45B**: laden
- **$E45C**: schon alle?
- **$E45E**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E447**: IERROR VEC, print basic error message ($e38b)
- **$E449**: IMAIN VECTOR, basic warm start ($a483)
- **$E44B**: ICRNCH VECTOR, tokenise basic text ($a57c)
- **$E44D**: IQPLOP VECTOR, list basic text ($a7a1)
- **$E44F**: IGONE VEXTOR, basic character dispatch ($a7e4)
- **$E451**: IEVAL VECTOR, evaluate basic token ($ae86)

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*