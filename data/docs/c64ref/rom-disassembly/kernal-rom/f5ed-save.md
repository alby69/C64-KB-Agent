---
title: save
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
- 0200-buf
- bit
- close
- f5ed-standard-save-ram-entry
- f5fa-speichern-auf-iec-bus
- f642-file-auf-iec-bus-schlieen
- f65f-save-ram-to-cassette
- listen
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  address: $F5ED
  address_end: $F68E
  symbol: save
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F5ED**: get the device number'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F5ED — save

## Disassemblatura
```assembly
.F5ED  A5 BA    LDA $BA   ; get the device number
.F5EF  D0 03    BNE $F5F4   ; if not keyboard go ?? else ..
.F5F1  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F5F4  C9 03    CMP #$03   ; compare device number with screen
.F5F6  F0 F9    BEQ $F5F1   ; if screen do illegal device number and return
.F5F8  90 5F    BCC $F659   ; branch if < screen is greater than screen so is serial bus
.F5FA  A9 61    LDA #$61   ; set secondary address to $01 when a secondary address is to be sent to a device on the serial bus the address must first be ORed with $60
.F5FC  85 B9    STA $B9   ; save the secondary address
.F5FE  A4 B7    LDY $B7   ; get the file name length
.F600  D0 03    BNE $F605   ; if filename not null continue
.F602  4C 10 F7 JMP $F710   ; else do 'missing file name' error and return
.F605  20 D5 F3 JSR $F3D5   ; send secondary address and filename
.F608  20 8F F6 JSR $F68F   ; print saving <file name>
.F60B  A5 BA    LDA $BA   ; get the device number
.F60D  20 0C ED JSR $ED0C   ; command devices on the serial bus to LISTEN
.F610  A5 B9    LDA $B9   ; get the secondary address
.F612  20 B9 ED JSR $EDB9   ; send secondary address after LISTEN
.F615  A0 00    LDY #$00   ; clear index
.F617  20 8E FB JSR $FB8E   ; copy I/O start address to buffer address
.F61A  A5 AC    LDA $AC   ; get buffer address low byte
.F61C  20 DD ED JSR $EDDD   ; output byte to serial bus
.F61F  A5 AD    LDA $AD   ; get buffer address high byte
.F621  20 DD ED JSR $EDDD   ; output byte to serial bus
.F624  20 D1 FC JSR $FCD1   ; check read/write pointer, return Cb = 1 if pointer >= end
.F627  B0 16    BCS $F63F   ; go do UNLISTEN if at end
.F629  B1 AC    LDA ($AC),Y   ; get byte from buffer
.F62B  20 DD ED JSR $EDDD   ; output byte to serial bus
.F62E  20 E1 FF JSR $FFE1   ; scan stop key
.F631  D0 07    BNE $F63A   ; if stop not pressed go increment pointer and loop for next else .. close the serial bus device and flag stop
.F633  20 42 F6 JSR $F642   ; close serial bus device
.F636  A9 00    LDA #$00
.F638  38       SEC   ; flag stop
.F639  60       RTS
.F63A  20 DB FC JSR $FCDB   ; increment read/write pointer
.F63D  D0 E5    BNE $F624   ; loop, branch always
.F63F  20 FE ED JSR $EDFE   ; command serial bus to UNLISTEN close serial bus device
.F642  24 B9    BIT $B9   ; test the secondary address
.F644  30 11    BMI $F657   ; if already closed just exit
.F646  A5 BA    LDA $BA   ; get the device number
.F648  20 0C ED JSR $ED0C   ; command devices on the serial bus to LISTEN
.F64B  A5 B9    LDA $B9   ; get the secondary address
.F64D  29 EF    AND #$EF   ; mask the channel number
.F64F  09 E0    ORA #$E0   ; OR with the CLOSE command
.F651  20 B9 ED JSR $EDB9   ; send secondary address after LISTEN
.F654  20 FE ED JSR $EDFE   ; command serial bus to UNLISTEN
.F657  18       CLC   ; flag ok
.F658  60       RTS
.F659  4A       LSR
.F65A  B0 03    BCS $F65F   ; if not RS232 device ??
.F65C  4C 13 F7 JMP $F713   ; else do 'illegal device number' and return
.F65F  20 D0 F7 JSR $F7D0   ; get tape buffer start pointer in XY
.F662  90 8D    BCC $F5F1   ; if < $0200 do illegal device number and return
.F664  20 38 F8 JSR $F838   ; wait for PLAY/RECORD
.F667  B0 25    BCS $F68E   ; exit if STOP was pressed
.F669  20 8F F6 JSR $F68F   ; print saving <file name>
.F66C  A2 03    LDX #$03   ; set header for a non relocatable program file
.F66E  A5 B9    LDA $B9   ; get the secondary address
.F670  29 01    AND #$01   ; mask non relocatable bit
.F672  D0 02    BNE $F676   ; if non relocatable program go ??
.F674  A2 01    LDX #$01   ; else set header for a relocatable program file
.F676  8A       TXA   ; copy header type to A
.F677  20 6A F7 JSR $F76A   ; write tape header
.F67A  B0 12    BCS $F68E   ; exit if error
.F67C  20 67 F8 JSR $F867   ; do tape write, 20 cycle count
.F67F  B0 0D    BCS $F68E   ; exit if error
.F681  A5 B9    LDA $B9   ; get the secondary address
.F683  29 02    AND #$02   ; mask end of tape flag
.F685  F0 06    BEQ $F68D   ; if not end of tape go ??
.F687  A9 05    LDA #$05   ; else set logical end of the tape
.F689  20 6A F7 JSR $F76A   ; write tape header
.F68C  24       .BYTE $24   ; makes next line BIT $18 so Cb is not changed
.F68D  18       CLC   ; flag ok
.F68E  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F5ED**: get the device number
- **$F5EF**: if not keyboard go ?? else ..
- **$F5F1**: else do 'illegal device number' and return
- **$F5F4**: compare device number with screen
- **$F5F6**: if screen do illegal device number and return
- **$F5F8**: branch if < screen is greater than screen so is serial bus
- **$F5FA**: set secondary address to $01 when a secondary address is to be sent to a device on the serial bus the address must first be ORed with $60
- **$F5FC**: save the secondary address
- **$F5FE**: get the file name length
- **$F600**: if filename not null continue
- **$F602**: else do 'missing file name' error and return
- **$F605**: send secondary address and filename
- **$F608**: print saving <file name>
- **$F60B**: get the device number
- **$F60D**: command devices on the serial bus to LISTEN
- **$F610**: get the secondary address
- **$F612**: send secondary address after LISTEN
- **$F615**: clear index
- **$F617**: copy I/O start address to buffer address
- **$F61A**: get buffer address low byte
- **$F61C**: output byte to serial bus
- **$F61F**: get buffer address high byte
- **$F621**: output byte to serial bus
- **$F624**: check read/write pointer, return Cb = 1 if pointer >= end
- **$F627**: go do UNLISTEN if at end
- **$F629**: get byte from buffer
- **$F62B**: output byte to serial bus
- **$F62E**: scan stop key
- **$F631**: if stop not pressed go increment pointer and loop for next else .. close the serial bus device and flag stop
- **$F633**: close serial bus device
- **$F638**: flag stop
- **$F63A**: increment read/write pointer
- **$F63D**: loop, branch always
- **$F63F**: command serial bus to UNLISTEN close serial bus device
- **$F642**: test the secondary address
- **$F644**: if already closed just exit
- **$F646**: get the device number
- **$F648**: command devices on the serial bus to LISTEN
- **$F64B**: get the secondary address
- **$F64D**: mask the channel number
- **$F64F**: OR with the CLOSE command
- **$F651**: send secondary address after LISTEN
- **$F654**: command serial bus to UNLISTEN
- **$F657**: flag ok
- **$F65A**: if not RS232 device ??
- **$F65C**: else do 'illegal device number' and return
- **$F65F**: get tape buffer start pointer in XY
- **$F662**: if < $0200 do illegal device number and return
- **$F664**: wait for PLAY/RECORD
- **$F667**: exit if STOP was pressed
- **$F669**: print saving <file name>
- **$F66C**: set header for a non relocatable program file
- **$F66E**: get the secondary address
- **$F670**: mask non relocatable bit
- **$F672**: if non relocatable program go ??
- **$F674**: else set header for a relocatable program file
- **$F676**: copy header type to A
- **$F677**: write tape header
- **$F67A**: exit if error
- **$F67C**: do tape write, 20 cycle count
- **$F67F**: exit if error
- **$F681**: get the secondary address
- **$F683**: mask end of tape flag
- **$F685**: if not end of tape go ??
- **$F687**: else set logical end of the tape
- **$F689**: write tape header
- **$F68C**: makes next line BIT $18 so Cb is not changed
- **$F68D**: flag ok

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*