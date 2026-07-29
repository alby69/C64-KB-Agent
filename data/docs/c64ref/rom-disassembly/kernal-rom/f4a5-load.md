---
title: load
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
- bit
- ece7-load
- f4a5-standard-load-ram-entry
- f4b8-iec-load
- stop
- talk
- untalk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $F4A5
  address_end: $F530
  symbol: load
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F4A5**: save load/verify flag'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F4A5 — load

## Disassemblatura
```assembly
.F4A5  85 93    STA $93   ; save load/verify flag
.F4A7  A9 00    LDA #$00   ; clear A
.F4A9  85 90    STA $90   ; clear the serial status byte
.F4AB  A5 BA    LDA $BA   ; get the device number
.F4AD  D0 03    BNE $F4B2   ; if not the keyboard continue do 'illegal device number'
.F4AF  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F4B2  C9 03    CMP #$03
.F4B4  F0 F9    BEQ $F4AF
.F4B6  90 7B    BCC $F533
.F4B8  A4 B7    LDY $B7   ; get file name length
.F4BA  D0 03    BNE $F4BF   ; if not null name go ??
.F4BC  4C 10 F7 JMP $F710   ; else do 'missing file name' error and return
.F4BF  A6 B9    LDX $B9   ; get the secondary address
.F4C1  20 AF F5 JSR $F5AF   ; print "Searching..."
.F4C4  A9 60    LDA #$60
.F4C6  85 B9    STA $B9   ; save the secondary address
.F4C8  20 D5 F3 JSR $F3D5   ; send secondary address and filename
.F4CB  A5 BA    LDA $BA   ; get the device number
.F4CD  20 09 ED JSR $ED09   ; command serial bus device to TALK
.F4D0  A5 B9    LDA $B9   ; get the secondary address
.F4D2  20 C7 ED JSR $EDC7   ; send secondary address after TALK
.F4D5  20 13 EE JSR $EE13   ; input byte from serial bus
.F4D8  85 AE    STA $AE   ; save program start address low byte
.F4DA  A5 90    LDA $90   ; get the serial status byte
.F4DC  4A       LSR   ; shift time out read ..
.F4DD  4A       LSR   ; .. into carry bit
.F4DE  B0 50    BCS $F530   ; if timed out go do file not found error and return
.F4E0  20 13 EE JSR $EE13   ; input byte from serial bus
.F4E3  85 AF    STA $AF   ; save program start address high byte
.F4E5  8A       TXA   ; copy secondary address
.F4E6  D0 08    BNE $F4F0   ; load location not set in LOAD call, so continue with the load
.F4E8  A5 C3    LDA $C3   ; get the load address low byte
.F4EA  85 AE    STA $AE   ; save the program start address low byte
.F4EC  A5 C4    LDA $C4   ; get the load address high byte
.F4EE  85 AF    STA $AF   ; save the program start address high byte
.F4F0  20 D2 F5 JSR $F5D2
.F4F3  A9 FD    LDA #$FD   ; mask xxxx xx0x, clear time out read bit
.F4F5  25 90    AND $90   ; mask the serial status byte
.F4F7  85 90    STA $90   ; set the serial status byte
.F4F9  20 E1 FF JSR $FFE1   ; scan stop key, return Zb = 1 = [STOP]
.F4FC  D0 03    BNE $F501   ; if not [STOP] go ??
.F4FE  4C 33 F6 JMP $F633   ; else close the serial bus device and flag stop
.F501  20 13 EE JSR $EE13   ; input byte from serial bus
.F504  AA       TAX   ; copy byte
.F505  A5 90    LDA $90   ; get the serial status byte
.F507  4A       LSR   ; shift time out read ..
.F508  4A       LSR   ; .. into carry bit
.F509  B0 E8    BCS $F4F3   ; if timed out go try again
.F50B  8A       TXA   ; copy received byte back
.F50C  A4 93    LDY $93   ; get load/verify flag
.F50E  F0 0C    BEQ $F51C   ; if load go load else is verify
.F510  A0 00    LDY #$00   ; clear index
.F512  D1 AE    CMP ($AE),Y   ; compare byte with previously loaded byte
.F514  F0 08    BEQ $F51E   ; if match go ??
.F516  A9 10    LDA #$10   ; flag read error
.F518  20 1C FE JSR $FE1C   ; OR into the serial status byte
.F51B  2C       .BYTE $2C   ; makes next line BIT $AE91
.F51C  91 AE    STA ($AE),Y   ; save byte to memory
.F51E  E6 AE    INC $AE   ; increment save pointer low byte
.F520  D0 02    BNE $F524   ; if no rollover go ??
.F522  E6 AF    INC $AF   ; else increment save pointer high byte
.F524  24 90    BIT $90   ; test the serial status byte
.F526  50 CB    BVC $F4F3   ; loop if not end of file close file and exit
.F528  20 EF ED JSR $EDEF   ; command serial bus to UNTALK
.F52B  20 42 F6 JSR $F642   ; close serial bus device
.F52E  90 79    BCC $F5A9   ; if ?? go flag ok and exit
.F530  4C 04 F7 JMP $F704   ; do file not found error and return
```


