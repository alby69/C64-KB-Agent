---
title: RS232 NMI routine
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
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $FE72
  address_end: $FEC1
  symbol: rs232-nmi-routine
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$FE73**: AND with the RS-232 interrupt enable byte'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$FE72**: ICR-Register'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: '- **$FE72**: Read CIA#2 interrupt control register'
---

# $FE72 — RS232 NMI routine

## Disassemblatura
```assembly
.FE72  98       TYA
.FE73  2D A1 02 AND $02A1   ; AND with the RS-232 interrupt enable byte
.FE76  AA       TAX
.FE77  29 01    AND #$01
.FE79  F0 28    BEQ $FEA3
.FE7B  AD 00 DD LDA $DD00   ; read VIA 2 DRA, serial port and video address
.FE7E  29 FB    AND #$FB   ; mask xxxx x0xx, clear RS232 Tx DATA
.FE80  05 B5    ORA $B5   ; OR in the RS232 transmit data bit
.FE82  8D 00 DD STA $DD00   ; save VIA 2 DRA, serial port and video address
.FE85  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.FE88  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FE8B  8A       TXA
.FE8C  29 12    AND #$12
.FE8E  F0 0D    BEQ $FE9D
.FE90  29 02    AND #$02
.FE92  F0 06    BEQ $FE9A
.FE94  20 D6 FE JSR $FED6
.FE97  4C 9D FE JMP $FE9D
.FE9A  20 07 FF JSR $FF07
.FE9D  20 BB EE JSR $EEBB
.FEA0  4C B6 FE JMP $FEB6
.FEA3  8A       TXA   ; get active interrupts back
.FEA4  29 02    AND #$02   ; mask ?? interrupt
.FEA6  F0 06    BEQ $FEAE   ; branch if not ?? interrupt was ?? interrupt
.FEA8  20 D6 FE JSR $FED6
.FEAB  4C B6 FE JMP $FEB6
.FEAE  8A       TXA   ; get active interrupts back
.FEAF  29 10    AND #$10   ; mask CB1 interrupt, Rx data bit transition
.FEB1  F0 03    BEQ $FEB6   ; if no bit restore registers and exit interrupt
.FEB3  20 07 FF JSR $FF07
.FEB6  AD A1 02 LDA $02A1   ; get the RS-232 interrupt enable byte
.FEB9  8D 0D DD STA $DD0D   ; save VIA 2 ICR
.FEBC  68       PLA   ; pull Y
.FEBD  A8       TAY   ; restore Y
.FEBE  68       PLA   ; pull X
.FEBF  AA       TAX   ; restore X
.FEC0  68       PLA   ; restore A
.FEC1  40       RTI
```


## Commenti

### Original Disassembly (—)
- **$FE73**: AND with the RS-232 interrupt enable byte
- **$FE7B**: read VIA 2 DRA, serial port and video address
- **$FE7E**: mask xxxx x0xx, clear RS232 Tx DATA
- **$FE80**: OR in the RS232 transmit data bit
- **$FE82**: save VIA 2 DRA, serial port and video address
- **$FE85**: get the RS-232 interrupt enable byte
- **$FE88**: save VIA 2 ICR
- **$FEA3**: get active interrupts back
- **$FEA4**: mask ?? interrupt
- **$FEA6**: branch if not ?? interrupt was ?? interrupt
- **$FEAE**: get active interrupts back
- **$FEAF**: mask CB1 interrupt, Rx data bit transition
- **$FEB1**: if no bit restore registers and exit interrupt
- **$FEB6**: get the RS-232 interrupt enable byte
- **$FEB9**: save VIA 2 ICR
- **$FEBC**: pull Y
- **$FEBD**: restore Y
- **$FEBE**: pull X
- **$FEBF**: restore X
- **$FEC0**: restore A

### Commodore-64-intern-Buch (Commodore)
- **$FE72**: ICR-Register
- **$FE73**: mit RS 232 NMI-Flag verknüp.
- **$FE76**: nach X retten
- **$FE77**: Sendebetrieb aktiv ?
- **$FE79**: nein
- **$FE7B**: Datenport lesen
- **$FE7E**: Bit 2 TXD löschen
- **$FE80**: zu sendendes Bit übergeben
- **$FE82**: und wieder in Datenport spei.
- **$FE85**: RS-232 NMI-Flag
- **$FE88**: wieder in ICR schreiben
- **$FE8B**: Wert aus X zurückholen
- **$FE8C**: Bit 1 und 4 isolieren
- **$FE8E**: Bit 1 und 4=0: Bit empfangen
- **$FE90**: Bit 1, Aufruf von Timer B
- **$FE92**: nein: verzweige zu Startbit
- **$FE94**: empfangenes Bit verarbeiten
- **$FE97**: Vorbereitung für Byte umgehen
- **$FE9A**: Vorbereitung für Empfang des nächsten Bytes
- **$FE9D**: Empfang des nächsten Bits v.
- **$FEA0**: Rückkehr vom Interrupt
- **$FEA3**: X nach Akku
- **$FEA4**: Datenempfang ?
- **$FEA6**: verzweige wenn kein Empfang
- **$FEA8**: empfangenes Bit verarbeiten
- **$FEAB**: Rückkehr vom Interrupt
- **$FEAE**: X nach Akku
- **$FEAF**: warten auf Startbit ?
- **$FEB1**: verzweige wenn kein Startbit
- **$FEB3**: Vorbereitung für Empfang des nächsten Bytes
- **$FEB6**: RS-232 NMI-Flag
- **$FEB9**: wieder in ICR
- **$FEBC**: Y-Register vom Stapel
- **$FEBD**: zurückholen
- **$FEBE**: X-Register
- **$FEBF**: zurückholen
- **$FEC0**: Akku zurückholen
- **$FEC1**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
- **$FE72**: Read CIA#2 interrupt control register
- **$FE73**: mask with ENABL, RS232 enable
- **$FE76**: temp store in (X)
- **$FE77**: test if sending (%00000001)
- **$FE79**: nope, jump to receive test
- **$FE7B**: load CIA#1 DRA
- **$FE7E**: mask bit2 (RS232 send)
- **$FE80**: NXTBIT, next bit to send
- **$FE82**: and write to port
- **$FE88**: write ENABL to CIA#2 I.C.R
- **$FE8B**: get temp
- **$FE8C**: test if receiving (bit1), or waiting for receiver edge (bit4) ($12 = %00010010)
- **$FE8E**: nope, skip receiver routine
- **$FE90**: test if receiving
- **$FE92**: nope
- **$FE94**: jump to NMI RS232 in
- **$FE9A**: jump to NMI RS232 out
- **$FE9D**: RS232 send byte
- **$FEA0**: goto exit
- **$FEA3**: get temp
- **$FEA4**: test bit1
- **$FEA6**: nope
- **$FEA8**: NMI RS232 in???
- **$FEAB**: goto exit
- **$FEAE**: set temp
- **$FEAF**: test bit4
- **$FEB1**: nope, exit
- **$FEB3**: NMI RS232 out
- **$FEB6**: ENABL
- **$FEB9**: CIA#2 interrupt control register
- **$FEBC**: restore registers (Y),(X),(A)
- **$FEC1**: back from NMI

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*