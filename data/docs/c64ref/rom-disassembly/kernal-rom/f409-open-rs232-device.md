---
title: open RS232 device
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
- f409-rs-232-open
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - magnus_nyman.txt
  - commodore-64-intern-buch.txt
  address: $F409
  address_end: $F47B
  symbol: open-rs232-device
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F409**: initialise RS232 output'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F409**: CIAs setzen'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
  - name: Magnus Nyman
    author: Magnus Nyman
    description: Nessun commento disponibile.
---

# $F409 — open RS232 device

## Disassemblatura
```assembly
.F409  20 83 F4 JSR $F483   ; initialise RS232 output
.F40C  8C 97 02 STY $0297   ; save the RS232 status register
.F40F  C4 B7    CPY $B7   ; compare with file name length
.F411  F0 0A    BEQ $F41D   ; exit loop if done
.F413  B1 BB    LDA ($BB),Y   ; get file name byte
.F415  99 93 02 STA $0293,Y   ; copy to 6551 register set
.F418  C8       INY   ; increment index
.F419  C0 04    CPY #$04   ; compare with $04
.F41B  D0 F2    BNE $F40F   ; loop if not to 4 yet
.F41D  20 4A EF JSR $EF4A   ; compute bit count
.F420  8E 98 02 STX $0298   ; save bit count
.F423  AD 93 02 LDA $0293   ; get pseudo 6551 control register
.F426  29 0F    AND #$0F   ; mask 0000 xxxx, baud rate
.F428  F0 1C    BEQ $F446   ; if zero skip the baud rate setup
.F42A  0A       ASL   ; * 2 bytes per entry
.F42B  AA       TAX   ; copy to the index
.F42C  AD A6 02 LDA $02A6   ; get the PAL/NTSC flag
.F42F  D0 09    BNE $F43A   ; if PAL go set PAL timing
.F431  BC C1 FE LDY $FEC1,X   ; get the NTSC baud rate value high byte
.F434  BD C0 FE LDA $FEC0,X   ; get the NTSC baud rate value low byte
.F437  4C 40 F4 JMP $F440   ; go save the baud rate values
.F43A  BC EB E4 LDY $E4EB,X   ; get the PAL baud rate value high byte
.F43D  BD EA E4 LDA $E4EA,X   ; get the PAL baud rate value low byte
.F440  8C 96 02 STY $0296   ; save the nonstandard bit timing high byte
.F443  8D 95 02 STA $0295   ; save the nonstandard bit timing low byte
.F446  AD 95 02 LDA $0295   ; get the nonstandard bit timing low byte
.F449  0A       ASL   ; * 2
.F44A  20 2E FF JSR $FF2E
.F44D  AD 94 02 LDA $0294   ; read the pseudo 6551 command register
.F450  4A       LSR   ; shift the X line/3 line bit into Cb
.F451  90 09    BCC $F45C   ; if 3 line skip the DRS test
.F453  AD 01 DD LDA $DD01   ; read VIA 2 DRB, RS232 port
.F456  0A       ASL   ; shift DSR in into Cb
.F457  B0 03    BCS $F45C   ; if DSR present skip the error set
.F459  20 0D F0 JSR $F00D   ; set no DSR
.F45C  AD 9B 02 LDA $029B   ; get index to Rx buffer end
.F45F  8D 9C 02 STA $029C   ; set index to Rx buffer start, clear Rx buffer
.F462  AD 9E 02 LDA $029E   ; get index to Tx buffer end
.F465  8D 9D 02 STA $029D   ; set index to Tx buffer start, clear Tx buffer
.F468  20 27 FE JSR $FE27   ; read the top of memory
.F46B  A5 F8    LDA $F8   ; get the RS232 input buffer pointer high byte
.F46D  D0 05    BNE $F474   ; if buffer already set skip the save
.F46F  88       DEY   ; decrement top of memory high byte, 256 byte buffer
.F470  84 F8    STY $F8   ; save the RS232 input buffer pointer high byte
.F472  86 F7    STX $F7   ; save the RS232 input buffer pointer low byte
.F474  A5 FA    LDA $FA   ; get the RS232 output buffer pointer high byte
.F476  D0 05    BNE $F47D   ; if ?? go set the top of memory to F0xx
.F478  88       DEY
.F479  84 FA    STY $FA   ; save the RS232 output buffer pointer high byte
.F47B  86 F9    STX $F9   ; save the RS232 output buffer pointer low byte
```


## Commenti

