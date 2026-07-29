---
title: perform RUN
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
- a871-basic-befehl-run
- clear
- ecec-run
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $A871
  address_end: $A880
  symbol: perform-run
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$A871**: save status'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$A871**: Statusregister retten'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$A87D**: do CLR'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$A871**: SAVE STATUS WHILE SUBTRACTING'
---

# $A871 — perform RUN

## Disassemblatura
```assembly
.A871  08       PHP   ; save status
.A872  A9 00    LDA #$00   ; no control or kernal messages
.A874  20 90 FF JSR $FF90   ; control kernal messages
.A877  28       PLP   ; restore status
.A878  D0 03    BNE $A87D   ; branch if RUN n
.A87A  4C 59 A6 JMP $A659   ; reset execution to start, clear variables, flush stack and return
.A87D  20 60 A6 JSR $A660   ; go do "CLEAR"
.A880  4C 97 A8 JMP $A897   ; get n and do GOTO n
```


## Commenti

### Original Disassembly (—)
- **$A871**: save status
- **$A872**: no control or kernal messages
- **$A874**: control kernal messages
- **$A877**: restore status
- **$A878**: branch if RUN n
- **$A87A**: reset execution to start, clear variables, flush stack and return
- **$A87D**: go do "CLEAR"
- **$A880**: get n and do GOTO n

### Commodore-64-intern-Buch (Commodore)
- **$A871**: Statusregister retten
- **$A872**: Wert laden und
- **$A874**: Flag für Programmodus setzen
- **$A877**: Statusregister zurückholen
- **$A878**: weitere Zeichen (Zeilennr.)?
- **$A87A**: Programmzeiger setzen, CLR
- **$A87D**: CLR-Befehl
- **$A880**: GOTO-Befehl

### Marko Mäkelä (Marko Mäkelä)
- **$A87D**: do CLR
- **$A880**: do GOTO

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$A871**: SAVE STATUS WHILE SUBTRACTING
- **$A877**: GET STATUS AGAIN (FROM CHRGET)
- **$A878**: PROBABLY A LINE NUMBER
- **$A87A**: START AT BEGINNING OF PROGRAM
- **$A87D**: CLEAR VARIABLES
- **$A880**: JOIN GOSUB STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*