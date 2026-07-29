---
title: variable name set-up
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/marko_mäkelä.txt
category: source-code
topics:
- rom-disassembly
- basic-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- af28-variable-holen
- af61-integervariable-holen
- af6e-real-variable-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $AF28
  address_end: $AF81
  symbol: variable-name-set-up
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AF28**: get variable address'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$AF28**: Variable suchen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: '- **$AF40**: T'
---

# $AF28 — variable name set-up

## Disassemblatura
```assembly
.AF28  20 8B B0 JSR $B08B   ; get variable address
.AF2B  85 64    STA $64   ; save variable pointer low byte
.AF2D  84 65    STY $65   ; save variable pointer high byte
.AF2F  A6 45    LDX $45   ; get current variable name first character
.AF31  A4 46    LDY $46   ; get current variable name second character
.AF33  A5 0D    LDA $0D   ; get data type flag, $FF = string, $00 = numeric
.AF35  F0 26    BEQ $AF5D   ; branch if numeric variable is string
.AF37  A9 00    LDA #$00   ; else clear A
.AF39  85 70    STA $70   ; clear FAC1 rounding byte
.AF3B  20 14 AF JSR $AF14   ; check address range
.AF3E  90 1C    BCC $AF5C   ; exit if not in BASIC ROM
.AF40  E0 54    CPX #$54   ; compare variable name first character with "T"
.AF42  D0 18    BNE $AF5C   ; exit if not "T"
.AF44  C0 C9    CPY #$C9   ; compare variable name second character with "I$"
.AF46  D0 14    BNE $AF5C   ; exit if not "I$" variable name was "TI$"
.AF48  20 84 AF JSR $AF84   ; read real time clock into FAC1 mantissa, 0HML
.AF4B  84 5E    STY $5E   ; clear exponent count adjust
.AF4D  88       DEY   ; Y = $FF
.AF4E  84 71    STY $71   ; set output string index, -1 to allow for pre increment
.AF50  A0 06    LDY #$06   ; HH:MM:SS is six digits
.AF52  84 5D    STY $5D   ; set number of characters before the decimal point
.AF54  A0 24    LDY #$24   ; index to jiffy conversion table
.AF56  20 68 BE JSR $BE68   ; convert jiffy count to string
.AF59  4C 6F B4 JMP $B46F   ; exit via STR$() code tail
.AF5C  60       RTS   ; variable name set-up, variable is numeric
.AF5D  24 0E    BIT $0E   ; test data type flag, $80 = integer, $00 = float
.AF5F  10 0D    BPL $AF6E   ; branch if float
.AF61  A0 00    LDY #$00   ; clear index
.AF63  B1 64    LDA ($64),Y   ; get integer variable low byte
.AF65  AA       TAX   ; copy to X
.AF66  C8       INY   ; increment index
.AF67  B1 64    LDA ($64),Y   ; get integer variable high byte
.AF69  A8       TAY   ; copy to Y
.AF6A  8A       TXA   ; copy low byte to A
.AF6B  4C 91 B3 JMP $B391   ; convert fixed integer AY to float FAC1 and return variable name set-up, variable is float
.AF6E  20 14 AF JSR $AF14   ; check address range
.AF71  90 2D    BCC $AFA0   ; if not in BASIC ROM get pointer and unpack into FAC1
.AF73  E0 54    CPX #$54   ; compare variable name first character with "T"
.AF75  D0 1B    BNE $AF92   ; branch if not "T"
.AF77  C0 49    CPY #$49   ; compare variable name second character with "I"
.AF79  D0 25    BNE $AFA0   ; branch if not "I" variable name was "TI"
.AF7B  20 84 AF JSR $AF84   ; read real time clock into FAC1 mantissa, 0HML
.AF7E  98       TYA   ; clear A
.AF7F  A2 A0    LDX #$A0   ; set exponent to 32 bit value
.AF81  4C 4F BC JMP $BC4F   ; set exponent = X and normalise FAC1
```


## Commenti

### Original Disassembly (—)
- **$AF28**: get variable address
- **$AF2B**: save variable pointer low byte
- **$AF2D**: save variable pointer high byte
- **$AF2F**: get current variable name first character
- **$AF31**: get current variable name second character
- **$AF33**: get data type flag, $FF = string, $00 = numeric
- **$AF35**: branch if numeric variable is string
- **$AF37**: else clear A
- **$AF39**: clear FAC1 rounding byte
- **$AF3B**: check address range
- **$AF3E**: exit if not in BASIC ROM
- **$AF40**: compare variable name first character with "T"
- **$AF42**: exit if not "T"
- **$AF44**: compare variable name second character with "I$"
- **$AF46**: exit if not "I$" variable name was "TI$"
- **$AF48**: read real time clock into FAC1 mantissa, 0HML
- **$AF4B**: clear exponent count adjust
- **$AF4D**: Y = $FF
- **$AF4E**: set output string index, -1 to allow for pre increment
- **$AF50**: HH:MM:SS is six digits
- **$AF52**: set number of characters before the decimal point
- **$AF54**: index to jiffy conversion table
- **$AF56**: convert jiffy count to string
- **$AF59**: exit via STR$() code tail
- **$AF5C**: variable name set-up, variable is numeric
- **$AF5D**: test data type flag, $80 = integer, $00 = float
- **$AF5F**: branch if float
- **$AF61**: clear index
- **$AF63**: get integer variable low byte
- **$AF65**: copy to X
- **$AF66**: increment index
- **$AF67**: get integer variable high byte
- **$AF69**: copy to Y
- **$AF6A**: copy low byte to A
- **$AF6B**: convert fixed integer AY to float FAC1 and return variable name set-up, variable is float
- **$AF6E**: check address range
- **$AF71**: if not in BASIC ROM get pointer and unpack into FAC1
- **$AF73**: compare variable name first character with "T"
- **$AF75**: branch if not "T"
- **$AF77**: compare variable name second character with "I"
- **$AF79**: branch if not "I" variable name was "TI"
- **$AF7B**: read real time clock into FAC1 mantissa, 0HML
- **$AF7E**: clear A
- **$AF7F**: set exponent to 32 bit value
- **$AF81**: set exponent = X and normalise FAC1

### Commodore-64-intern-Buch (Commodore)
- **$AF28**: Variable suchen
- **$AF2B**: Zeiger auf Variable
- **$AF2D**: bzw. Stringdescriptor
- **$AF2F**: als
- **$AF31**: Variablenname speichern
- **$AF33**: Typflag holen
- **$AF35**: numerisch?
- **$AF37**: Wert laden und
- **$AF39**: in Rundungsbyte fur FAC
- **$AF3B**: Descriptor im Interpreter?
- **$AF3E**: nein
- **$AF40**: 'T'? (von TI$)
- **$AF42**: nein: $AF5C
- **$AF44**: 'I$'? (von TI$)
- **$AF46**: nein: $AF5C
- **$AF48**: Zeit nach FAC holen
- **$AF4B**: Flag für Exponentialdarst. =0
- **$AF4D**: vermindern (=$FF)
- **$AF4E**: Zeiger für Stringstartadresse
- **$AF50**: Länge 6 für TI$
- **$AF52**: speichern
- **$AF54**: Zeiger auf Stellenwert
- **$AF56**: erzeugt String TI$
- **$AF59**: bringt String in Str.bereich
- **$AF5C**: Rücksprung
- **$AF5D**: INTEGER/ REAL Flag
- **$AF5F**: REAL? ja: $AF6E

### Marko Mäkelä (Marko Mäkelä)
- **$AF40**: T
- **$AF44**: I$
- **$AF73**: T
- **$AF77**: I

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*