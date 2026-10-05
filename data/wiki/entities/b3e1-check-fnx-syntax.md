---
id: b3e1-check-fnx-syntax
type: entity
title: check FNx syntax
aliases:
- check FNx syntax
tags:
- rom-disassembly
- basic-rom
sources:
- path: data/docs/c64ref/rom-disassembly/basic-rom/b3e1-check-fnx-syntax.md
  sha256: 6a1ae25dad8d24ebcaf500b004a235bad9aed44079bd2254e14ab5e226900409
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-b3e1-check-fnx-syntax
---

# check FNx syntax



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

## References
- Source: [[src-b3e1-check-fnx-syntax]]
