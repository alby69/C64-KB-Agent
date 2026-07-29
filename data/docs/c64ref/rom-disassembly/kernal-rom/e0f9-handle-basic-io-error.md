---
title: handle BASIC I/O error
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
- e0f9-io-routinen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E0F9
  address_end: $E109
  symbol: handle-basic-io-error
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E0F9**: compare error with $F0'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E0F9**: RS 232 OPEN oder CLOSE ?'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E0F9**: test error'
---

# $E0F9 — handle BASIC I/O error

## Disassemblatura
```assembly
.E0F9  C9 F0    CMP #$F0   ; compare error with $F0
.E0FB  D0 07    BNE $E104   ; branch if not $F0
.E0FD  84 38    STY $38   ; set end of memory high byte
.E0FF  86 37    STX $37   ; set end of memory low byte
.E101  4C 63 A6 JMP $A663   ; clear from start to end and return error was not $F0
.E104  AA       TAX   ; copy error #
.E105  D0 02    BNE $E109   ; branch if not $00
.E107  A2 1E    LDX #$1E   ; else error $1E, break error
.E109  4C 37 A4 JMP $A437   ; do error #X then warm start
```


## Commenti

### Original Disassembly (—)
- **$E0F9**: compare error with $F0
- **$E0FB**: branch if not $F0
- **$E0FD**: set end of memory high byte
- **$E0FF**: set end of memory low byte
- **$E101**: clear from start to end and return error was not $F0
- **$E104**: copy error #
- **$E105**: branch if not $00
- **$E107**: else error $1E, break error
- **$E109**: do error #X then warm start

### Commodore-64-intern-Buch (Commodore)
- **$E0F9**: RS 232 OPEN oder CLOSE ?
- **$E0FB**: nein
- **$E0FD**: BASIC-RAM Ende
- **$E0FF**: neu setzen
- **$E101**: und zum CLR-Befehl
- **$E104**: Fehlernummer nach X
- **$E105**: nicht Null ?
- **$E107**: sonst Nummer für 'BREAK'
- **$E109**: Fehlermeldung ausgeben

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E0F9**: test error
- **$E0FD**: MEMSIZ, highest address in BASIC
- **$E101**: do CLR without aborting I/O
- **$E104**: put error flag i (X)
- **$E105**: if error code $00, then set error code $1e
- **$E109**: do error

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*