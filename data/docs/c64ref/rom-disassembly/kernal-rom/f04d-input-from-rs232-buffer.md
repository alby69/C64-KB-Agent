---
title: input from RS232 buffer
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
- f04d-rs-232-setzen
- f07d-handshake
- rts
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F04D
  address_end: $F085
  symbol: input-from-rs232-buffer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F04D**: save the input device number'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F04D**: Gerätenummer speichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$F085**: F086 GET FROM RS232'
---

# $F04D — input from RS232 buffer

## Disassemblatura
```assembly
.F04D  85 99    STA $99   ; save the input device number
.F04F  AD 94 02 LDA $0294   ; get pseudo 6551 command register
.F052  4A       LSR   ; shift the handshake bit to Cb
.F053  90 28    BCC $F07D   ; if 3 line interface go ??
.F055  29 08    AND #$08   ; mask the duplex bit, pseudo 6551 command is >> 1
.F057  F0 24    BEQ $F07D   ; if full duplex go ??
.F059  A9 02    LDA #$02   ; mask 0000 00x0, RTS out
.F05B  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.F05E  10 AD    BPL $F00D   ; if DSR = 0 set no DSR and exit
.F060  F0 22    BEQ $F084   ; if RTS = 0 just exit
.F062  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F065  4A       LSR   ; shift the timer A interrupt enable bit to Cb
.F066  B0 FA    BCS $F062   ; loop while the timer A interrupt is enabled
.F068  AD 01 DD LDA $DD01   ; read VIA 2 DRB, RS232 port
.F06B  29 FD    AND #$FD   ; mask xxxx xx0x, clear RTS out
.F06D  8D 01 DD STA $DD01   ; save VIA 2 DRB, RS232 port
.F070  AD 01 DD LDA $DD01   ; read VIA 2 DRB, RS232 port
.F073  29 04    AND #$04   ; mask xxxx x1xx, DTR in
.F075  F0 F9    BEQ $F070   ; loop while DTR low
.F077  A9 90    LDA #$90   ; enable the FLAG interrupt
.F079  18       CLC   ; flag ok
.F07A  4C 3B EF JMP $EF3B   ; set VIA 2 ICR from A and return
.F07D  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.F080  29 12    AND #$12   ; mask 000x 00x0
.F082  F0 F3    BEQ $F077   ; if FLAG or timer B bits set go enable the FLAG interrupt
.F084  18       CLC   ; flag ok
.F085  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F04D**: save the input device number
- **$F04F**: get pseudo 6551 command register
- **$F052**: shift the handshake bit to Cb
- **$F053**: if 3 line interface go ??
- **$F055**: mask the duplex bit, pseudo 6551 command is >> 1
- **$F057**: if full duplex go ??
- **$F059**: mask 0000 00x0, RTS out
- **$F05B**: test VIA 2 DRB, RS232 port
- **$F05E**: if DSR = 0 set no DSR and exit
- **$F060**: if RTS = 0 just exit
- **$F062**: get the RS-232 interrupt enable byte
- **$F065**: shift the timer A interrupt enable bit to Cb
- **$F066**: loop while the timer A interrupt is enabled
- **$F068**: read VIA 2 DRB, RS232 port
- **$F06B**: mask xxxx xx0x, clear RTS out
- **$F06D**: save VIA 2 DRB, RS232 port
- **$F070**: read VIA 2 DRB, RS232 port
- **$F073**: mask xxxx x1xx, DTR in
- **$F075**: loop while DTR low
- **$F077**: enable the FLAG interrupt
- **$F079**: flag ok
- **$F07A**: set VIA 2 ICR from A and return
- **$F07D**: get the RS-232 interrupt enable byte
- **$F080**: mask 000x 00x0
- **$F082**: if FLAG or timer B bits set go enable the FLAG interrupt
- **$F084**: flag ok

### Commodore-64-intern-Buch (Commodore)
- **$F04D**: Gerätenummer speichern
- **$F04F**: RS 232 Befehlsregister laden
- **$F052**: Bit 0 ins Carry schieben
- **$F053**: verzweige wenn 3-Line- Handshake
- **$F055**: Bit für Dupex Mode isolieren
- **$F057**: verzweige wenn voll Dupex
- **$F059**: Maske für 'RTS OUT'
- **$F05B**: Data Set Ready abfragen
- **$F05E**: verzweige wenn nein
- **$F060**: Ready To Send abfragen
- **$F062**: RS 232 NMI Status laden
- **$F065**: Bit 0 ins Carry (Sendebetrieb aktiv)
- **$F066**: ja, warten bis beendet
- **$F068**: Port B laden
- **$F06B**: Request To Send
- **$F06D**: und wieder speichern
- **$F070**: Port B holen
- **$F073**: Bit für Data Terminal Ready
- **$F075**: verzweige wenn nein, warten
- **$F077**: NMI-Maske für 'Flag' laden
- **$F079**: Carry löschen (ok Kennzeichen)
- **$F07A**: NMI freigeben

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$F085**: F086 GET FROM RS232

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*