### Original Disassembly (—)
- **$F409**: initialise RS232 output
- **$F40C**: save the RS232 status register
- **$F40F**: compare with file name length
- **$F411**: exit loop if done
- **$F413**: get file name byte
- **$F415**: copy to 6551 register set
- **$F418**: increment index
- **$F419**: compare with $04
- **$F41B**: loop if not to 4 yet
- **$F41D**: compute bit count
- **$F420**: save bit count
- **$F423**: get pseudo 6551 control register
- **$F426**: mask 0000 xxxx, baud rate
- **$F428**: if zero skip the baud rate setup
- **$F42A**: * 2 bytes per entry
- **$F42B**: copy to the index
- **$F42C**: get the PAL/NTSC flag
- **$F42F**: if PAL go set PAL timing
- **$F431**: get the NTSC baud rate value high byte
- **$F434**: get the NTSC baud rate value low byte
- **$F437**: go save the baud rate values
- **$F43A**: get the PAL baud rate value high byte
- **$F43D**: get the PAL baud rate value low byte
- **$F440**: save the nonstandard bit timing high byte
- **$F443**: save the nonstandard bit timing low byte
- **$F446**: get the nonstandard bit timing low byte
- **$F449**: * 2
- **$F44D**: read the pseudo 6551 command register
- **$F450**: shift the X line/3 line bit into Cb
- **$F451**: if 3 line skip the DRS test
- **$F453**: read VIA 2 DRB, RS232 port
- **$F456**: shift DSR in into Cb
- **$F457**: if DSR present skip the error set
- **$F459**: set no DSR
- **$F45C**: get index to Rx buffer end
- **$F45F**: set index to Rx buffer start, clear Rx buffer
- **$F462**: get index to Tx buffer end
- **$F465**: set index to Tx buffer start, clear Tx buffer
- **$F468**: read the top of memory
- **$F46B**: get the RS232 input buffer pointer high byte
- **$F46D**: if buffer already set skip the save
- **$F46F**: decrement top of memory high byte, 256 byte buffer
- **$F470**: save the RS232 input buffer pointer high byte
- **$F472**: save the RS232 input buffer pointer low byte
- **$F474**: get the RS232 output buffer pointer high byte
- **$F476**: if ?? go set the top of memory to F0xx
- **$F479**: save the RS232 output buffer pointer high byte
- **$F47B**: save the RS232 output buffer pointer low byte

### Commodore-64-intern-Buch (Commodore)
- **$F409**: CIAs setzen
- **$F40C**: RS-232 Status löschen
- **$F40F**: Länge des "Filenamens"
- **$F411**: verzweige wenn kein Filename
- **$F413**: die ersten
- **$F415**: vier
- **$F418**: Zeichen
- **$F419**: speichern
- **$F41B**: verzweige wenn noch nicht alle vier Zeichen
- **$F41D**: Anzahl der Datenbits berechnen
- **$F420**: und speichern
- **$F423**: Kontrollregister holen
- **$F426**: Bits für Baud-Rate isolieren
- **$F428**: verzweige wenn User-Baud-Rate
- **$F42A**: mal 2 für Tabelle
- **$F42B**: als Zeiger merken
- **$F42C**: NTSC-Version
- **$F42F**: verzweige wenn nein
- **$F431**: Baud-Rate, HIGH für NTSC-Timing
- **$F434**: Baud-Rate, LOW
- **$F437**: überspringe zwei Befehle
- **$F43A**: Baud-Rate, HIGH für PAL-Timing
- **$F43D**: Baud-Rate, LOW
- **$F440**: HIGH-Byte speichern
- **$F443**: LOW-Byte speichern
- **$F446**: Timerwert = Baud-Rate * zwei + $C8 (200)
- **$F449**: Timer LOW * zwei
- **$F44A**: Timerwert für Baud-Rate ermitteln
- **$F44D**: Kommandoregister laden
- **$F450**: Prüfe ob 3-Line-Handshake
- **$F451**: verzweige wenn ja
- **$F453**: Prüfe ob Data Set Ready
- **$F456**: Bit 7 ins Carry
- **$F457**: verzweige wenn DSR vorhanden
- **$F459**: Status für DSR setzen
- **$F45C**: Anfang RS-232 Eingabepuffer
- **$F45F**: mit Ende des Eingabepuffers gleichsetzen
- **$F462**: Anfang des RS-232 Ausgabepuffers
- **$F465**: mit Ende des Ausgabepuffers gleichsetzen
- **$F468**: Memory Top holen
- **$F46B**: HIGH-Byte des Zeigers auf RS-232 Eingabepuffer
- **$F46D**: ungleich Null, so Eingabe- puffer bereits angelegt
- **$F46F**: HIGH-Byte Memory Top -1
- **$F470**: als Zeiger für RS-232 Eingabepuffer speichern
- **$F472**: LOW-Byte Memory Top als LOW- Byte Eingabepuffer setzen
- **$F474**: HIGH-Byte des Zeigers auf RS-232 Ausgabepuffer
- **$F476**: verzweige wenn Ausgabepuffer bereits angelegt
- **$F478**: HIGH-Byte des Memory Top -1
- **$F479**: und als Zeiger für RS-232 Ausgabepuffer setzen
- **$F47B**: LOW-Byte Memory Top als LOW- Byte Ausgabepuffer setzen
- **$F47D**: Carry =1 (Fehlerkennzeichen)
- **$F47E**: Ftag für Puffer schützen/ freigeben setzen
- **$F480**: Memory-Top neu setzen

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

### Magnus Nyman (Magnus Nyman)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*