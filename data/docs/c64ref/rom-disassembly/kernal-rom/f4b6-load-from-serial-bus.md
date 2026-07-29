---
title: LOAD FROM SERIAL BUS
source_url: https://github.com/mist64/c64ref/blob/main/src/c64disasm/magnus_nyman.txt
category: source-code
topics:
- rom-disassembly
- kernal-rom
difficulty: advanced
language: assembly
hardware:
- C64
related:
- 0090-status
- 00ae-eal
- 00b7-fnlen
- 00c3-memuss
- ece7-load
- f4b6-load-from-serial-bus
- f4b8-iec-load
- stop
- talk
- untalk
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - magnus_nyman.txt
  address: $F4B6
  address_end: $F5A8
  symbol: load-from-serial-bus
  sources:
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F4B6**: device < 3, e.g. tape or RS232, illegal device'
---

# $F4B6 — LOAD FROM SERIAL BUS

## Disassemblatura
```assembly
.F4B6  90 7B    BCC $F533   ; device < 3, e.g. tape or RS232, illegal device
.F4B8  A4 B7    LDY $B7   ; FNLEN, length of filename
.F4BA  D0 03    BNE $F4BF   ; if length not is zero
.F4BC  4C 10 F7 JMP $F710   ; 'MISSING FILENAME'
.F4BF  A6 B9    LDX $B9   ; SA, current secondary address
.F4C1  20 AF F5 JSR $F5AF   ; print "SEARCHING"
.F4C4  A9 60    LDA #$60
.F4C6  85 B9    STA $B9   ; set SA to $60
.F4C8  20 D5 F3 JSR $F3D5   ; send SA and filename
.F4CB  A5 BA    LDA $BA   ; FA, current devicenumber
.F4CD  20 09 ED JSR $ED09   ; send TALK to serial bus
.F4D0  A5 B9    LDA $B9   ; SA
.F4D2  20 C7 ED JSR $EDC7   ; send TALK SA
.F4D5  20 13 EE JSR $EE13   ; receive from serial bus
.F4D8  85 AE    STA $AE   ; load address, <EAL
.F4DA  A5 90    LDA $90   ; check STATUS
.F4DC  4A       LSR
.F4DD  4A       LSR
.F4DE  B0 50    BCS $F530   ; EOI set, file not found
.F4E0  20 13 EE JSR $EE13   ; receive from serial bus
.F4E3  85 AF    STA $AF   ; load address, >EAL
.F4E5  8A       TXA   ; retrieve SA and test relocated load
.F4E6  D0 08    BNE $F4F0
.F4E8  A5 C3    LDA $C3   ; use MEMUSS as load address
.F4EA  85 AE    STA $AE   ; store in <EAL
.F4EC  A5 C4    LDA $C4
.F4EE  85 AF    STA $AF   ; store in >EAL
.F4F0  20 D2 F5 JSR $F5D2
.F4F3  A9 FD    LDA #$FD   ; mask %11111101
.F4F5  25 90    AND $90   ; read ST
.F4F7  85 90    STA $90
.F4F9  20 E1 FF JSR $FFE1   ; scan <STOP>
.F4FC  D0 03    BNE $F501   ; not stopped
.F4FE  4C 33 F6 JMP $F633
.F501  20 13 EE JSR $EE13      A   ; CPTR, receive from serial bus
.F504  AA       TAX
.F505  A5 90    LDA $90
.F507  4A       LSR
.F508  4A       LSR
.F509  B0 E8    BCS $F4F3
.F50B  8A       TXA
.F50C  A4 93    LDY $93
.F50E  F0 0C    BEQ $F51C   ; jump to LOAD
.F510  A0 00    LDY #$00
.F512  D1 AE    CMP ($AE),Y   ; compare with memory
.F514  F0 08    BEQ $F51E   ; verified byte OK
.F516  A9 10    LDA #$10
.F518  20 1C FE JSR $FE1C
.F51B  2C       .BYTE $2C   ; mask next write command
.F51C  91 AE    STA ($AE),Y   ; store in memory
.F51E  E6 AE    INC $AE   ; increment <EAL, next address
.F520  D0 02    BNE $F524   ; skip MSB
.F522  E6 AF    INC $AF   ; increment >EAL
.F524  24 90    BIT $90   ; test STATUS
.F526  50 CB    BVC $F4F3   ; get next byte
.F528  20 EF ED JSR $EDEF   ; send UNTALK to serial bus
.F52B  20 42 F6 JSR $F642
.F52E  90 79    BCC $F5A9   ; end routine
.F530  4C 04 F7 JMP $F704   ; I/O error #4, file not found
.F533  4A       LSR
.F534  B0 03    BCS $F539
.F536  4C 13 F7 JMP $F713
.F539  20 D0 F7 JSR $F7D0
.F53C  B0 03    BCS $F541
.F53E  4C 13 F7 JMP $F713
.F541  20 17 F8 JSR $F817
.F544  B0 68    BCS $F5AE
.F546  20 AF F5 JSR $F5AF
.F549  A5 B7    LDA $B7
.F54B  F0 09    BEQ $F556
.F54D  20 EA F7 JSR $F7EA
.F550  90 0B    BCC $F55D
.F552  F0 5A    BEQ $F5AE
.F554  B0 DA    BCS $F530
.F556  20 2C F7 JSR $F72C
.F559  F0 53    BEQ $F5AE
.F55B  B0 D3    BCS $F530
.F55D  A5 90    LDA $90
.F55F  29 10    AND #$10
.F561  38       SEC
.F562  D0 4A    BNE $F5AE
.F564  E0 01    CPX #$01
.F566  F0 11    BEQ $F579
.F568  E0 03    CPX #$03
.F56A  D0 DD    BNE $F549
.F56C  A0 01    LDY #$01
.F56E  B1 B2    LDA ($B2),Y
.F570  85 C3    STA $C3
.F572  C8       INY
.F573  B1 B2    LDA ($B2),Y
.F575  85 C4    STA $C4
.F577  B0 04    BCS $F57D
.F579  A5 B9    LDA $B9
.F57B  D0 EF    BNE $F56C
.F57D  A0 03    LDY #$03
.F57F  B1 B2    LDA ($B2),Y
.F581  A0 01    LDY #$01
.F583  F1 B2    SBC ($B2),Y
.F585  AA       TAX
.F586  A0 04    LDY #$04
.F588  B1 B2    LDA ($B2),Y
.F58A  A0 02    LDY #$02
.F58C  F1 B2    SBC ($B2),Y
.F58E  A8       TAY
.F58F  18       CLC
.F590  8A       TXA
.F591  65 C3    ADC $C3
.F593  85 AE    STA $AE
.F595  98       TYA
.F596  65 C4    ADC $C4
.F598  85 AF    STA $AF
.F59A  A5 C3    LDA $C3
.F59C  85 C1    STA $C1
.F59E  A5 C4    LDA $C4
.F5A0  85 C2    STA $C2
.F5A2  20 D2 F5 JSR $F5D2
.F5A5  20 4A F8 JSR $F84A
.F5A8  24       .BYTE $24
```


