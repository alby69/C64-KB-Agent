---
title: get parameters for LOAD/SAVE
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
- e1d4-holen
- ece7-load
- f5ed-save
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E1D4
  address_end: $E1FD
  symbol: get-parameters-for-loadsave
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E1D4**: clear file name length'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E1D4**: Default für Länge des Filenamen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E1D4**: clear length of filename'
---

# $E1D4 — get parameters for LOAD/SAVE

## Disassemblatura
```assembly
.E1D4  A9 00    LDA #$00   ; clear file name length
.E1D6  20 BD FF JSR $FFBD   ; clear the filename
.E1D9  A2 01    LDX #$01   ; set default device number, cassette
.E1DB  A0 00    LDY #$00   ; set default command
.E1DD  20 BA FF JSR $FFBA   ; set logical, first and second addresses
.E1E0  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E1E3  20 57 E2 JSR $E257   ; set filename
.E1E6  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E1E9  20 00 E2 JSR $E200   ; scan and get byte, else do syntax error then warm start
.E1EC  A0 00    LDY #$00   ; clear command
.E1EE  86 49    STX $49   ; save device number
.E1F0  20 BA FF JSR $FFBA   ; set logical, first and second addresses
.E1F3  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E1F6  20 00 E2 JSR $E200   ; scan and get byte, else do syntax error then warm start
.E1F9  8A       TXA   ; copy command to A
.E1FA  A8       TAY   ; copy command to Y
.E1FB  A6 49    LDX $49   ; get device number back
.E1FD  4C BA FF JMP $FFBA   ; set logical, first and second addresses and return
```


## Commenti

### Original Disassembly (—)
- **$E1D4**: clear file name length
- **$E1D6**: clear the filename
- **$E1D9**: set default device number, cassette
- **$E1DB**: set default command
- **$E1DD**: set logical, first and second addresses
- **$E1E0**: exit function if [EOT] or ":"
- **$E1E3**: set filename
- **$E1E6**: exit function if [EOT] or ":"
- **$E1E9**: scan and get byte, else do syntax error then warm start
- **$E1EC**: clear command
- **$E1EE**: save device number
- **$E1F0**: set logical, first and second addresses
- **$E1F3**: exit function if [EOT] or ":"
- **$E1F6**: scan and get byte, else do syntax error then warm start
- **$E1F9**: copy command to A
- **$E1FA**: copy command to Y
- **$E1FB**: get device number back
- **$E1FD**: set logical, first and second addresses and return

### Commodore-64-intern-Buch (Commodore)
- **$E1D4**: Default für Länge des Filenamen
- **$E1D6**: Filenamenparameter setzen
- **$E1D9**: Default für Gerätenummer
- **$E1DB**: Sekundäradresse
- **$E1DD**: Fileparameter setzen
- **$E1E0**: weitere Zeichen ?
- **$E1E3**: Filenamen holen
- **$E1E6**: weitere Zeichen ?
- **$E1E9**: Geräteadresse holen
- **$E1EC**: Sekundäradresse
- **$E1EE**: Geräteadresse
- **$E1F0**: Fileparameter setzen
- **$E1F3**: weitere Zeichen ?
- **$E1F6**: Sekundäradresse holen
- **$E1F9**: in Akku schieben
- **$E1FA**: Sekundäradresse
- **$E1FB**: Gerätenummer
- **$E1FD**: Fileparameter setzen
- **$E200**: prüft auf Komma und weitere Zeichen
- **$E203**: holt Byte-Wert nach X

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E1D4**: clear length of filename
- **$E1D6**: SETNAM
- **$E1D9**: default FA, device number is #01
- **$E1DB**: default SA, secondary address is #00
- **$E1DD**: SETLFS, and device number
- **$E1E0**: test if "end of line", if so end here
- **$E1E3**: set up given filename and perform SETNAM
- **$E1E6**: test if "end of line", if so end here
- **$E1E9**: check for comma, and input one byte, FA, to (X)
- **$E1F0**: perform new SETLFS with device number
- **$E1F3**: test if "end of line", if so end here
- **$E1F6**: check for comma, and input one byte, SA, to (X)
- **$E1F9**: transfer (X) to (Y)
- **$E1FB**: get FA
- **$E1FD**: perform SETLFS with both device number and secondary address. Then exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*