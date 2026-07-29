---
title: open RS232 channel for output
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
- efe1-rs-232
- f00d-no-dsr-error
- rts
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $EFE1
  address_end: $F013
  symbol: open-rs232-channel-for-output
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$EFE1**: save the output device number'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$EFE1**: Gerätenummer abspeichern'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$EFE1**: DFLTO, default output device'
---

# $EFE1 — open RS232 channel for output

## Disassemblatura
```assembly
.EFE1  85 9A    STA $9A   ; save the output device number
.EFE3  AD 94 02 LDA $0294   ; read the pseudo 6551 command register
.EFE6  4A       LSR   ; shift handshake bit to carry
.EFE7  90 29    BCC $F012   ; if 3 line interface go ??
.EFE9  A9 02    LDA #$02   ; mask 0000 00x0, RTS out
.EFEB  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.EFEE  10 1D    BPL $F00D   ; if DSR = 0 set DSR not present and exit
.EFF0  D0 20    BNE $F012   ; if RTS = 1 just exit
.EFF2  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.EFF5  29 02    AND #$02   ; mask 0000 00x0, timer B interrupt
.EFF7  D0 F9    BNE $EFF2   ; loop while the timer B interrupt is enabled
.EFF9  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.EFFC  70 FB    BVS $EFF9   ; loop while CTS high
.EFFE  AD 01 DD LDA $DD01   ; read VIA 2 DRB, RS232 port
.F001  09 02    ORA #$02   ; mask xxxx xx1x, set RTS high
.F003  8D 01 DD STA $DD01   ; save VIA 2 DRB, RS232 port
.F006  2C 01 DD BIT $DD01   ; test VIA 2 DRB, RS232 port
.F009  70 07    BVS $F012   ; exit if CTS high
.F00B  30 F9    BMI $F006   ; loop while DSR high set no DSR and exit
.F00D  A9 40    LDA #$40   ; set DSR signal not present
.F00F  8D 97 02 STA $0297   ; save the RS232 status register
.F012  18       CLC   ; flag ok
.F013  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$EFE1**: save the output device number
- **$EFE3**: read the pseudo 6551 command register
- **$EFE6**: shift handshake bit to carry
- **$EFE7**: if 3 line interface go ??
- **$EFE9**: mask 0000 00x0, RTS out
- **$EFEB**: test VIA 2 DRB, RS232 port
- **$EFEE**: if DSR = 0 set DSR not present and exit
- **$EFF0**: if RTS = 1 just exit
- **$EFF2**: get the RS-232 interrupt enable byte
- **$EFF5**: mask 0000 00x0, timer B interrupt
- **$EFF7**: loop while the timer B interrupt is enabled
- **$EFF9**: test VIA 2 DRB, RS232 port
- **$EFFC**: loop while CTS high
- **$EFFE**: read VIA 2 DRB, RS232 port
- **$F001**: mask xxxx xx1x, set RTS high
- **$F003**: save VIA 2 DRB, RS232 port
- **$F006**: test VIA 2 DRB, RS232 port
- **$F009**: exit if CTS high
- **$F00B**: loop while DSR high set no DSR and exit
- **$F00D**: set DSR signal not present
- **$F00F**: save the RS232 status register
- **$F012**: flag ok

### Commodore-64-intern-Buch (Commodore)
- **$EFE1**: Gerätenummer abspeichern
- **$EFE3**: RS 232 Kommandregister laden
- **$EFE6**: Bit 0 (Handshake) ins Carry
- **$EFE7**: verzweige wenn 3-Line- Handshake
- **$EFE9**: Haske für DATA SET READY
- **$EFEB**: Port B auslesen
- **$EFEE**: kein DSR, dann Fehler
- **$EFF0**: verzweige wenn kein Request To Send
- **$EFF2**: RS-232 NMI Status Laden
- **$EFF5**: verknüpfe mit Bit für Datenempfang aktiv
- **$EFF7**: warten bis Empfang beendet
- **$EFF9**: Port B der NMI-CIA auslesen
- **$EFFC**: und auf Clear To Send warten
- **$EFFE**: Port B lesen
- **$F001**: Bit für Request To Send setzen
- **$F003**: und wieder zurückschreiben
- **$F006**: Port B holen und
- **$F009**: auf Clear To Send warten
- **$F00B**: verzweige wenn nicht Data Set Ready
- **$F00D**: Bit für fehlendes DSR
- **$F00F**: Status setzen
- **$F012**: Carry für ok Kennzeichen setzen
- **$F013**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$EFE1**: DFLTO, default output device
- **$EFE3**: M51CDR, 6551 command register image
- **$EFE7**: 3 line mode, no handshaking, exit
- **$EFEB**: RS232 I/O port
- **$EFEE**: no DRS, error
- **$EFF2**: ENABL, RS232 enables
- **$EFF9**: RS232 I/O port
- **$EFFC**: wait for no CTS
- **$F003**: set RTS
- **$F009**: CTS set
- **$F00B**: wait for no DSR

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*