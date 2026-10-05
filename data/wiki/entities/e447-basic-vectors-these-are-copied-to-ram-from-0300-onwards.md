---
id: e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards
type: entity
title: BASIC vectors, these are copied to RAM from $0300 onwards
aliases:
- BASIC vectors, these are copied to RAM from $0300 onwards
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards.md
  sha256: 612bde02f858903e0886a5c95897a373825fa2e19f4aa5153dad246c79e4f2b3
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards
---

# BASIC vectors, these are copied to RAM from $0300 onwards



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

## References
- Source: [[src-e447-basic-vectors-these-are-copied-to-ram-from-0300-onwards]]
