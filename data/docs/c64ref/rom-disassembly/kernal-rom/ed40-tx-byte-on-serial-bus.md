---
title: Tx byte on serial bus
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
- ed40-ausgeben
- edad-flag-errors
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $ED40
  address_end: $EDB7
  symbol: tx-byte-on-serial-bus
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$ED40**: disable the interrupts'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$ED40**: Interruptflag setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$ED40**: disable interrupts'
---

# $ED40 — Tx byte on serial bus

## Disassemblatura
```assembly
.ED40  78       SEI   ; disable the interrupts
.ED41  20 97 EE JSR $EE97   ; set the serial data out high
.ED44  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.ED47  B0 64    BCS $EDAD   ; if the serial data is high go do 'device not present'
.ED49  20 85 EE JSR $EE85   ; set the serial clock out high
.ED4C  24 A3    BIT $A3   ; test the EOI flag
.ED4E  10 0A    BPL $ED5A   ; if not EOI go ?? I think this is the EOI sequence so the serial clock has been released and the serial data is being held low by the peripheral. first up wait for the serial data to rise
.ED50  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.ED53  90 FB    BCC $ED50   ; loop if the data is low now the data is high, EOI is signalled by waiting for at least 200us without pulling the serial clock line low again. the listener should respond by pulling the serial data line low
.ED55  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.ED58  B0 FB    BCS $ED55   ; loop if the data is high the serial data has gone low ending the EOI sequence, now just wait for the serial data line to go high again or, if this isn't an EOI sequence, just wait for the serial data to go high the first time
.ED5A  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.ED5D  90 FB    BCC $ED5A   ; loop if the data is low serial data is high now pull the clock low, preferably within 60us
.ED5F  20 8E EE JSR $EE8E   ; set the serial clock out low now the C64 has to send the eight bits, LSB first. first it sets the serial data line to reflect the bit in the byte, then it sets the serial clock to high. The serial clock is left high for 26 cycles, 23us on a PAL Vic, before it is again pulled low and the serial data is allowed high again
.ED62  A9 08    LDA #$08   ; eight bits to do
.ED64  85 A5    STA $A5   ; set serial bus bit count
.ED66  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.ED69  CD 00 DD CMP $DD00   ; compare it with itself
.ED6C  D0 F8    BNE $ED66   ; if changed go try again
.ED6E  0A       ASL   ; shift the serial data into Cb
.ED6F  90 3F    BCC $EDB0   ; if the serial data is low go do serial bus timeout
.ED71  66 95    ROR $95   ; rotate the transmit byte
.ED73  B0 05    BCS $ED7A   ; if the bit = 1 go set the serial data out high
.ED75  20 A0 EE JSR $EEA0   ; else set the serial data out low
.ED78  D0 03    BNE $ED7D   ; continue, branch always
.ED7A  20 97 EE JSR $EE97   ; set the serial data out high
.ED7D  20 85 EE JSR $EE85   ; set the serial clock out high
.ED80  EA       NOP   ; waste ..
.ED81  EA       NOP   ; .. a ..
.ED82  EA       NOP   ; .. cycle ..
.ED83  EA       NOP   ; .. or two
.ED84  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.ED87  29 DF    AND #$DF   ; mask xx0x xxxx, set the serial data out high
.ED89  09 10    ORA #$10   ; mask xxx1 xxxx, set the serial clock out low
.ED8B  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.ED8E  C6 A5    DEC $A5   ; decrement the serial bus bit count
.ED90  D0 D4    BNE $ED66   ; loop if not all done now all eight bits have been sent it's up to the peripheral to signal the byte was received by pulling the serial data low. this should be done within one millisecond
.ED92  A9 04    LDA #$04   ; wait for up to about 1ms
.ED94  8D 07 DC STA $DC07   ; save VIA 1 timer B high byte
.ED97  A9 19    LDA #$19   ; load timer B, timer B single shot, start timer B
.ED99  8D 0F DC STA $DC0F   ; save VIA 1 CRB
.ED9C  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.ED9F  AD 0D DC LDA $DC0D   ; read VIA 1 ICR
.EDA2  29 02    AND #$02   ; mask 0000 00x0, timer A interrupt
.EDA4  D0 0A    BNE $EDB0   ; if timer A interrupt go do serial bus timeout
.EDA6  20 A9 EE JSR $EEA9   ; get the serial data status in Cb
.EDA9  B0 F4    BCS $ED9F   ; if the serial data is high go wait some more
.EDAB  58       CLI   ; enable the interrupts
.EDAC  60       RTS   ; device not present
.EDAD  A9 80    LDA #$80   ; error $80, device not present
.EDAF  2C       .BYTE $2C   ; makes next line BIT $03A9 timeout on serial bus
.EDB0  A9 03    LDA #$03   ; error $03, read timeout, write timeout
.EDB2  20 1C FE JSR $FE1C   ; OR into the serial status byte
.EDB5  58       CLI   ; enable the interrupts
.EDB6  18       CLC   ; clear for branch
.EDB7  90 4A    BCC $EE03   ; ATN high, delay, clock high then data high, branch always
```


