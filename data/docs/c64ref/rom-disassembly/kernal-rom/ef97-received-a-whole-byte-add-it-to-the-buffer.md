---
title: received a whole byte, add it to the buffer
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
- ef97-weiterverarbeiten
- eor
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $EF97
  address_end: $EFDF
  symbol: received-a-whole-byte-add-it-to-the-buffer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EF97**: get index to Rx buffer end'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EF97**: Pufferzeiger laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $EF97 — received a whole byte, add it to the buffer

## Disassemblatura
```assembly
.EF97  AC 9B 02 LDY $029B   ; get index to Rx buffer end
.EF9A  C8       INY   ; increment index
.EF9B  CC 9C 02 CPY $029C   ; compare with index to Rx buffer start
.EF9E  F0 2A    BEQ $EFCA   ; if buffer full go do Rx overrun error
.EFA0  8C 9B 02 STY $029B   ; save index to Rx buffer end
.EFA3  88       DEY   ; decrement index
.EFA4  A5 AA    LDA $AA   ; get assembled byte
.EFA6  AE 98 02 LDX $0298   ; get bit count
.EFA9  E0 09    CPX #$09   ; compare with byte + stop
.EFAB  F0 04    BEQ $EFB1   ; branch if all nine bits received
.EFAD  4A       LSR   ; else shift byte
.EFAE  E8       INX   ; increment bit count
.EFAF  D0 F8    BNE $EFA9   ; loop, branch always
.EFB1  91 F7    STA ($F7),Y   ; save received byte to Rx buffer
.EFB3  A9 20    LDA #$20   ; mask 00x0 0000, parity enable bit
.EFB5  2C 94 02 BIT $0294   ; test the pseudo 6551 command register
.EFB8  F0 B4    BEQ $EF6E   ; branch if parity disabled
.EFBA  30 B1    BMI $EF6D   ; branch if mark or space parity
.EFBC  A5 A7    LDA $A7   ; get the RS232 received data bit
.EFBE  45 AB    EOR $AB   ; EOR with the receiver parity bit
.EFC0  F0 03    BEQ $EFC5
.EFC2  70 A9    BVS $EF6D   ; if ?? just exit
.EFC4  2C       .BYTE $2C   ; makes next line BIT $A650
.EFC5  50 A6    BVC $EF6D   ; if ?? just exit
.EFC7  A9 01    LDA #$01   ; set Rx parity error
.EFC9  2C       .BYTE $2C   ; makes next line BIT $04A9
.EFCA  A9 04    LDA #$04   ; set Rx overrun error
.EFCC  2C       .BYTE $2C   ; makes next line BIT $80A9
.EFCD  A9 80    LDA #$80   ; set Rx break error
.EFCF  2C       .BYTE $2C   ; makes next line BIT $02A9
.EFD0  A9 02    LDA #$02   ; set Rx frame error
.EFD2  0D 97 02 ORA $0297   ; OR it with the RS232 status byte
.EFD5  8D 97 02 STA $0297   ; save the RS232 status byte
.EFD8  4C 7E EF JMP $EF7E   ; setup to receive an RS232 bit and return
.EFDB  A5 AA    LDA $AA
.EFDD  D0 F1    BNE $EFD0   ; if ?? do frame error
.EFDF  F0 EC    BEQ $EFCD   ; else do break error, branch always
```


## Commenti

### Original Disassembly (—)
- **$EF97**: get index to Rx buffer end
- **$EF9A**: increment index
- **$EF9B**: compare with index to Rx buffer start
- **$EF9E**: if buffer full go do Rx overrun error
- **$EFA0**: save index to Rx buffer end
- **$EFA3**: decrement index
- **$EFA4**: get assembled byte
- **$EFA6**: get bit count
- **$EFA9**: compare with byte + stop
- **$EFAB**: branch if all nine bits received
- **$EFAD**: else shift byte
- **$EFAE**: increment bit count
- **$EFAF**: loop, branch always
- **$EFB1**: save received byte to Rx buffer
- **$EFB3**: mask 00x0 0000, parity enable bit
- **$EFB5**: test the pseudo 6551 command register
- **$EFB8**: branch if parity disabled
- **$EFBA**: branch if mark or space parity
- **$EFBC**: get the RS232 received data bit
- **$EFBE**: EOR with the receiver parity bit
- **$EFC2**: if ?? just exit
- **$EFC4**: makes next line BIT $A650
- **$EFC5**: if ?? just exit
- **$EFC7**: set Rx parity error
- **$EFC9**: makes next line BIT $04A9
- **$EFCA**: set Rx overrun error
- **$EFCC**: makes next line BIT $80A9
- **$EFCD**: set Rx break error
- **$EFCF**: makes next line BIT $02A9
- **$EFD0**: set Rx frame error
- **$EFD2**: OR it with the RS232 status byte
- **$EFD5**: save the RS232 status byte
- **$EFD8**: setup to receive an RS232 bit and return
- **$EFDD**: if ?? do frame error
- **$EFDF**: else do break error, branch always

### Commodore-64-intern-Buch (Commodore)
- **$EF97**: Pufferzeiger laden
- **$EF9A**: und erhöhen
- **$EF9B**: mit Empfangspuffer vergleichen
- **$EF9E**: verzweige wenn voll, dann Status setzen
- **$EFA0**: Pufferzeiger abspeichern
- **$EFA3**: und normalisieren
- **$EFA4**: empfangenes Byte laden
- **$EFA6**: Anzahl Datenbits laden
- **$EFA9**: 8 Bits plus ein Stopbit?
- **$EFAB**: verzweige wenn ja, ok
- **$EFAD**: sonst Bits in richtige Position schieben
- **$EFAE**: Datenbitzähler um 1 erhöhen
- **$EFAF**: unbedingter Sprung
- **$EFB1**: Byte in RS 232 Puffer schreiben
- **$EFB3**: Maskenwert für Paritätsprüfung
- **$EFB5**: Bit 5 im Kommandregister prüfen
- **$EFB8**: verzweige wenn Übertragung ohne Parity
- **$EFBA**: verzweige wenn festes Bit anstelle Parity
- **$EFBC**: empfangenes Paritybit laden
- **$EFBE**: mit berechneter Parity vergleichen
- **$EFC0**: verzweige wenn gleich, ok
- **$EFC2**: gerade Parity, dann ok
- **$EFC4**: Skip nach $EFC7
- **$EFC5**: verzweige wenn ungerade Parity, dann ok
- **$EFC7**: sonst Parity-Fehler
- **$EFC9**: Skip nach EFCC
- **$EFCA**: Empfängerpuffer voll
- **$EFCC**: Skip nach $EFCF
- **$EFCD**: Break-Befehl empfangen
- **$EFCF**: Skip nach $EFD2
- **$EFD0**: Rahmen-Fehler
- **$EFD2**: mit Code für RS-232 Status verknüpfen
- **$EFD5**: und speichern
- **$EFD8**: zum Empfang des nächsten Bytes springen
- **$EFDB**: empfangenes Byte
- **$EFDD**: ungleich 0, dann zu Rahmen- Fehler
- **$EFDF**: sonst zu Break-Befehl empfangen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*