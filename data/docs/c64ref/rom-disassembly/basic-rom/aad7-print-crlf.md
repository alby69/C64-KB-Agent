---
title: print CR/LF
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
- aad7-end-line-on-cmd-output-file
- aae8-routine-for-printing-tab-and-spc
- aaf8-tab-c1-und-spc-c0
- cursor
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $AAD7
  address_end: $AB1C
  symbol: print-crlf
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$AAD7**: set [CR]'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $AAD7 — print CR/LF

## Disassemblatura
```assembly
.AAD7  A9 0D    LDA #$0D   ; set [CR]
.AAD9  20 47 AB JSR $AB47   ; print the character
.AADC  24 13    BIT $13   ; test current I/O channel
.AADE  10 05    BPL $AAE5   ; if ?? toggle A, EOR #$FF and return
.AAE0  A9 0A    LDA #$0A   ; set [LF]
.AAE2  20 47 AB JSR $AB47   ; print the character toggle A
.AAE5  49 FF    EOR #$FF   ; invert A
.AAE7  60       RTS   ; was ","
.AAE8  38       SEC   ; set Cb for read cursor position
.AAE9  20 F0 FF JSR $FFF0   ; read/set X,Y cursor position
.AAEC  98       TYA   ; copy cursor Y
.AAED  38       SEC   ; set carry for subtract
.AAEE  E9 0A    SBC #$0A   ; subtract one TAB length
.AAF0  B0 FC    BCS $AAEE   ; loop if result was +ve
.AAF2  49 FF    EOR #$FF   ; complement it
.AAF4  69 01    ADC #$01   ; +1, twos complement
.AAF6  D0 16    BNE $AB0E   ; always print A spaces, result is never $00
.AAF8  08       PHP   ; save TAB( or SPC( status
.AAF9  38       SEC   ; set Cb for read cursor position
.AAFA  20 F0 FF JSR $FFF0   ; read/set X,Y cursor position
.AAFD  84 09    STY $09   ; save current cursor position
.AAFF  20 9B B7 JSR $B79B   ; scan and get byte parameter
.AB02  C9 29    CMP #$29   ; compare with ")"
.AB04  D0 59    BNE $AB5F   ; if not ")" do syntax error
.AB06  28       PLP   ; restore TAB( or SPC( status
.AB07  90 06    BCC $AB0F   ; branch if was SPC( else was TAB(
.AB09  8A       TXA   ; copy TAB() byte to A
.AB0A  E5 09    SBC $09   ; subtract current cursor position
.AB0C  90 05    BCC $AB13   ; go loop for next if already past requited position
.AB0E  AA       TAX   ; copy [SPACE] count to X
.AB0F  E8       INX   ; increment count
.AB10  CA       DEX   ; decrement count
.AB11  D0 06    BNE $AB19   ; branch if count was not zero was ";" or [SPACES] printed
.AB13  20 73 00 JSR $0073   ; increment and scan memory
.AB16  4C A2 AA JMP $AAA2   ; continue print loop
.AB19  20 3B AB JSR $AB3B   ; print [SPACE] or [CURSOR RIGHT]
.AB1C  D0 F2    BNE $AB10   ; loop, branch always
```


## Commenti

### Original Disassembly (—)
- **$AAD7**: set [CR]
- **$AAD9**: print the character
- **$AADC**: test current I/O channel
- **$AADE**: if ?? toggle A, EOR #$FF and return
- **$AAE0**: set [LF]
- **$AAE2**: print the character toggle A
- **$AAE5**: invert A
- **$AAE7**: was ","
- **$AAE8**: set Cb for read cursor position
- **$AAE9**: read/set X,Y cursor position
- **$AAEC**: copy cursor Y
- **$AAED**: set carry for subtract
- **$AAEE**: subtract one TAB length
- **$AAF0**: loop if result was +ve
- **$AAF2**: complement it
- **$AAF4**: +1, twos complement
- **$AAF6**: always print A spaces, result is never $00
- **$AAF8**: save TAB( or SPC( status
- **$AAF9**: set Cb for read cursor position
- **$AAFA**: read/set X,Y cursor position
- **$AAFD**: save current cursor position
- **$AAFF**: scan and get byte parameter
- **$AB02**: compare with ")"
- **$AB04**: if not ")" do syntax error
- **$AB06**: restore TAB( or SPC( status
- **$AB07**: branch if was SPC( else was TAB(
- **$AB09**: copy TAB() byte to A
- **$AB0A**: subtract current cursor position
- **$AB0C**: go loop for next if already past requited position
- **$AB0E**: copy [SPACE] count to X
- **$AB0F**: increment count
- **$AB10**: decrement count
- **$AB11**: branch if count was not zero was ";" or [SPACES] printed
- **$AB13**: increment and scan memory
- **$AB16**: continue print loop
- **$AB19**: print [SPACE] or [CURSOR RIGHT]
- **$AB1C**: loop, branch always

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*