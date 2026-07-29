---
title: find the tape header, exit with header in buffer
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
- f72c-lesen
- stop
scraped_at: '2026-07-29'
c64ref:
  module: c64disasm
  source_files:
  - marko_mäkelä.txt
  - original_disassembly.txt
  - commodore-64-intern-buch.txt
  address: $F72C
  address_end: $F769
  symbol: find-the-tape-header-exit-with-header-in-buffer
  sources:
  - name: Original Disassembly
    author: —
    description: '- **$F72C**: get load/verify flag'
  - name: Commodore-64-intern-Buch
    author: Commodore
    description: '- **$F72C**: Load/Verify Flag laden'
  - name: Marko Mäkelä
    author: Marko Mäkelä
    description: Nessun commento disponibile.
---

# $F72C — find the tape header, exit with header in buffer

## Disassemblatura
```assembly
.F72C  A5 93    LDA $93   ; get load/verify flag
.F72E  48       PHA   ; save load/verify flag
.F72F  20 41 F8 JSR $F841   ; initiate tape read
.F732  68       PLA   ; restore load/verify flag
.F733  85 93    STA $93   ; save load/verify flag
.F735  B0 32    BCS $F769   ; exit if error
.F737  A0 00    LDY #$00   ; clear the index
.F739  B1 B2    LDA ($B2),Y   ; read first byte from tape buffer
.F73B  C9 05    CMP #$05   ; compare with logical end of the tape
.F73D  F0 2A    BEQ $F769   ; if end of the tape exit
.F73F  C9 01    CMP #$01   ; compare with header for a relocatable program file
.F741  F0 08    BEQ $F74B   ; if program file header go ??
.F743  C9 03    CMP #$03   ; compare with header for a non relocatable program file
.F745  F0 04    BEQ $F74B   ; if program file header go  ??
.F747  C9 04    CMP #$04   ; compare with data file header
.F749  D0 E1    BNE $F72C   ; if data file loop to find the tape header was a program file header
.F74B  AA       TAX   ; copy header type
.F74C  24 9D    BIT $9D   ; get message mode flag
.F74E  10 17    BPL $F767   ; exit if control messages off
.F750  A0 63    LDY #$63   ; index to "FOUND "
.F752  20 2F F1 JSR $F12F   ; display kernel I/O message
.F755  A0 05    LDY #$05   ; index to the tape filename
.F757  B1 B2    LDA ($B2),Y   ; get byte from tape buffer
.F759  20 D2 FF JSR $FFD2   ; output character to channel
.F75C  C8       INY   ; increment the index
.F75D  C0 15    CPY #$15   ; compare it with end+1
.F75F  D0 F6    BNE $F757   ; loop if more to do
.F761  A5 A1    LDA $A1   ; get the jiffy clock mid byte
.F763  20 E0 E4 JSR $E4E0   ; wait ~8.5 seconds for any key from the STOP key column
.F766  EA       NOP   ; waste cycles
.F767  18       CLC   ; flag no error
.F768  88       DEY   ; decrement the index
.F769  60       RTS
```


## Commenti

### Original Disassembly (—)
- **$F72C**: get load/verify flag
- **$F72E**: save load/verify flag
- **$F72F**: initiate tape read
- **$F732**: restore load/verify flag
- **$F733**: save load/verify flag
- **$F735**: exit if error
- **$F737**: clear the index
- **$F739**: read first byte from tape buffer
- **$F73B**: compare with logical end of the tape
- **$F73D**: if end of the tape exit
- **$F73F**: compare with header for a relocatable program file
- **$F741**: if program file header go ??
- **$F743**: compare with header for a non relocatable program file
- **$F745**: if program file header go  ??
- **$F747**: compare with data file header
- **$F749**: if data file loop to find the tape header was a program file header
- **$F74B**: copy header type
- **$F74C**: get message mode flag
- **$F74E**: exit if control messages off
- **$F750**: index to "FOUND "
- **$F752**: display kernel I/O message
- **$F755**: index to the tape filename
- **$F757**: get byte from tape buffer
- **$F759**: output character to channel
- **$F75C**: increment the index
- **$F75D**: compare it with end+1
- **$F75F**: loop if more to do
- **$F761**: get the jiffy clock mid byte
- **$F763**: wait ~8.5 seconds for any key from the STOP key column
- **$F766**: waste cycles
- **$F767**: flag no error
- **$F768**: decrement the index

### Commodore-64-intern-Buch (Commodore)
- **$F72C**: Load/Verify Flag laden
- **$F72E**: und retten
- **$F72F**: Block vom Band lesen
- **$F732**: L/V Flag wiederholen
- **$F733**: und speichern
- **$F735**: Fehler, dann beenden
- **$F737**: Zähler auf Null stellen
- **$F739**: Header-Typ testen
- **$F73B**: EOT ?
- **$F73D**: verzweige falls ja
- **$F73F**: BASIC-Programm ?
- **$F741**: verzweige falls ja
- **$F743**: Maschinenprogramm ?
- **$F745**: verzweige falls ja
- **$F747**: Daten-Header ?
- **$F749**: kein Header gefunden, dann erneut suchen
- **$F74B**: Kennzeichen merken
- **$F74C**: Direktmodus ?
- **$F74E**: nein, dann weiter
- **$F750**: Offset für 'FOUND'
- **$F752**: Meldung ausgeben
- **$F755**: Zeiger auf Filenamen
- **$F757**: Filenamen holen
- **$F759**: und ausgeben
- **$F75C**: Zeiger erhöhen
- **$F75D**: schon alle Buchstaben
- **$F75F**: verzweige wenn nein
- **$F761**: Akku mit mittelwertigem Time-Byte laden
- **$F763**: wartet auf Commodore-Taste oder Zeitschleife
- **$F766**: no operation
- **$F767**: Carry =0 (ok Kennzeichen)
- **$F768**: Y-REG auf $FF zur Kennzeich nung, daß kein EOT
- **$F769**: Rücksprung

### Marko Mäkelä (Marko Mäkelä)
Nessun commento disponibile.

---
*Fonte: [c64ref](https://github.com/mist64/c64ref) — Ultimate Commodore 64 Reference*