---
title: input a byte from the serial bus
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
- ee13-iec-bus-holen
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EE13
  address_end: $EE84
  symbol: input-a-byte-from-the-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EE13**: disable the interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EE13**: Interruptflag setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EE16**: CNTDN, counter'
---

# $EE13 — input a byte from the serial bus

## Disassemblatura
```assembly
.EE13  78       SEI   ; disable the interrupts
.EE14  A9 00    LDA #$00   ; set 0 bits to do, will flag EOI on timeout
.EE16  85 A5    STA $A5   ; save the serial bus bit count
.EE18  20 85 EE JSR $EE85   ; set the serial clock out high
.EE1B  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.EE1E  10 FB    BPL $EE1B   ; loop if the serial clock is low
.EE20  A9 01    LDA #$01   ; set the timeout count high byte
.EE22  8D 07 DC STA $DC07   ; save VIA 1 timer B high byte
.EE25  A9 19    LDA #$19   ; load timer B, timer B single shot, start timer B
.EE27  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.EE2A  20 97 EE JSR $EE97   ; set the serial data out high
.EE2D  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.EE30  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.EE33  29 02    AND #$02   ; mask 0000 00x0, timer A interrupt
.EE35  D0 07    BNE $EE3E   ; if timer A interrupt go ??
.EE37  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.EE3A  30 F4    BMI $EE30   ; loop if the serial clock is low
.EE3C  10 18    BPL $EE56   ; else go set 8 bits to do, branch always timer A timed out
.EE3E  A5 A5    LDA $A5   ; get the serial bus bit count
.EE40  F0 05    BEQ $EE47   ; if not already EOI then go flag EOI
.EE42  A9 02    LDA #$02   ; else error $02, read timeout
.EE44  4C B2 ED JMP $EDB2   ; set the serial status and exit
.EE47  20 A0 EE JSR $EEA0   ; set the serial data out low
.EE4A  20 85 EE JSR $EE85   ; set the serial clock out high
.EE4D  A9 40    LDA #$40   ; set EOI
.EE4F  20 1C FE JSR $FE1C   ; OR into the serial status byte
.EE52  E6 A5    INC $A5   ; increment the serial bus bit count, do error on the next timeout
.EE54  D0 CA    BNE $EE20   ; go try again, branch always
.EE56  A9 08    LDA #$08   ; set 8 bits to do
.EE58  85 A5    STA $A5   ; save the serial bus bit count
.EE5A  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE5D  CD 00 DD CMP $DD00   ; compare it with itself
.EE60  D0 F8    BNE $EE5A   ; if changing go try again
.EE62  0A       ASL   ; shift the serial data into the carry
.EE63  10 F5    BPL $EE5A   ; loop while the serial clock is low
.EE65  66 A4    ROR $A4   ; shift the data bit into the receive byte
.EE67  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.EE6A  CD 00 DD CMP $DD00   ; compare it with itself
.EE6D  D0 F8    BNE $EE67   ; if changing go try again
.EE6F  0A       ASL   ; shift the serial data into the carry
.EE70  30 F5    BMI $EE67   ; loop while the serial clock is high
.EE72  C6 A5    DEC $A5   ; decrement the serial bus bit count
.EE74  D0 E4    BNE $EE5A   ; loop if not all done
.EE76  20 A0 EE JSR $EEA0   ; set the serial data out low
.EE79  24 90    BIT $90   ; test the serial status byte
.EE7B  50 03    BVC $EE80   ; if EOI not set skip the bus end sequence
.EE7D  20 06 EE JSR $EE06   ; 1ms delay, clock high then data high
.EE80  A5 A4    LDA $A4   ; get the receive byte
.EE82  58       CLI   ; enable the interrupts
.EE83  18       CLC   ; flag ok
.EE84  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EE13**: disable the interrupts
- **$EE14**: set 0 bits to do, will flag EOI on timeout
- **$EE16**: save the serial bus bit count
- **$EE18**: set the serial clock out high
- **$EE1B**: get the serial data status in Cb
- **$EE1E**: loop if the serial clock is low
- **$EE20**: set the timeout count high byte
- **$EE22**: save VIA 1 timer B high byte
- **$EE25**: load timer B, timer B single shot, start timer B
- **$EE27**: save VIA 1 CRB
- **$EE2A**: set the serial data out high
- **$EE2D**: read VIA 1 ICR
- **$EE30**: read VIA 1 ICR
- **$EE33**: mask 0000 00x0, timer A interrupt
- **$EE35**: if timer A interrupt go ??
- **$EE37**: get the serial data status in Cb
- **$EE3A**: loop if the serial clock is low
- **$EE3C**: else go set 8 bits to do, branch always timer A timed out
- **$EE3E**: get the serial bus bit count
- **$EE40**: if not already EOI then go flag EOI
- **$EE42**: else error $02, read timeout
- **$EE44**: set the serial status and exit
- **$EE47**: set the serial data out low
- **$EE4A**: set the serial clock out high
- **$EE4D**: set EOI
- **$EE4F**: OR into the serial status byte
- **$EE52**: increment the serial bus bit count, do error on the next timeout
- **$EE54**: go try again, branch always
- **$EE56**: set 8 bits to do
- **$EE58**: save the serial bus bit count
- **$EE5A**: read VIA 2 DRA, serial port and video address
- **$EE5D**: compare it with itself
- **$EE60**: if changing go try again
- **$EE62**: shift the serial data into the carry
- **$EE63**: loop while the serial clock is low
- **$EE65**: shift the data bit into the receive byte
- **$EE67**: read VIA 2 DRA, serial port and video address
- **$EE6A**: compare it with itself
- **$EE6D**: if changing go try again
- **$EE6F**: shift the serial data into the carry
- **$EE70**: loop while the serial clock is high
- **$EE72**: decrement the serial bus bit count
- **$EE74**: loop if not all done
- **$EE76**: set the serial data out low
- **$EE79**: test the serial status byte
- **$EE7B**: if EOI not set skip the bus end sequence
- **$EE7D**: 1ms delay, clock high then data high
- **$EE80**: get the receive byte
- **$EE82**: enable the interrupts
- **$EE83**: flag ok

### Commodore-64-intern-Buch (Commodore)
- **$EE13**: Interruptflag setzen
- **$EE14**: $00 laden
- **$EE16**: und Zähler löschen
- **$EE18**: CLOCK auf LOW setzen
- **$EE1B**: CLOCK-IN LOW ?
- **$EE1E**: nein, dann warten
- **$EE20**: $01
- **$EE22**: in Timer B HIGH schreiben
- **$EE25**: Timer
- **$EE27**: starten
- **$EE2A**: DATA auf LOW setzen
- **$EE2D**: Interrupt Control Register
- **$EE30**: laden
- **$EE33**: Timer B abgelaufen ?
- **$EE35**: ja, 'TIME OUT'
- **$EE37**: CLOCK-IN HIGH ?
- **$EE3A**: nein, dann warten
- **$EE3C**: unbedingter Sprung
- **$EE3E**: lade Zähler
- **$EE40**: verzweige wenn $00
- **$EE42**: 'TIME OUT'
- **$EE44**: Status setzen
- **$EE47**: DATA auf HIGH setzen
- **$EE4A**: CLOCK auf LOW setzen
- **$EE4D**: Bit 6 für 'END OR IDENTIFY'
- **$EE4F**: Status setzen
- **$EE52**: Zähler erhöhen
- **$EE54**: unbedingter Sprung
- **$EE56**: $08 als
- **$EE58**: Bitzähler setzen
- **$EE5A**: Port A laden
- **$EE5D**: Änderung ?
- **$EE60**: verzweige wenn ja
- **$EE62**: Datenbit ins Carry schieben
- **$EE63**: erneut holen wenn CLOCK = 1
- **$EE65**: Datenbit in $A4 schieben
- **$EE67**: Port A laden
- **$EE6A**: Änderung ?
- **$EE6D**: verzweige wenn ja
- **$EE6F**: Datenbit ins Carry schieben
- **$EE70**: erneut wenn CLOCK = 0
- **$EE72**: Bitzähler veringerrn
- **$EE74**: verzweige wenn noch nicht alle 8 Bits gesendet
- **$EE76**: DATA auf HIGH setzen
- **$EE79**: Status
- **$EE7B**: verzweige wenn kein 'EOI' ?
- **$EE7D**: warten und Bits 101 senden
- **$EE80**: Datenbyte in Akku holen
- **$EE82**: Interruptflag löschen
- **$EE83**: Carry löschen
- **$EE84**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EE16**: CNTDN, counter
- **$EE18**: set CLK 1
- **$EE1B**: get serial in and clock
- **$EE1E**: wait for CLK = 1
- **$EE22**: setup CIA#1 timer B, high byte
- **$EE27**: set 1 shot, load and start CIA timer B
- **$EE2A**: set data 1
- **$EE30**: read CIA#1 ICR
- **$EE33**: test if timer B reaches zero
- **$EE35**: timeout
- **$EE37**: get serial in and clock
- **$EE3A**: CLK 1
- **$EE3C**: CLK 0
- **$EE3E**: CNTDN
- **$EE42**: flag read timeout
- **$EE44**: set I/O status word
- **$EE47**: set data 1
- **$EE4A**: set CLK 1
- **$EE4D**: flag EOI
- **$EE4F**: set I/O status word
- **$EE52**: increment CNTDN, counter
- **$EE54**: again
- **$EE56**: set up CNTDN to receive 8 bits
- **$EE5A**: serial bus I/O port
- **$EE5D**: compare
- **$EE60**: wait for serial bus to settle
- **$EE63**: wait for data in =1
- **$EE65**: roll in received bit in temp data area
- **$EE67**: serial bus I/O port
- **$EE6A**: compare
- **$EE6D**: wait for bus to settle
- **$EE70**: wait for data in =0
- **$EE72**: one bit received
- **$EE74**: repeat for all 8 bits
- **$EE76**: set data 1
- **$EE79**: STATUS, I/O status word
- **$EE7B**: not EOI
- **$EE7D**: handshake and exit without byte
- **$EE80**: read received byte
- **$EE82**: enable interrupts
- **$EE83**: clear carry, no errors

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*