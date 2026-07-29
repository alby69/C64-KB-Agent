---
title: bad input routine
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
- 00d7-data
- ab4d-fehlerbehandlung-bei-eingabe
- ab57-fehler-bei-read
- ab5b-fehler-bei-get
- ab62-fehler-bei-input
- input
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AB4D
  address_end: $AB7A
  symbol: bad-input-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AB4D**: get INPUT mode flag, $00 = INPUT, $40 = GET, $98 =
      READ'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AB4D**: Flag für INPUT / GET / READ'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AB6B**: low  AD0C'
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: '- **$AB4F**: TAKEN IF INPUT'
---

# $AB4D — bad input routine

## Disassemblatura
```assembly
.AB4D  A5 11    LDA $11   ; get INPUT mode flag, $00 = INPUT, $40 = GET, $98 = READ
.AB4F  F0 11    BEQ $AB62   ; branch if INPUT
.AB51  30 04    BMI $AB57   ; branch if READ else was GET
.AB53  A0 FF    LDY #$FF   ; set current line high byte to -1, indicate immediate mode
.AB55  D0 04    BNE $AB5B   ; branch always
.AB57  A5 3F    LDA $3F   ; get current DATA line number low byte
.AB59  A4 40    LDY $40   ; get current DATA line number high byte
.AB5B  85 39    STA $39   ; set current line number low byte
.AB5D  84 3A    STY $3A   ; set current line number high byte
.AB5F  4C 08 AF JMP $AF08   ; do syntax error then warm start was INPUT
.AB62  A5 13    LDA $13   ; get current I/O channel
.AB64  F0 05    BEQ $AB6B   ; branch if default channel
.AB66  A2 18    LDX #$18   ; else error $18, file data error
.AB68  4C 37 A4 JMP $A437   ; do error #X then warm start
.AB6B  A9 0C    LDA #$0C   ; set "?REDO FROM START" pointer low byte
.AB6D  A0 AD    LDY #$AD   ; set "?REDO FROM START" pointer high byte
.AB6F  20 1E AB JSR $AB1E   ; print null terminated string
.AB72  A5 3D    LDA $3D   ; get continue pointer low byte
.AB74  A4 3E    LDY $3E   ; get continue pointer high byte
.AB76  85 7A    STA $7A   ; save BASIC execute pointer low byte
.AB78  84 7B    STY $7B   ; save BASIC execute pointer high byte
.AB7A  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$AB4D**: get INPUT mode flag, $00 = INPUT, $40 = GET, $98 = READ
- **$AB4F**: branch if INPUT
- **$AB51**: branch if READ else was GET
- **$AB53**: set current line high byte to -1, indicate immediate mode
- **$AB55**: branch always
- **$AB57**: get current DATA line number low byte
- **$AB59**: get current DATA line number high byte
- **$AB5B**: set current line number low byte
- **$AB5D**: set current line number high byte
- **$AB5F**: do syntax error then warm start was INPUT
- **$AB62**: get current I/O channel
- **$AB64**: branch if default channel
- **$AB66**: else error $18, file data error
- **$AB68**: do error #X then warm start
- **$AB6B**: set "?REDO FROM START" pointer low byte
- **$AB6D**: set "?REDO FROM START" pointer high byte
- **$AB6F**: print null terminated string
- **$AB72**: get continue pointer low byte
- **$AB74**: get continue pointer high byte
- **$AB76**: save BASIC execute pointer low byte
- **$AB78**: save BASIC execute pointer high byte

### Commodore-64-intern-Buch (Commodore)
- **$AB4D**: Flag für INPUT / GET / READ
- **$AB4F**: INPUT: $AB62
- **$AB51**: READ: $AB57
- **$AB53**: GET:
- **$AB55**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
- **$AB6B**: low  AD0C
- **$AB6D**: high AD0C

### Bob Sander-Cederlof (Bob Sander-Cederlof)
- **$AB4F**: TAKEN IF INPUT
- **$AB51**: TAKEN IF READ
- **$AB53**: FROM A GET
- **$AB55**: ...ALWAYS
- **$AB57**: TELL WHERE THE "DATA" IS, RATHER
- **$AB59**: THAN THE "READ"
- **$AB66**: ERROR CODE = 254
- **$AB6B**: "?REENTER"
- **$AB72**: RE-EXECUTE THE WHOLE INPUT STATEMENT

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*