---
title: get parameters for OPEN/CLOSE
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
- close
- e219-parameter-fr-open-holen
- f34a-open
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $E219
  address_end: $E254
  symbol: get-parameters-for-openclose
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$E219**: clear the filename length'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$E219**: Default für Länge des Filenamens'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$E219**: default filename is null'
---

# $E219 — get parameters for OPEN/CLOSE

## Disassemblatura
```assembly
.E219  A9 00    LDA #$00   ; clear the filename length
.E21B  20 BD FF JSR $FFBD   ; clear the filename
.E21E  20 11 E2 JSR $E211   ; scan for valid byte, else do syntax error then warm start
.E221  20 9E B7 JSR $B79E   ; get byte parameter, logical file number
.E224  86 49    STX $49   ; save logical file number
.E226  8A       TXA   ; copy logical file number to A
.E227  A2 01    LDX #$01   ; set default device number, cassette
.E229  A0 00    LDY #$00   ; set default command
.E22B  20 BA FF JSR $FFBA   ; set logical, first and second addresses
.E22E  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E231  20 00 E2 JSR $E200   ; scan and get byte, else do syntax error then warm start
.E234  86 4A    STX $4A   ; save device number
.E236  A0 00    LDY #$00   ; clear command
.E238  A5 49    LDA $49   ; get logical file number
.E23A  E0 03    CPX #$03   ; compare device number with screen
.E23C  90 01    BCC $E23F   ; branch if less than screen
.E23E  88       DEY   ; else decrement command
.E23F  20 BA FF JSR $FFBA   ; set logical, first and second addresses
.E242  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E245  20 00 E2 JSR $E200   ; scan and get byte, else do syntax error then warm start
.E248  8A       TXA   ; copy command to A
.E249  A8       TAY   ; copy command to Y
.E24A  A6 4A    LDX $4A   ; get device number
.E24C  A5 49    LDA $49   ; get logical file number
.E24E  20 BA FF JSR $FFBA   ; set logical, first and second addresses
.E251  20 06 E2 JSR $E206   ; exit function if [EOT] or ":"
.E254  20 0E E2 JSR $E20E   ; scan for ",byte", else do syntax error then warm start
```


## Commenti

### Original Disassembly (—)
- **$E219**: clear the filename length
- **$E21B**: clear the filename
- **$E21E**: scan for valid byte, else do syntax error then warm start
- **$E221**: get byte parameter, logical file number
- **$E224**: save logical file number
- **$E226**: copy logical file number to A
- **$E227**: set default device number, cassette
- **$E229**: set default command
- **$E22B**: set logical, first and second addresses
- **$E22E**: exit function if [EOT] or ":"
- **$E231**: scan and get byte, else do syntax error then warm start
- **$E234**: save device number
- **$E236**: clear command
- **$E238**: get logical file number
- **$E23A**: compare device number with screen
- **$E23C**: branch if less than screen
- **$E23E**: else decrement command
- **$E23F**: set logical, first and second addresses
- **$E242**: exit function if [EOT] or ":"
- **$E245**: scan and get byte, else do syntax error then warm start
- **$E248**: copy command to A
- **$E249**: copy command to Y
- **$E24A**: get device number
- **$E24C**: get logical file number
- **$E24E**: set logical, first and second addresses
- **$E251**: exit function if [EOT] or ":"
- **$E254**: scan for ",byte", else do syntax error then warm start

### Commodore-64-intern-Buch (Commodore)
- **$E219**: Default für Länge des Filenamens
- **$E21B**: Filenamenparameter setzen
- **$E21E**: weitere Zeichen ?
- **$E221**: holt logische Filenummer nach X-Reg
- **$E224**: und speichern
- **$E226**: logische Filenummer
- **$E227**: Default für Geräteadresse
- **$E229**: Sekundäradresse
- **$E22B**: Fileparameter setzen
- **$E22E**: weitere Zeichen ?
- **$E231**: holt Geräteadresse
- **$E234**: und speichern
- **$E236**: Sekundäradresse
- **$E238**: logische Filenummer
- **$E23A**: Gerätenummer kleiner 3 ?
- **$E23C**: ja
- **$E23E**: sonst Sekundäradresse auf 255 (keine Sek-Adr)
- **$E23F**: Fileparameter setzen
- **$E242**: weitere Zeichen ?
- **$E245**: holt Sekundäradresse
- **$E248**: in Akku schieben
- **$E249**: Sekundäradresse
- **$E24A**: Gerätenummer
- **$E24C**: logische Filenummer
- **$E24E**: Fileparameter setzen
- **$E251**: weitere Zeichen ?
- **$E254**: prüft auf Komma
- **$E257**: FRMEVL Ausdruck holen
- **$E25A**: holt Stringparameter, FRESTR
- **$E25D**: Adresse des
- **$E25F**: Filenamens
- **$E261**: Filenamenparameter setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$E219**: default filename is null
- **$E21B**: SETNAM
- **$E21E**: confirm TXTPNT is no terminator, if so - error
- **$E221**: input one byte character to (X)
- **$E224**: store logical filenumber in <FORPNT
- **$E226**: set default parameters to
- **$E227**: device = #1
- **$E229**: secondary address = #0
- **$E22B**: SETLFS
- **$E22E**: test if "end of line", if so end here
- **$E231**: check for comma, and input FA, device number
- **$E234**: store in >FORPNT
- **$E236**: secondary address = #0
- **$E238**: logical file number from temp store
- **$E23A**: test if serial device
- **$E23C**: nope
- **$E23E**: if serial, set secondary address to $ff
- **$E23F**: SETLFS
- **$E242**: test if "end of line", if so end here
- **$E245**: check for comma, and input SA, secondary address
- **$E249**: SA to (Y)
- **$E24A**: FA
- **$E24C**: LA
- **$E24E**: SETLFS
- **$E251**: test if "end of line", if so end here
- **$E254**: check for comma only
- **$E257**: evaluate expression in text
- **$E25A**: do string housekeeping
- **$E25D**: pointers to given filename
- **$E261**: SETNAM and exit

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*