## Commenti

### Original Disassembly (—)
- **$ED40**: disable the interrupts
- **$ED41**: set the serial data out high
- **$ED44**: get the serial data status in Cb
- **$ED47**: if the serial data is high go do 'device not present'
- **$ED49**: set the serial clock out high
- **$ED4C**: test the EOI flag
- **$ED4E**: if not EOI go ?? I think this is the EOI sequence so the serial clock has been released and the serial data is being held low by the peripheral. first up wait for the serial data to rise
- **$ED50**: get the serial data status in Cb
- **$ED53**: loop if the data is low now the data is high, EOI is signalled by waiting for at least 200us without pulling the serial clock line low again. the listener should respond by pulling the serial data line low
- **$ED55**: get the serial data status in Cb
- **$ED58**: loop if the data is high the serial data has gone low ending the EOI sequence, now just wait for the serial data line to go high again or, if this isn't an EOI sequence, just wait for the serial data to go high the first time
- **$ED5A**: get the serial data status in Cb
- **$ED5D**: loop if the data is low serial data is high now pull the clock low, preferably within 60us
- **$ED5F**: set the serial clock out low now the C64 has to send the eight bits, LSB first. first it sets the serial data line to reflect the bit in the byte, then it sets the serial clock to high. The serial clock is left high for 26 cycles, 23us on a PAL Vic, before it is again pulled low and the serial data is allowed high again
- **$ED62**: eight bits to do
- **$ED64**: set serial bus bit count
- **$ED66**: read VIA 2 DRA, serial port and video address
- **$ED69**: compare it with itself
- **$ED6C**: if changed go try again
- **$ED6E**: shift the serial data into Cb
- **$ED6F**: if the serial data is low go do serial bus timeout
- **$ED71**: rotate the transmit byte
- **$ED73**: if the bit = 1 go set the serial data out high
- **$ED75**: else set the serial data out low
- **$ED78**: continue, branch always
- **$ED7A**: set the serial data out high
- **$ED7D**: set the serial clock out high
- **$ED80**: waste ..
- **$ED81**: .. a ..
- **$ED82**: .. cycle ..
- **$ED83**: .. or two
- **$ED84**: read VIA 2 DRA, serial port and video address
- **$ED87**: mask xx0x xxxx, set the serial data out high
- **$ED89**: mask xxx1 xxxx, set the serial clock out low
- **$ED8B**: save VIA 2 DRA, serial port and video address
- **$ED8E**: decrement the serial bus bit count
- **$ED90**: loop if not all done now all eight bits have been sent it's up to the peripheral to signal the byte was received by pulling the serial data low. this should be done within one millisecond
- **$ED92**: wait for up to about 1ms
- **$ED94**: save VIA 1 timer B high byte
- **$ED97**: load timer B, timer B single shot, start timer B
- **$ED99**: save VIA 1 CRB
- **$ED9C**: read VIA 1 ICR
- **$ED9F**: read VIA 1 ICR
- **$EDA2**: mask 0000 00x0, timer A interrupt
- **$EDA4**: if timer A interrupt go do serial bus timeout
- **$EDA6**: get the serial data status in Cb
- **$EDA9**: if the serial data is high go wait some more
- **$EDAB**: enable the interrupts
- **$EDAC**: device not present
- **$EDAD**: error $80, device not present
- **$EDAF**: makes next line BIT $03A9 timeout on serial bus
- **$EDB0**: error $03, read timeout, write timeout
- **$EDB2**: OR into the serial status byte
- **$EDB5**: enable the interrupts
- **$EDB6**: clear for branch
- **$EDB7**: ATN high, delay, clock high then data high, branch always