## Commenti

### Magnus Nyman (Magnus Nyman)
- **$F4B6**: device < 3, e.g. tape or RS232, illegal device
- **$F4B8**: FNLEN, length of filename
- **$F4BA**: if length not is zero
- **$F4BC**: 'MISSING FILENAME'
- **$F4BF**: SA, current secondary address
- **$F4C1**: print "SEARCHING"
- **$F4C6**: set SA to $60
- **$F4C8**: send SA and filename
- **$F4CB**: FA, current devicenumber
- **$F4CD**: send TALK to serial bus
- **$F4D0**: SA
- **$F4D2**: send TALK SA
- **$F4D5**: receive from serial bus
- **$F4D8**: load address, <EAL
- **$F4DA**: check STATUS
- **$F4DE**: EOI set, file not found
- **$F4E0**: receive from serial bus
- **$F4E3**: load address, >EAL
- **$F4E5**: retrieve SA and test relocated load
- **$F4E8**: use MEMUSS as load address
- **$F4EA**: store in <EAL
- **$F4EE**: store in >EAL
- **$F4F3**: mask %11111101
- **$F4F5**: read ST
- **$F4F9**: scan <STOP>
- **$F4FC**: not stopped
- **$F501**: CPTR, receive from serial bus
- **$F50E**: jump to LOAD
- **$F512**: compare with memory
- **$F514**: verified byte OK
- **$F51B**: mask next write command
- **$F51C**: store in memory
- **$F51E**: increment <EAL, next address
- **$F520**: skip MSB
- **$F522**: increment >EAL
- **$F524**: test STATUS
- **$F526**: get next byte
- **$F528**: send UNTALK to serial bus
- **$F52E**: end routine
- **$F530**: I/O error #4, file not found

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*