## Commenti

### Original Disassembly (—)
- **$F4A5**: save load/verify flag
- **$F4A7**: clear A
- **$F4A9**: clear the serial status byte
- **$F4AB**: get the device number
- **$F4AD**: if not the keyboard continue do 'illegal device number'
- **$F4AF**: else do 'illegal device number' and return
- **$F4B8**: get file name length
- **$F4BA**: if not null name go ??
- **$F4BC**: else do 'missing file name' error and return
- **$F4BF**: get the secondary address
- **$F4C1**: print "Searching..."
- **$F4C6**: save the secondary address
- **$F4C8**: send secondary address and filename
- **$F4CB**: get the device number
- **$F4CD**: command serial bus device to TALK
- **$F4D0**: get the secondary address
- **$F4D2**: send secondary address after TALK
- **$F4D5**: input byte from serial bus
- **$F4D8**: save program start address low byte
- **$F4DA**: get the serial status byte
- **$F4DC**: shift time out read ..
- **$F4DD**: .. into carry bit
- **$F4DE**: if timed out go do file not found error and return
- **$F4E0**: input byte from serial bus
- **$F4E3**: save program start address high byte
- **$F4E5**: copy secondary address
- **$F4E6**: load location not set in LOAD call, so continue with the load
- **$F4E8**: get the load address low byte
- **$F4EA**: save the program start address low byte
- **$F4EC**: get the load address high byte
- **$F4EE**: save the program start address high byte
- **$F4F3**: mask xxxx xx0x, clear time out read bit
- **$F4F5**: mask the serial status byte
- **$F4F7**: set the serial status byte
- **$F4F9**: scan stop key, return Zb = 1 = [STOP]
- **$F4FC**: if not [STOP] go ??
- **$F4FE**: else close the serial bus device and flag stop
- **$F501**: input byte from serial bus
- **$F504**: copy byte
- **$F505**: get the serial status byte
- **$F507**: shift time out read ..
- **$F508**: .. into carry bit
- **$F509**: if timed out go try again
- **$F50B**: copy received byte back
- **$F50C**: get load/verify flag
- **$F50E**: if load go load else is verify
- **$F510**: clear index
- **$F512**: compare byte with previously loaded byte
- **$F514**: if match go ??
- **$F516**: flag read error
- **$F518**: OR into the serial status byte
- **$F51B**: makes next line BIT $AE91
- **$F51C**: save byte to memory
- **$F51E**: increment save pointer low byte
- **$F520**: if no rollover go ??
- **$F522**: else increment save pointer high byte
- **$F524**: test the serial status byte
- **$F526**: loop if not end of file close file and exit
- **$F528**: command serial bus to UNTALK
- **$F52B**: close serial bus device
- **$F52E**: if ?? go flag ok and exit
- **$F530**: do file not found error and return

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*