### Commodore-64-intern-Buch (Commodore)
- **$ED40**: Interruptflag setzen
- **$ED41**: DATA auf LOW setzen
- **$ED44**: Hardware-Rückmeldung aus DATA holen
- **$ED47**: DATA LOW, dann 'DEVICE NOT PRESENT'
- **$ED49**: CLOCK auf LOW setzen
- **$ED4C**: Bit für EOI gesetzt?
- **$ED4E**: nein, dann verzweige
- **$ED50**: DATA ins Carry
- **$ED53**: warten bis Listener bereit
- **$ED55**: DATA ins Carry
- **$ED58**: warten auf DATA HIGH
- **$ED5A**: DATA ins Carry
- **$ED5D**: warten bis bereit für Daten
- **$ED5F**: CLOCK auf HIGH setzen
- **$ED62**: Bitzähler für serielle
- **$ED64**: Ausgabe setzen ($08 Bits)
- **$ED66**: Port A lesen
- **$ED69**: und entprellen
- **$ED6C**: verzweige wenn Änderung
- **$ED6E**: Datenbit ins Carry
- **$ED6F**: DATA HIGH, dann 'TIME OUT'
- **$ED71**: nächstes Bit zur Ausgabe bereitstellen
- **$ED73**: verzweige wenn Bit gesetzt
- **$ED75**: DATA auf HIGH setzen
- **$ED78**: unbedingter Sprung
- **$ED7A**: DATA auf LOW setzen
- **$ED7D**: CLOCK auf LOW setzen
- **$ED80**: Listener
- **$ED81**: 8 Microsekunden Zeit zur
- **$ED82**: Verarbeitung der
- **$ED83**: Daten geben
- **$ED84**: Port A laden
- **$ED87**: DATA auf LOW
- **$ED89**: und CLOCK auf HIGH
- **$ED8B**: setzen
- **$ED8E**: nächstes Bit
- **$ED90**: mache weiter wenn noch nicht alle Bits gesendet
- **$ED92**: $04 als Timerwert setzen
- **$ED94**: Timer B HIGH, ca. eine ms
- **$ED97**: und Timer B
- **$ED99**: starten
- **$ED9C**: Interrupt control register
- **$ED9F**: laden
- **$EDA2**: Timer B abgelaufen ?
- **$EDA4**: ja, dann 'TIME OUT'
- **$EDA6**: DATA ins Carry
- **$EDA9**: warten auf DATA HIGH
- **$EDAB**: Interruptflag löschen
- **$EDAC**: Rücksprung
- **$EDAD**: 'DEVICE NOT PRESENT'
- **$EDAF**: Skip nach $EDB2
- **$EDB0**: 'TIME OUT'
- **$EDB2**: Status setzen
- **$EDB5**: Interruptflag löschen
- **$EDB6**: Carry setzen
- **$EDB7**: unbedingter Sprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$ED40**: disable interrupts
- **$ED41**: set data 1
- **$ED44**: get serial in and clock
- **$ED47**: no activity, device not present.
- **$ED49**: set CLK 1
- **$ED4C**: temp data area
- **$ED50**: get serial in and clock
- **$ED53**: wait for indata = 0
- **$ED55**: get serial in and clock
- **$ED58**: wait for indata = 1
- **$ED5A**: get serial in and clock
- **$ED5D**: wait for indata = 0
- **$ED5F**: set CLK 0
- **$ED62**: output 8 bits
- **$ED71**: BSOUR, buffered character for bus
- **$ED73**: prepare to output 1
- **$ED75**: else, serial output 0
- **$ED8E**: decrement bit counter
- **$ED90**: next bit till all 8 are done
- **$ED94**: CIA timer B, high byte
- **$ED99**: set 1 shot, load and start CIA timer B
- **$ED9C**: CIA ICR
- **$EDA2**: timeout
- **$EDA4**: yep, flag write timeout
- **$EDA6**: get serial in and clock
- **$EDAB**: enable interrupts

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*