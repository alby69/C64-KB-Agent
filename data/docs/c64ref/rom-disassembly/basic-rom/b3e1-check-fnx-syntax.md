---
title: check FNx syntax
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
- b3e1-prft-fn-syntax
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $B3E1
  address_end: $B3F1
  symbol: check-fnx-syntax
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$B3E1**: set FN token'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$B3E1**: FN-Code'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$B3E1**: MUST NOW SEE "FN" TOKEN'
---

# $B3E1 — check FNx syntax

## Disassemblatura
```assembly
.B3E1  A9 A5    LDA #$A5   ; set FN token
.B3E3  20 FF AE JSR $AEFF   ; scan for CHR$(A), else do syntax error then warm start
.B3E6  09 80    ORA #$80   ; set FN flag bit
.B3E8  85 10    STA $10   ; save FN name
.B3EA  20 92 B0 JSR $B092   ; search for FN variable
.B3ED  85 4E    STA $4E   ; save function pointer low byte
.B3EF  84 4F    STY $4F   ; save function pointer high byte
.B3F1  4C 8D AD JMP $AD8D   ; check if source is numeric and return, else do type mismatch
```


## Commenti

### Original Disassembly (—)
- **$B3E1**: set FN token
- **$B3E3**: scan for CHR$(A), else do syntax error then warm start
- **$B3E6**: set FN flag bit
- **$B3E8**: save FN name
- **$B3EA**: search for FN variable
- **$B3ED**: save function pointer low byte
- **$B3EF**: save function pointer high byte
- **$B3F1**: check if source is numeric and return, else do type mismatch

### Commodore-64-intern-Buch (Commodore)
- **$B3E1**: FN-Code
- **$B3E3**: prüft auf FN-Code
- **$B3E6**: Wert laden
- **$B3E8**: sperrt INTEGER-Variable
- **$B3EA**: sucht Variable
- **$B3ED**: LOW- und HIGH-Byte
- **$B3EF**: FN-Variablenzeiger setzen
- **$B3F1**: prüft auf numerisch

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$B3E1**: MUST NOW SEE "FN" TOKEN
- **$B3E3**: OR ELSE SYNTAX ERROR
- **$B3E6**: SET SIGN BIT ON 1ST CHAR OF NAME,
- **$B3E8**: MAKING $C0 < SUBFLG < $DB
- **$B3EA**: WHICH TELLS PTRGET WHO CALLED
- **$B3ED**: FOUND VALID FUNCTION NAME, SO
- **$B3EF**: SAVE ADDRESS
- **$B3F1**: MUST BE NUMERIC

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*