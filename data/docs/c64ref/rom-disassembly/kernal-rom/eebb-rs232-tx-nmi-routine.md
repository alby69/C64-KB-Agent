---
title: RS232 Tx NMI routine
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
- 00d7-data
- eebb-rs-232-ausgabe
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EEBB
  address_end: $EED6
  symbol: rs232-tx-nmi-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EEBB**: get RS232 bit count'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EEBB**: Anzahl Bits zu senden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EEBB**: BITTS, RS232 out bit count'
---

# $EEBB — RS232 Tx NMI routine

## Disassemblatura
```assembly
.EEBB  A5 B4    LDA $B4   ; get RS232 bit count
.EEBD  F0 47    BEQ $EF06   ; if zero go setup next RS232 Tx byte and return
.EEBF  30 3F    BMI $EF00   ; if -ve go do stop bit(s) else bit count is non zero and +ve
.EEC1  46 B6    LSR $B6   ; shift RS232 output byte buffer
.EEC3  A2 00    LDX #$00   ; set $00 for bit = 0
.EEC5  90 01    BCC $EEC8   ; branch if bit was 0
.EEC7  CA       DEX   ; set $FF for bit = 1
.EEC8  8A       TXA   ; copy bit to A
.EEC9  45 BD    EOR $BD   ; EOR with RS232 parity byte
.EECB  85 BD    STA $BD   ; save RS232 parity byte
.EECD  C6 B4    DEC $B4   ; decrement RS232 bit count
.EECF  F0 06    BEQ $EED7   ; if RS232 bit count now zero go do parity bit save bit and exit
.EED1  8A       TXA   ; copy bit to A
.EED2  29 04    AND #$04   ; mask 0000 0x00, RS232 Tx DATA bit
.EED4  85 B5    STA $B5   ; save the next RS232 data bit to send
.EED6  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EEBB**: get RS232 bit count
- **$EEBD**: if zero go setup next RS232 Tx byte and return
- **$EEBF**: if -ve go do stop bit(s) else bit count is non zero and +ve
- **$EEC1**: shift RS232 output byte buffer
- **$EEC3**: set $00 for bit = 0
- **$EEC5**: branch if bit was 0
- **$EEC7**: set $FF for bit = 1
- **$EEC8**: copy bit to A
- **$EEC9**: EOR with RS232 parity byte
- **$EECB**: save RS232 parity byte
- **$EECD**: decrement RS232 bit count
- **$EECF**: if RS232 bit count now zero go do parity bit save bit and exit
- **$EED1**: copy bit to A
- **$EED2**: mask 0000 0x00, RS232 Tx DATA bit
- **$EED4**: save the next RS232 data bit to send

### Commodore-64-intern-Buch (Commodore)
- **$EEBB**: Anzahl Bits zu senden
- **$EEBD**: verzweige wenn Byte schon komplett übertragen
- **$EEBF**: verzweige falls Stopbit erforderlich
- **$EEC1**: nächstes Bit ins Carry schieben
- **$EEC3**: '0' falls Datenbit = 0
- **$EEC5**: verzweige wenn Datenbit gelöscht
- **$EEC7**: nein, dann X-Register =$FF
- **$EEC8**: X-Register in Akku
- **$EEC9**: mit Register für Paritybit verknüpfen
- **$EECB**: und abspeichern
- **$EECD**: Bitzähler erniedrigen
- **$EECF**: verzweige wenn alle Bits übertragen
- **$EED1**: alten Akku wiederherstellen
- **$EED2**: Bit 2 isolieren
- **$EED4**: und ins Ausgaberegister bringen
- **$EED6**: Rücksprung
- **$EED7**: Bit 5 (Parity)
- **$EED9**: RS 232 Befehlsregister abfragen
- **$EEDC**: verzweige wenn ohne Parity
- **$EEDE**: verzweige wenn feste Parität
- **$EEE0**: verzweige wenn ungerade Parität
- **$EEE2**: verzweige wenn Parity gleich eins
- **$EEE4**: verzweige wenn ja
- **$EEE6**: Parity $FF
- **$EEE7**: Bitzähler auf $FF
- **$EEE9**: RS 232 Kontrollregister laden
- **$EEEC**: verzweige wenn zwei Stopbits
- **$EEEE**: Bitzähler auf $FE
- **$EEF0**: unbedingter Sprung zur Berechnung der Stopbits
- **$EEF2**: Bitzähler erhöhen, keine Parity
- **$EEF4**: unbedingter Sprung zur Berechnung der Stopbits
- **$EEF6**: Parity
- **$EEF8**: verzweige wenn gleich 0, dann Null-Bit ausgeben
- **$EEFA**: unbedingter Sprung 1-Bit ausgeben
- **$EEFC**: Null-Bit ausgeben
- **$EEFE**: sonst 1-Bit ausgeben (feste Parität)
- **$EF00**: Bitzähler erhöhen
- **$EF02**: Wert für Stopbit
- **$EF04**: unbedingter Sprung
- **$EF06**: RS 232 Befehlsregister laden
- **$EF09**: Bit 0 ins Carry
- **$EF0A**: verzweige wenn 3-Line Handshake, Abfrage übergehen
- **$EF0C**: Port B abfragen
- **$EF0F**: verzweige wenn DSR fehlt
- **$EF11**: verzweige wenn CTS fehlt
- **$EF13**: 0 laden und
- **$EF15**: Parity-Register löschen
- **$EF17**: Register für zu sendendes Bit (Startbit)
- **$EF19**: Anzahl der zu übertragenden Bits
- **$EF1C**: als Bitzähler merken
- **$EF1E**: lade Zeiger für übertragenes Byte
- **$EF21**: alle Bytes übertragen ?
- **$EF24**: ja, dann abschließen
- **$EF26**: Datenbyte aus RS 232 Puffer holen
- **$EF28**: zum Senden übergeben
- **$EF2A**: Pufferzeiger erhöhen
- **$EF2D**: Rücksprung
- **$EF2E**: DSR (Data Set Ready) fehlt
- **$EF30**: Skip nach $EF33
- **$EF31**: CTS (Clear To Send) fehlt
- **$EF33**: mit Status verknüpfen
- **$EF36**: und setzen
- **$EF39**: NMI für
- **$EF3B**: Timer A löschen
- **$EF3E**: Flag für
- **$EF41**: RS 232 umdrehen
- **$EF43**: und speichern
- **$EF46**: IRR setzen, alle übrigen zulassen NMIs
- **$EF49**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EEBB**: BITTS, RS232 out bit count
- **$EEBD**: send new RS232 byte
- **$EEC1**: RODATA, RS232 out byte buffer
- **$EEC9**: ROPRTY, RS232 out parity
- **$EECD**: BITTS
- **$EED4**: NXTBIT, next RS232 bit to send
- **$EED9**: M51CDR, 6551 command register image
- **$EEDC**: no parity
- **$EEDE**: mark/space transmit
- **$EEE0**: even parity
- **$EEE2**: ROPRTY, out parity
- **$EEE7**: BITTS, out bit count
- **$EEE9**: M51CTR, 6551 control register image
- **$EEEC**: one stop bit only
- **$EEEE**: BITTS
- **$EEF2**: BITTS
- **$EEF6**: ROPRTY
- **$EF00**: BITTS

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*