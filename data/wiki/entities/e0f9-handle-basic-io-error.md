---
id: e0f9-handle-basic-io-error
type: entity
title: handle BASIC I/O error
aliases:
- handle BASIC I/O error
tags:
- kernal-rom
- rom-disassembly
sources:
- path: data/docs/c64ref/rom-disassembly/kernal-rom/e0f9-handle-basic-io-error.md
  sha256: d5acb56d174ead969a244992e9b8ca8b93f1242d99e5a3d4527d0ef7583b8a8e
created_at: '2026-10-05'
updated_at: '2026-10-05'
status: stable
contradictions: []
links_out:
- src-e0f9-handle-basic-io-error
---

# handle BASIC I/O error



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

## References
- Source: [[src-e0f9-handle-basic-io-error]]
