---
title: convert AY and do (AY)/FAC1
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
- bb0f-fac-konstante-ay-fac
- bb12-fac-arg-fac
- bb8f-copy-result-into-fac-mantissa-and-normalize
- bc5b-fac
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - bob_sander-cederlof.txt
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $BB0F
  address_end: $BB9F
  symbol: convert-ay-and-do-ayfac1
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$BB0F**: unpack memory (AY) into FAC2'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$BB0F**: Konstante (A/Y) nach ARG'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Bob Sander-Cederlof
    author: Bob Sander-Cederlof
    description: Nessun commento disponibile.
---

# $BB0F — convert AY and do (AY)/FAC1

## Disassemblatura
```assembly
.BB0F  20 8C BA JSR $BA8C   ; unpack memory (AY) into FAC2
.BB12  F0 76    BEQ $BB8A   ; if zero go do /0 error
.BB14  20 1B BC JSR $BC1B   ; round FAC1
.BB17  A9 00    LDA #$00   ; clear A
.BB19  38       SEC   ; set carry for subtract
.BB1A  E5 61    SBC $61   ; subtract FAC1 exponent (2s complement)
.BB1C  85 61    STA $61   ; save FAC1 exponent
.BB1E  20 B7 BA JSR $BAB7   ; test and adjust accumulators
.BB21  E6 61    INC $61   ; increment FAC1 exponent
.BB23  F0 BA    BEQ $BADF   ; if zero do overflow error
.BB25  A2 FC    LDX #$FC   ; set index to FAC temp
.BB27  A9 01    LDA #$01   ; set byte
.BB29  A4 6A    LDY $6A   ; get FAC2 mantissa 1
.BB2B  C4 62    CPY $62   ; compare FAC1 mantissa 1
.BB2D  D0 10    BNE $BB3F   ; branch if <>
.BB2F  A4 6B    LDY $6B   ; get FAC2 mantissa 2
.BB31  C4 63    CPY $63   ; compare FAC1 mantissa 2
.BB33  D0 0A    BNE $BB3F   ; branch if <>
.BB35  A4 6C    LDY $6C   ; get FAC2 mantissa 3
.BB37  C4 64    CPY $64   ; compare FAC1 mantissa 3
.BB39  D0 04    BNE $BB3F   ; branch if <>
.BB3B  A4 6D    LDY $6D   ; get FAC2 mantissa 4
.BB3D  C4 65    CPY $65   ; compare FAC1 mantissa 4
.BB3F  08       PHP   ; save FAC2-FAC1 compare status
.BB40  2A       ROL   ; shift byte
.BB41  90 09    BCC $BB4C   ; skip next if no carry
.BB43  E8       INX   ; increment index to FAC temp
.BB44  95 29    STA $29,X
.BB46  F0 32    BEQ $BB7A
.BB48  10 34    BPL $BB7E
.BB4A  A9 01    LDA #$01
.BB4C  28       PLP   ; restore FAC2-FAC1 compare status
.BB4D  B0 0E    BCS $BB5D   ; if FAC2 >= FAC1 then do subtract FAC2 = FAC2*2
.BB4F  06 6D    ASL $6D   ; shift FAC2 mantissa 4
.BB51  26 6C    ROL $6C   ; shift FAC2 mantissa 3
.BB53  26 6B    ROL $6B   ; shift FAC2 mantissa 2
.BB55  26 6A    ROL $6A   ; shift FAC2 mantissa 1
.BB57  B0 E6    BCS $BB3F   ; loop with no compare
.BB59  30 CE    BMI $BB29   ; loop with compare
.BB5B  10 E2    BPL $BB3F   ; loop with no compare, branch always
.BB5D  A8       TAY   ; save FAC2-FAC1 compare status
.BB5E  A5 6D    LDA $6D   ; get FAC2 mantissa 4
.BB60  E5 65    SBC $65   ; subtract FAC1 mantissa 4
.BB62  85 6D    STA $6D   ; save FAC2 mantissa 4
.BB64  A5 6C    LDA $6C   ; get FAC2 mantissa 3
.BB66  E5 64    SBC $64   ; subtract FAC1 mantissa 3
.BB68  85 6C    STA $6C   ; save FAC2 mantissa 3
.BB6A  A5 6B    LDA $6B   ; get FAC2 mantissa 2
.BB6C  E5 63    SBC $63   ; subtract FAC1 mantissa 2
.BB6E  85 6B    STA $6B   ; save FAC2 mantissa 2
.BB70  A5 6A    LDA $6A   ; get FAC2 mantissa 1
.BB72  E5 62    SBC $62   ; subtract FAC1 mantissa 1
.BB74  85 6A    STA $6A   ; save FAC2 mantissa 1
.BB76  98       TYA   ; restore FAC2-FAC1 compare status
.BB77  4C 4F BB JMP $BB4F
.BB7A  A9 40    LDA #$40
.BB7C  D0 CE    BNE $BB4C   ; branch always do A<<6, save as FAC1 rounding byte, normalise and return
.BB7E  0A       ASL
.BB7F  0A       ASL
.BB80  0A       ASL
.BB81  0A       ASL
.BB82  0A       ASL
.BB83  0A       ASL
.BB84  85 70    STA $70   ; save FAC1 rounding byte
.BB86  28       PLP   ; dump FAC2-FAC1 compare status
.BB87  4C 8F BB JMP $BB8F   ; copy temp to FAC1, normalise and return do "Divide by zero" error
.BB8A  A2 14    LDX #$14   ; error $14, divide by zero error
.BB8C  4C 37 A4 JMP $A437   ; do error #X then warm start
.BB8F  A5 26    LDA $26   ; get temp mantissa 1
.BB91  85 62    STA $62   ; save FAC1 mantissa 1
.BB93  A5 27    LDA $27   ; get temp mantissa 2
.BB95  85 63    STA $63   ; save FAC1 mantissa 2
.BB97  A5 28    LDA $28   ; get temp mantissa 3
.BB99  85 64    STA $64   ; save FAC1 mantissa 3
.BB9B  A5 29    LDA $29   ; get temp mantissa 4
.BB9D  85 65    STA $65   ; save FAC1 mantissa 4
.BB9F  4C D7 B8 JMP $B8D7   ; normalise FAC1 and return
```


## Commenti

### Original Disassembly (—)
- **$BB0F**: unpack memory (AY) into FAC2
- **$BB12**: if zero go do /0 error
- **$BB14**: round FAC1
- **$BB17**: clear A
- **$BB19**: set carry for subtract
- **$BB1A**: subtract FAC1 exponent (2s complement)
- **$BB1C**: save FAC1 exponent
- **$BB1E**: test and adjust accumulators
- **$BB21**: increment FAC1 exponent
- **$BB23**: if zero do overflow error
- **$BB25**: set index to FAC temp
- **$BB27**: set byte
- **$BB29**: get FAC2 mantissa 1
- **$BB2B**: compare FAC1 mantissa 1
- **$BB2D**: branch if <>
- **$BB2F**: get FAC2 mantissa 2
- **$BB31**: compare FAC1 mantissa 2
- **$BB33**: branch if <>
- **$BB35**: get FAC2 mantissa 3
- **$BB37**: compare FAC1 mantissa 3
- **$BB39**: branch if <>
- **$BB3B**: get FAC2 mantissa 4
- **$BB3D**: compare FAC1 mantissa 4
- **$BB3F**: save FAC2-FAC1 compare status
- **$BB40**: shift byte
- **$BB41**: skip next if no carry
- **$BB43**: increment index to FAC temp
- **$BB4C**: restore FAC2-FAC1 compare status
- **$BB4D**: if FAC2 >= FAC1 then do subtract FAC2 = FAC2*2
- **$BB4F**: shift FAC2 mantissa 4
- **$BB51**: shift FAC2 mantissa 3
- **$BB53**: shift FAC2 mantissa 2
- **$BB55**: shift FAC2 mantissa 1
- **$BB57**: loop with no compare
- **$BB59**: loop with compare
- **$BB5B**: loop with no compare, branch always
- **$BB5D**: save FAC2-FAC1 compare status
- **$BB5E**: get FAC2 mantissa 4
- **$BB60**: subtract FAC1 mantissa 4
- **$BB62**: save FAC2 mantissa 4
- **$BB64**: get FAC2 mantissa 3
- **$BB66**: subtract FAC1 mantissa 3
- **$BB68**: save FAC2 mantissa 3
- **$BB6A**: get FAC2 mantissa 2
- **$BB6C**: subtract FAC1 mantissa 2
- **$BB6E**: save FAC2 mantissa 2
- **$BB70**: get FAC2 mantissa 1
- **$BB72**: subtract FAC1 mantissa 1
- **$BB74**: save FAC2 mantissa 1
- **$BB76**: restore FAC2-FAC1 compare status
- **$BB7C**: branch always do A<<6, save as FAC1 rounding byte, normalise and return
- **$BB84**: save FAC1 rounding byte
- **$BB86**: dump FAC2-FAC1 compare status
- **$BB87**: copy temp to FAC1, normalise and return do "Divide by zero" error
- **$BB8A**: error $14, divide by zero error
- **$BB8C**: do error #X then warm start
- **$BB8F**: get temp mantissa 1
- **$BB91**: save FAC1 mantissa 1
- **$BB93**: get temp mantissa 2
- **$BB95**: save FAC1 mantissa 2
- **$BB97**: get temp mantissa 3
- **$BB99**: save FAC1 mantissa 3
- **$BB9B**: get temp mantissa 4
- **$BB9D**: save FAC1 mantissa 4
- **$BB9F**: normalise FAC1 and return

### Commodore-64-intern-Buch (Commodore)
- **$BB0F**: Konstante (A/Y) nach ARG

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Bob Sander-Cederlof (Bob Sander-Cederlof)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*